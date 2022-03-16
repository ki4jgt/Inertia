from pynput import keyboard
from pynput.keyboard import Controller
bot = Controller()

from os import listdir

from argon2 import PasswordHasher

from string import printable
printable = printable.strip()
from random import choice

bit = False
password = []
stream = []
salt = ""

def hash(i):
    return PasswordHasher().hash(i)[-20:]

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

def on_press(key):
    global bit, password, stream, salt, now
    
    try:
        if key.char in printable:
            stream.append(key.char)
            while len(stream) > 2:
                stream.pop(0)
            if bit:
                password.append(stream[1])
    except:
        pass
    
    if "".join(stream) == "@/":
        if bit:
            stream = []
            b = "\b" * len(password) + "\b\b"
            bot.type(b + hash("".join(password[:-2]) + salt))
        bit = not bit
        password = []
        
    try:
        print(key.char)
    except:
        print("UNKNOWN")
    print(bit)
    print(password)
    print(stream)
    print("--------")
    
listener = keyboard.Listener(on_press=on_press)
listener.start()

input()
