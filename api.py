# -*- coding:utf-8 -*-
from bottle import route, run, view, static_file, url
from bottle import get, request
import os
#import picamera
import pygame.mixer

pygame.mixer.init()
sound1 = pygame.mixer.Sound("./take1.wav")
#sound2 = pygame.mixer.Sound("nc2036.wav")
   
#camera = picamera.PiCamera()

id = 0

@route('/start')
def main():
    id += 1
    return id

@route('/status/<id>')
def status(id):
    #take picture
    save_path = "./img/"
    pic_name  =  id + ".jpg"
    pic_loc   = save_path + pic_name
    #camera.resolution = (1024,768) 
    #camera.capture(pic_loc)

    #print picture
    for x in range(1,4):
        sound1.play()
        #time.sleep(1)

    #sound2.play()	
    #common.pic_print(pic_loc)
    
    return pic_loc

@route('/get_pic/<id>')
def get_pic(id):
    pic_name = id + ".jpg"
    if os.path.isfile(pic_name):
        return "file exists"
    return "file do not exists"


#TODO:localhost setting
run(host='192.168.167.214', port=8080, debug=True)