# import pyautogui
# import time
# from unicodedata import name
import tkinter as tk

# def screenshot():
#     time.sleep(5)
#     name = time.time()
#     name = "path{}.png".format()
#     img = pyautogui.screenshot()
#     img.save(name)
#     img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,text='Take Screenshot')
button.pack(side=tk.LEFT)

close = tk.Button(frame,text='Close',command=quit)
close.pack(side=tk.LEFT)

root.mainloop()



