from pynput import keyboard
from pynput.keyboard import Key, Listener



COMBINATIONS = [
    
    {Key.shift, keyboard.KeyCode(char='a')},
    {Key.shift, keyboard.KeyCode(char='A')}
]

myText = keyboard.Controller()

current = set()

def execute():
    myText.press(Key.backspace)
    myText.release(Key.backspace)
    for char in "This is a Hotkey":
        myText.press(char)
    myText.press(Key.space)
    myText.release(Key.space)
    

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]) and not key in current:
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)
        
    if key == Key.esc:
        # Stop listener
        return False

with keyboard.Listener(
            on_press=on_press, 
            on_release=on_release) as listener:
    listener.join()


        #cd PyQTWork\pyFiles
        #[myText.press(x) for x in 'hello']