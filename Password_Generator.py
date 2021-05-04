import random
import time
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller() #Keyboard go brrrr

count = 0 #This makes it loop since it was easier that way

print("Get ready in 5 seconds")
time.sleep(5) #Just gets u ready


guess_password = ""
while count < 5:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuwxyz1234567890" 
    guess_password = ''.join(random.choice(letters) for i in range(random.randint(8,20)))
    print(list(guess_password))
    keyboard.press(Key.enter)
    keyboard.type(guess_password)
    keyboard.press(Key.enter)
    time.sleep(1)