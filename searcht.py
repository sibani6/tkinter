from tkinter import *
import wikipedia

def getme():
  ev=entry.get()
  av=wikipedia.summary(ev)
  answer.insert(INSERT,av)



root=Tk()

topframe=Frame(root)
entry=Entry(topframe)
entry.pack()

b=Button(topframe,text="search",command=getme)
b.pack()

topframe.pack(side=TOP)

bottomframe=Frame(root)

scroll=Scrollbar(bottomframe)
scroll.pack(side=RIGHT,fill=Y)

answer=Text(bottomframe,width=30,height=15,yscrollcommand=scroll.set)
scroll.config(command=answer.yview)
answer.pack()

bottomframe.pack()





root.mainloop()
