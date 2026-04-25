import wikipedia
from tkinter import *

# enter_topic = input("Enter the topic to search:\n")
# try:
#     options = wikipedia.search(enter_topic)
#     result = wikipedia.summary(enter_topic)
#     print(f"{options}\n: {result}")
# except wikipedia.exceptions.DisambiguationError as e:
#     print(e.options)
def on_press():
    q = get_q.get()
    text.insert(INSERT,wikipedia.summary(q))
    

root = Tk()
root.title("WIKI search")
question = Label(root,text='question')
question.pack()
get_q = Entry(root,bd=5)
get_q.pack()
submit = Button(root,text='Search',command=on_press)
submit.pack()
text = Text(root)

root.mainloop()