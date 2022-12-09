from tkinter import *

def click(event):
 global scvalue
 text=event.widget.cget("text")
 if text=="=":
  if scvalue.get().isdigit():
    value=int(scvalue.get())
  else:
    try:
     value=eval(screen.get())
    except Exception as e:
     print(e)
     value="Error"
  scvalue.set(value)
  screen.update()
 
 elif text=="C":
  scvalue.set("")
  screen.update()
 else:
  scvalue.set(scvalue.get()+text)
root= Tk()
root.geometry("1000x1200")
root.title("Calculator by Sahil Kumar")
#root.wm_iconbitmap("1.ico")


scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f=Frame(root,bg="grey")
b=Button(f,text="9",padx=28,pady=22,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=28,pady=22,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=28,pady=22,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="6",padx=28,pady=22,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=28,pady=22,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=28,pady=22,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="3",padx=28,pady=22,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=28,pady=22,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=28,pady=22,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="0",padx=30,pady=22,font="lucida 36 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=30,pady=22,font="lucida 36 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=30,pady=22,font="lucida 36 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="+",padx=28,pady=30,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=16)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=28,pady=30,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=16)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=28,pady=30
,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=16)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="C",padx=28,pady=30,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="%",padx=28,pady=30,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text=".",padx=28,pady=30,font="lucida 36 bold")
b.pack(side=LEFT,padx=16,pady=12)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()





