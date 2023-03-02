import pyautogui as t
from time import sleep

sleep(5)
i=158
while(i):
    i += 1
    t.write("ha ha ha")
    t.typewrite(""+str(i))
    t.press("Enter")
