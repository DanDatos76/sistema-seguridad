import cv2
import numpy as np
import  pygame
import simpleaudio as sa
import time
import datetime
import requests

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)


import telebot

bot = telebot.TeleBot("xxxxxxxxxxxxxxxxxxxxxxxxxxxx") # You can set parse_mode by default. HTML or MARKDOWN
i = 0
while True:
  ret, frame = video.read()
  if ret == False: break
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  if i == 20:
    bgGray = gray
  if i > 20:
    dif = cv2.absdiff(gray, bgGray)
    _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
    # Para OpenCV 3
    #_, cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Para OpenCV 4
    cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, cnts, -1, (0,0,255),2)        
    
    for c in cnts:
      area = cv2.contourArea(c)
      if area > 9000:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
        fecha = time.strftime("%Y%m%d-%H%M%S")

        cv2.imwrite(fecha + ".jpg", frame)
        wave_obj = sa.WaveObject.from_wave_file('alarm.wav')
        play_obj = wave_obj.play()
        play_obj.wait_done()
        cv2.imwrite(fecha + ".jpg", frame)
        cv2.imwrite(fecha + ".jpg", frame)
        cv2.imwrite(fecha + ".jpg", frame)
        alarma = cv2.imwrite("alarma"+fecha + ".jpg", frame)
        

        @bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
          bot.reply_to(message, "Howdy, how are you doing?")
        #requests.post('https://api.telegram.org/bot<TOKEN>/sendPhoto',
              #data={'chat_id': <CHAT_ID>, 'photo':alarma, 'caption': <TEXT>})

  cv2.imshow('Frame',frame)

  i = i+1
  if cv2.waitKey(30) & 0xFF == ord ('q'):
    break
video.release()


#5035305575:AAF0CZbYK-pOETL1mGU0x8TX1U4TEaT4R0Q
