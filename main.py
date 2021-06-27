import os
import I2C_driver
# from pynput.keyboard import Key, Listener
mylcd = I2C_driver.lcd()

AUDIO_URL = './assets/audio/'

task_1 = ['woord 1?', 'task-2', 'story-1']
task_2 = ['woord 2?', 'task-3', 'story-2']
task_3 = ['woord 3?', 'task-4', 'story-3']
task_4 = ['woord 4?', '', 'story-4']

repeat = True
keylogger = []

# def listToString(s): 
#     str1 = "" 
#     for ele in s: 
#         str1 += ele  
#     return str1 

# def on_press(key):
#     key = str(key).replace("'", "")
#     if key == Key.enter:
#         keylogger.clear()
#     elif key == Key.backspace:
#         if keylogger:
#             keylogger.pop()
#     else:
#         keylogger.append(key)

def PlaySound(sound):
    os.system(f'omxplayer {AUDIO_URL}{sound}.mp3')

def awnserLoop(tasks, currectAwnser):
    question = False
    while question == False:
        # TODO display lcd tasks question
        mylcd.lcd_clear()
        mylcd.lcd_display_string(tasks[0], 1)
        awnser = input(tasks[0])
        if (awnser != currectAwnser):
            PlaySound('try-again')
        else:
            if tasks[1] == '':
                mylcd.lcd_display_string('goed gedaan', 1)
                print('goed gedaan')
                PlaySound[2]
                mylcd.lcd_display_string('Press Enter to start again', 1)
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