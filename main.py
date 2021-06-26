import os
from playsound import playsound
import I2C_driver

import pygame

mylcd = I2C_driver.lcd()

AUDIO_URL = './assets/audio/'

task_1 = ['woord 1?', 'task-2', 'story-1']
task_2 = ['woord 2?', 'task-3', 'story-2']
task_3 = ['woord 3?', 'task-4', 'story-3']
task_4 = ['woord 4?', '', 'story-4']

repeat = True

def PlaySound(sound):
    # playsound(f'{AUDIO_URL}{sound}.mp3')
    pygame.mixer.music.load(f'{AUDIO_URL}{sound}.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    print('hello')

def typing(input)

def awnserLoop(tasks, currectAwnser):
    question = False
    while question == False:
        # TODO display lcd tasks question
        mylcd.lcd_display_string(tasks[0], 1)
        awnser = input(tasks[0])
        n = eval(input("Enter price: "))
        mylcd.lcd_display_string(awnser, 2)

        if (awnser != currectAwnser):
            PlaySound('try-again')
        else:
            if tasks[1] == '':
                # TODO display lcd goed gedaan
                mylcd.lcd_display_string('goed gedaan', 1)

                print('goed gedaan')
                PlaySound[2]
                # TODO display lcd goed gedaan
                input('Press Enter to start again')
            else:
                PlaySound(tasks[2])
                PlaySound(tasks[1])
            question = True

while repeat:
    awnserLoop(task_1, 'selma')
    awnserLoop(task_2, 'verzet')
    awnserLoop(task_3, 'envelop')
    awnserLoop(task_4, 'verraad')
