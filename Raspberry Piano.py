import subprocess
from threading import Thread
from rstem.button import Button

def c:
    play = Thread(target = subprocess.call, args = ([["aplay", "C.wav"]]))
    play.start()
    
def d:
    play = Thread(target = subprocess.call, args = ([["aplay", "D.wav"]]))
    play.start()
    
def e:
    play = Thread(target = subprocess.call, args = ([["aplay", "E.wav"]]))
    play.start()
    
def f
    play = Thread(target = subprocess.call, args = ([["aplay", "F.wav"]]))
    play.start()
    
def g:
    play = Thread(target = subprocess.call, args = ([["aplay", "G.wav"]]))
    play.start()

def a:
    play = Thread(target = subprocess.call, args = ([["aplay", "A.wav"]]))
    play.start()

def b:
    play = Thread(target = subprocess.call, args = ([["aplay", "B.wav"]]))
    play.start()

buttons = {c: Button(8), d: Button(0) e: Button(3), f: Button(13) g: Button(30), a: Button(23), b: Button(25)}

while True:
    for key, val in buttons.items():
        if val.presses():
            key()
