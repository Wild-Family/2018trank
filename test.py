import picamera
import pygame.mixer
import json
import argparse

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw

camera = picamera.PiCamera()

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

save_path = "./img/"


def check_face_loc(face_box,left_eye,right_eye,nose_tip,joyLikelihood):
    # if((face_box[0][0]-face_box[1][0])*(face_box[1][1]-face_box[2][1]) < 200 * 200):#ここ調整
    #     print("もう少し近づいて")
    #     return "forward"
    if(face_box[0][0] > 1024*1/2):
        right.play()
        return "right" #被写体は右に
    if(face_box[1][0] < 1024*1/2):
        left.play()
        return "left" #被写体は左に
    if(face_box[0][1] > 768*1/2):
        forward.play()
        return "forward" #顔はもう少し上に
    if(face_box[3][1] < 768*1/2):
        back.play()
        return "back" #顔はもう少し下に
    if(joyLikelihood == 1):
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

    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    for face in faces:
        left_eye =  face.landmarks[0].position
        right_eye = face.landmarks[1].position
        nose_tip =  face.landmarks[7].position
        joyLikelihood = face.joy_likelihood
        
        box = [(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]#(左上、右上、右下、左下)
        draw.line(box + [box[0]], width=5, fill='#00ff00')
    im.save("./output.jpg")
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

if __name__ == '__main__':
    pic_name  = "test.jpg"
    pic_loc   = save_path + pic_name

    count3.play()
    camera.resolution = (1024,768) 
    camera.capture(pic_loc)

    check_face_loc_result = get_face(pic_loc, 1)
    print(check_face_loc_result)