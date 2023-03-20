from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get())
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.title("Calculator")
root.iconbitmap("calculator.ico")

scvalue = StringVar()
screen = Entry(root, textvariable=scvalue, font="lucida 32 bold", width=8)
screen.pack(fill=X, padx=8)

f = Frame(root)
b = Button(f, text="7", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="8", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="9", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
b = Button(f, text="4", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="5", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="6", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
b = Button(f, text="1", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="2", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="3", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
b = Button(f, text="0", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="-", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="*", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
b = Button(f, text="/", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="+", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="=", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
b = Button(f, text="C", font="Helvetica 16 bold", bg="orange", width=3)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()