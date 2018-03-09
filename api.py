# -*- coding:utf-8 -*-
from bottle import route, run, view, static_file, url
from bottle import get, request, response
import os
import time
import picamera
import pygame.mixer
import json
import argparse

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw

# キュー
wait_flag = False
former_status = None


camera = picamera.PiCamera()
save_path = "./img/"

pygame.mixer.init()
start   = pygame.mixer.Sound("./take1.wav")
take    = pygame.mixer.Sound("./take.wav")
nobody  = pygame.mixer.Sound("./nobody.wav")
forward = pygame.mixer.Sound("./forward.wav")
back    = pygame.mixer.Sound("./back.wav")
left    = pygame.mixer.Sound("./left.wav")
right   = pygame.mixer.Sound("./right.wav")
smile   = pygame.mixer.Sound("./smile.wav")
end     = pygame.mixer.Sound("./end.wav")
angry   = pygame.mixer.Sound("./angry.wav")
count1  = pygame.mixer.Sound("./count1.wav")
count2  = pygame.mixer.Sound("./count2.wav")
count3  = pygame.mixer.Sound("./count3.wav")
shut    = pygame.mixer.Sound("./camera.wav")

forward_again   = pygame.mixer.Sound("./forward_again.wav")
back_again      = pygame.mixer.Sound("./back_again.wav")
right_again     = pygame.mixer.Sound("./right_again.wav")
left_again      = pygame.mixer.Sound("./left_again.wav")
smile_again     = pygame.mixer.Sound("./smile_again.wav")

def check_face_loc(face_box,left_eye,right_eye,nose_tip,joyLikelihood):
    global former_status
    if(face_box[0][0] > 1024*1/2):
        if former_status == "right":
            right_again.play()
            return "right again"
        former_status = "right"
        right.play()
        return "right" #被写体は右に
    if(face_box[1][0] < 1024*1/2):
        if former_status == "left":
            left_again.play()
            return "left again"
        former_status = "left"
        left.play()
        return "left" #被写体は左に
    if(face_box[0][1] > 768*1/2 or (face_box[0][0]-face_box[1][0])*(face_box[1][1]-face_box[2][1]) < 200 * 200):
        if former_status == "forward":
            forward_again.play()
            return "forward again"
        former_status = "forward"
        forward.play()
        return "forward" #顔はもう少し上に
    if(face_box[3][1] < 768*1/2 or (face_box[0][0]-face_box[1][0])*(face_box[1][1]-face_box[2][1]) > 500 * 500):
        if former_status == "back":
            back_again.play()
            return "back again"
        former_status = "back"
        back.play()
        return "back" #顔はもう少し下に
    if(joyLikelihood == 1):
        if former_status == "smile":
            smile_again.play()
            return "smile again"
        former_status = "smile"
        print("笑顔になって")
        smile.play()
        return "smile"
    return "ok"

def detect_face(face_file, max_results=4):
    client = vision.ImageAnnotatorClient()
    content = face_file.read()
    image = types.Image(content=content)
    return client.face_detection(image=image).face_annotations

def highlight_faces(image, faces):
    box = ((0,0), (0,0), (0,0), (0,0))
    left_eye = None
    right_eye = None
    nose_tip = None
    joyLikelihood = None

    for face in faces:
        left_eye =  face.landmarks[0].position
        right_eye = face.landmarks[1].position
        nose_tip =  face.landmarks[7].position
        joyLikelihood = face.joy_likelihood
    return check_face_loc(box,left_eye,right_eye,nose_tip,joyLikelihood)

def get_face(input_filename,max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image)
        if not faces:
            print("顔を認識できません")
            nobody.play()
            return "nobody"
        image.seek(0)
        return highlight_faces(image, faces)

@route('/start/<id>')
def main(id):
    global wait_flag

    print(wait_flag)
    if wait_flag:
        return "wait"
    wait_flag = True
    start.play()
    return str(id)

@route('/status/<id>')
def status(id):
    #take picture
    global save_path
    global camera
    global status_count

    pic_name  =  id + ".jpg"
    pic_loc   = save_path + pic_name
    camera.resolution = (1024,768) 
    camera.capture(pic_loc)
    status = get_face(pic_loc, 1)
    return status

@route('/pic/<id>')
def get_pic(id):
    global save_path
    global camera
    global wait_flag
    pic_name = id + ".jpg"
    pic_loc = save_path + pic_name

    # 撮影
    take.play()
    camera.resolution = (1024,768)
    count3.play()
    time.sleep(1)
    count2.play()
    time.sleep(1)
    count1.play()
    time.sleep(1)
    shut.play()
    camera.capture(pic_loc)

    # wait_flag
    wait_flag = False

    if not os.path.isfile(pic_loc):
        return "file do not exists"

    response.content_type = 'image/jpg'
    with open(pic_loc, 'rb') as fh:
        content = fh.read()
        response.set_header('Content-Length', str(len(content)))
        os.remove(pic_loc)
        return content
    #return "faile do not exists"

@route('/end/<id>')
def end_obachan(id):
    global former_status
    former_status = None
    end.play()

@route('/angry/<id>')
def angry_obachan(id):
    global wait_flag
    global former_status
    wait_flag = False
    former_status = None
    angry.play()
    return "angry"

#TODO:localhost setting
run(host='localhost', port=8080, debug=True)