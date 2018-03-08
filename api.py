# -*- coding:utf-8 -*-
from bottle import route, run, view, static_file, url
from bottle import get, post, request
from datetime import datetime
import random
#import picamera
import time
#import common
import pygame.mixer

pygame.mixer.init()
sound1 = pygame.mixer.Sound("./test.wav")
#sound2 = pygame.mixer.Sound("nc2036.wav")
   
#camera = picamera.PiCamera()

@route('/')
def main():
    return "test"

@route('/take')
def take():
    #take picture
    save_path = "./img/"
    main_name = datetime.now().strftime("%Y%m%d_%H%M%S")#201712_xxxxx
    rand_char = str(random.randint(1,1000))               
    file_ext  = ".jpg" 
    pic_name  =  main_name + rand_char + file_ext       #201712_xxxxx0.jpg
    pic_loc   = save_path + pic_name                    #./static/img/201712_xxxxx0.jpg
    #camera.resolution = (1024,768) 
    #camera.capture(pic_loc)

    #print picture
    for x in range(1,4):
        sound1.play()
        #time.sleep(1)

    #sound2.play()	
    #common.pic_print(pic_loc)
    
    return pic_loc

#TODO:localhost setting
run(host='localhost', port=8080, debug=True)