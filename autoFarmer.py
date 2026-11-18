import pyautogui 
from pynput import keyboard
import time
import pydirectinput
import threading
import minescript
from java import JavaClass

control = False
def on_press(key):
    global control
    # Regular alphanumeric keys (a-z, 0-9)
    try:
        #print(f"Key pressed: {key.char}")
        if(key.char == "l"):
            #print(pyautogui.position())
            testEat()
            #pass
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

def testEat():
    Minecraft = JavaClass("net.minecraft.client.Minecraft")
    mc = Minecraft.getInstance()
    if mc.player:
        food_data = mc.player.getFoodData()
        hunger = food_data.getFoodLevel()
        saturation = food_data.getSaturationLevel()
        minescript.echo(f"Hunger{hunger} Saturation:{saturation}")

def testMove():
    global control
    Minecraft = JavaClass("net.minecraft.client.Minecraft")
    mc = Minecraft.getInstance()
    foodTarg = "minecraft:cooked_beef"
    

    pydirectinput.moveRel(75, 0, relative=True)
    time.sleep(0.5)
    if control == False:
       return
    pydirectinput.click(button='left')
    time.sleep(0.5)
    if control == False:
           return
    while control == True:
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
        if mc.player:
            food_data = mc.player.getFoodData()
            hunger = food_data.getFoodLevel()
            saturation = food_data.getSaturationLevel()
            if(hunger < 12):
                while(hunger < 20):
                    hunger = food_data.getFoodLevel()
                    #eat food here
                    foodSlot = None
                    for stack in minescript.player_inventory():
                        if stack.item == foodTarg and 0<= stack.slot <=8:
                            foodSlot = stack.slot
                    if foodSlot != None:
                        previousSlot = minescript.player_inventory_select_slot(foodSlot)
                        minescript.player_press_use(True)
                        time.sleep(1.8)
                        minescript.player_press_use(False)
                        minescript.player_inventory_select_slot(previousSlot)
                        if(hunger == 20):
                            break
                    else:
                        print("out of food, don't wanna die")
                        exit()
                    if control == False:
                        return
                        
            #minescript.echo(f"Hunger{hunger} Saturation:{saturation}")
        
        
        
        


    

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()
