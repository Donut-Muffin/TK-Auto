import tkinter
from tkinter import *
import pyautogui
import time
import keyboard
Click=False
window = tkinter.Tk()
window.title("AutoClicker")
window.geometry("600x600")
def stop():
    global Click
    Click=False
    autoclickButton.configure(bg="gray")
    pyautogui.alert("AutoClicker has stopped")
def autoclick():
    autoclickButton.configure(bg="yellow")
    global Click
    Click=True
    try:
        msDelay = int(msDelayEntry.get())
        secondDelay = int(secondDelayEntry.get())
    except:
        pyautogui.alert("Please enter a valid number")
        return
    time.sleep(2.5)
    button=str(stringvarButton.get()).lower()
    delay=msDelay/1000+secondDelay
    autoclickButton.configure(bg="red")
    if repeatUntilStoppedVar.get()==1:
        if repeatVar.get()==1:
            pyautogui.alert("Please select only one option")
            autoclickButton.configure(bg="gray")
            return
    if repeatUntilStoppedVar.get()==0:
        if repeatVar.get()==0:
            pyautogui.alert("Please select an option")
            autoclickButton.configure(bg="gray")
            return
    if repeatVar.get()==1:
        for x in range(int(repeatTimes.get())):
            pyautogui.click(button=button)
            time.sleep(delay)
            timesToGo.configure(text=f"{x} clicks to go")
            if keyboard.is_pressed("f2"):
                Click=False
                pyautogui.alert("AutoClicker has stopped")
                autoclickButton.configure(bg="gray")
                return
        else:
            autoclickButton.configure(bg="grey")
            return
    elif repeatUntilStoppedVar.get()==1:
        while Click==True:
            pyautogui.click(button=button)
            time.sleep(delay)
            if keyboard.is_pressed("f2"):
                Click=False
                pyautogui.alert("AutoClicker has stopped")
                autoclickButton.configure(bg="gray")
                return
    else:
        pyautogui.alert("Please select a valid option")
        autoclickButton.configure(bg="gray")
        return
Delays = LabelFrame(window, width = 450, height = 45, pady=5, padx=5, text="Delays")
Delays.pack()
msDelayEntry = tkinter.Entry(Delays)
msDelayEntry.grid(row=1, column=0, padx=5, pady=5)
msDelayEntry.insert(0, "25")
secondDelayEntry = tkinter.Entry(Delays)
secondDelayEntry.grid(row=1, column=1, padx=5, pady=5)
secondDelayEntry.insert(0, "0")
label = tkinter.Label(Delays, text="Delay (ms):")
label.grid(row=0, column=0, padx=5, pady=5)
label = tkinter.Label(Delays, text="Delay (sec):")
label.grid(row=0, column=1, padx=5, pady=5)
Controls = LabelFrame(window, width = 450, height = 45, pady=5, padx=5, text="Delays")
Controls.pack()
stopButton = tkinter.Button(Controls, text="Stop (F2)", command=lambda : stop())
stopButton.grid(row=0,column=0, padx=5, pady=5)
autoclickButton = tkinter.Button(Controls, text="Start", command=autoclick)
autoclickButton.grid(row=0,column=1, padx=5, pady=5)
stringvarButton = tkinter.StringVar(Controls)
stringvarButton.set("Left")
buttonMenu = tkinter.OptionMenu(Controls, stringvarButton, "Left", "Right", "Middle")
buttonMenu.grid(row=0, column=2, padx=5, pady=5)
Repeats = LabelFrame(window, width = 450, height = 45, pady=5, padx=5, text="Repeats")
Repeats.pack()
timesToGo = tkinter.Label(Repeats, text="Clicks times to go")
timesToGo.grid(row=5, column=0, padx=5, pady=5)
window.wm_attributes("-topmost", 1)
repeatUntilStoppedVar=IntVar()
repeatVar=IntVar()
repeat = tkinter.Checkbutton(Repeats, text="Repeat (times):", variable=repeatVar)
repeat.grid(row=0, column=0, padx=5, pady=5, sticky="w")
repeatUntilStopped = tkinter.Checkbutton(Repeats, text="Repeat until stopped", variable=repeatUntilStoppedVar)
repeatUntilStopped.grid(row=1, column=0, padx=5, pady=5, sticky="w")
repeatTimes = tkinter.Entry(Repeats)
repeatTimes.grid(row=0, column=1, padx=5, pady=5)
repeatTimes.insert(0, "0")
window.resizable(0,0)
window.mainloop()