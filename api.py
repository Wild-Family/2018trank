# -*- coding:utf-8 -*-
from bottle import route, run, view, static_file, url
from bottle import get, request, response
import os
#import picamera
import pygame.mixer

pygame.mixer.init()
sound1 = pygame.mixer.Sound("./take1.wav")
#sound2 = pygame.mixer.Sound("nc2036.wav")
   
#camera = picamera.PiCamera()

save_path = "./img/"

@route('/start/<id>')
def main(id):
    return str(id)

@route('/status/<id>')
def status(id):
    #take picture
    global save_path
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
    global save_path
    pic_name = id + ".jpg"
    pic_loc = save_path + pic_name

    if not os.path.isfile(pic_loc):
        return "file do not exists"

    response.content_type = 'image/jpg'
    with open(pic_loc, 'rb') as fh:
        content = fh.read()
        response.set_header('Content-Length', str(len(content)))
        return content
    #return "faile do not exists"

#TODO:localhost setting
run(host='localhost', port=8080, debug=True)