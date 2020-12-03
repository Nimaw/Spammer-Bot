from pynput.keyboard import Key,Controller
import keyboard  as key2 
import time

    

message = "http://zihdir.ir/"
count  = -1
keyboard = Controller()

time.sleep(5)


while True:
    if key2.is_pressed('q'):   
            print('You have stopped process!')
            break  
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
        count += 1
        print (count)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
