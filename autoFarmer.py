import pyautogui 
import time
import pydirectinput
import threading

control = False
def on_press(key):
    global control
    # Regular alphanumeric keys (a-z, 0-9)
    try:
        print(f"Key pressed: {key.char}")
        if(key.char == "l"):
            print(pyautogui.position())
        if(key.char == "i"):
           control = True
           threading.Thread(target=testMove, daemon=True).start()
        if(key.char == "r"):
           control = False
    
    except AttributeError:
    
        
        pass


def on_release(key):
  
  if key == keyboard.Key.esc:
    print("Stopping keyboard listener...")
    return False


def testMove():
    global control
    

    pydirectinput.moveRel(75, 0, relative=True)
    time.sleep(0.5)
    if control == False:
       return
    pydirectinput.click(button='left')
    time.sleep(0.5)
    if control == False:
           return
    while control == True or counter < 100:
        print("hey")
        print(counter)
        pydirectinput.moveRel(-150, 0, relative=True)
        time.sleep(0.5)
        if control == False:
            return
        pydirectinput.click(button='left')
        time.sleep(0.5)
        if control == False:
            return
        pydirectinput.moveRel(150, 0, relative=True)
        time.sleep(0.5)
        if control == False:
            return
        pydirectinput.click(button='left')
        time.sleep(0.5)
        if control == False:
            return
        counter += 1
        
        
        


    

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()
