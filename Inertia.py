from pynput import keyboard
from pynput.keyboard import Controller
bot = Controller()

from os import listdir

import argon2

from string import printable
printable = printable.strip()
from random import choice

bit = False
password = []
stream = []
salt = ""

def hash(i, salt):
    return argon2.low_level.hash_secret(i.encode(), salt.encode(), time_cost = 1, memory_cost = 512, parallelism=2, hash_len=20, type=argon2.low_level.Type.D).decode()[-20:]

def saltGen():
    return ''.join(choice(printable) for i in range(20))

if "my.salt" in listdir():
    fob = open("my.salt", "r")
    salt = fob.read()
    fob.close()
else:
    salt = saltGen()
    fob = open("my.salt", "a")
    fob.write(salt)
    fob.close()

def on_press(k):
    global bit, password, stream, salt
    
    try:
        if k.char in printable:
            stream.append(k.char)
            while len(stream) > 2:
                stream.pop(0)
            if bit:
                password.append(stream[1])
    except:
        pass
    
    if k == keyboard.Key.backspace:
        if bit:
            try:
                password.pop()
            except:
                password = []
        else:
            try:
                stream.pop()
            except:
                stream = []
        
    if "".join(stream) == "@/":
        if bit:
            stream = []
            b = "\b" * len(password) + "\b\b"
            bot.type(b + hash("".join(password[:-2]), salt))
        bit = not bit
        password = []
        
    try:
        print(k.char)
    except:
        print("UNKNOWN")
    print(bit)
    print(password)
    print(stream)
    print("--------")
    
listener = keyboard.Listener(on_press=on_press)
listener.start()

input()
