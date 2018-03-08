# -*- coding:utf-8 -*-
from bottle import route, run, view, static_file, url
from bottle import get, request, response
import os
import picamera
import pygame.mixer
import json
import argparse

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw


camera = picamera.PiCamera()

pygame.mixer.init()
sound1 = pygame.mixer.Sound("./take1.wav")
#sound2 = pygame.mixer.Sound("nc2036.wav")

save_path = "./img/"

def check_face_loc(face_box,left_eye,right_eye,nose_tip):
    if((face_box[0][0]-face_box[1][0])*(face_box[1][1]-face_box[2][1]) < 200 * 200):#ここ調整
        print("もう少し近づいて")
        return "move forward"
    if(face_box[0][0] > 1024*1/2):
        return "right" #被写体は右に
    if(face_box[1][0] < 1024*1/2):
        return "left" #被写体は左に
    if(face_box[0][1] > 768*1/2):
        return "forward" #顔はもう少し上に
    if(face_box[3][1] < 768*1/2):
        return "back" #顔はもう少し下に
    
    
    # print(nose_tip.x)
    # if(nose_tip.x < 1024*4/7):
    #     print("もうちょい右やで")    
    #     return "move right"
    # if(nose_tip.x > 1024*4/7):
    #     print("もうちょい左やで")
    #     return "move left"
    # if(nose_tip.y < 768*4/7):
    #     print("もうちょい下(後ろに下がって)")
    #     return "get back"
    # if(nose_tip.y > 768*4/7):
    #     print("もうちょい上(前に出て)")
    #     return "move forward"
    return "ok"

def detect_face(face_file, max_results=4):
    client = vision.ImageAnnotatorClient()
    content = face_file.read()
    image = types.Image(content=content)
    return client.face_detection(image=image).face_annotations


def highlight_faces(image, faces):
    for face in faces:
        left_eye =  face.landmarks[0].position
        right_eye = face.landmarks[1].position
        nose_tip =  face.landmarks[7].position

        box = [(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]#(左上、右上、右下、左下)
        #print(faces)
        #print(face.landmarks[0].position)#左目
        #print(face.landmarks[1].position)#右目
    #print(left_eye)
    #print(right_eye)
    #print(nose_tip)
    print(box)
    return check_face_loc(box,left_eye,right_eye,nose_tip)

def main(input_filename,max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_results)
        image.seek(0)
        return highlight_faces(image, faces)

@route('/start/<id>')
def main(id):
    return str(id)

@route('/status/<id>')
def status(id):
    #take picture
    global save_path
    pic_name  =  id + ".jpg"
    pic_loc   = save_path + pic_name
    for x in range(1,4):
        sound1.play()
        #time.sleep(1)
    camera.resolution = (1024,768) 
    camera.capture(pic_loc)

    return pic_loc

@route('/pic/<id>')
def get_pic(id):
    global save_path
    pic_name = id + ".jpg"
    pic_loc = save_path + pic_name

    if not os.path.isfile(pic_loc):
        return "file do not exists"

    response.content_type = 'image/jpg'
    with open(pic_loc, 'rb') as fh:
        content = fh.read()
        response.set_header('Content-Length', str(len(content)))
        os.remove(pic_loc)
        return content
    #return "faile do not exists"

#TODO:localhost setting
run(host='localhost', port=8080, debug=True)