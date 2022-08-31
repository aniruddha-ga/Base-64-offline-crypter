from tkinter import *
import base64
global namevalue
root = Tk()

def getPath(filename):
    import os
    import sys
    from os import chdir
    from os.path import join
    from os.path import dirname
    from os import environ
    
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller >= 1.6
        chdir(sys._MEIPASS)
        filename = join(sys._MEIPASS, filename)
    elif '_MEIPASS2' in environ:
        # PyInstaller < 1.6 (tested on 1.5 only)
        chdir(environ['_MEIPASS2'])
        filename = join(environ['_MEIPASS2'], filename)
    else:
        chdir(dirname(sys.argv[0]))
        filename = join(dirname(sys.argv[0]), filename)
        
    return filename

def encoder():
    stringname= namevalue.get()
    Utf_encode_first = stringname.encode('utf-8','strict')
    stringvalue = base64.b64encode(Utf_encode_first)
    stringvalue = stringvalue.decode()
    if(len(stringvalue) != 0):
        namevalue.set(stringvalue)
    else:
        namevalue.set("Enter the String")
    
def decoder():
    stringname= namevalue.get()
    stringvalue = base64.b64decode(stringname)
    stringvalue = stringvalue.decode()
    if(len(stringvalue) != 0):
        namevalue.set(stringvalue)
    else:
        namevalue.set("Enter the String")
    
root.geometry("1100x434")
root.title("B64 Crypter")
root.configure(background="black")
root.minsize(400,300)
root.maxsize(3000,1600)
root.iconbitmap(getPath("encrypt.ico"))
Label(root, text="Base64 Crypter", font="comicsansms 60 bold",bg="black",fg="white", pady=15).pack()
Label(root, text="Enter The Text", font="comicsansms 40 bold",bg="black",fg="white", pady=15).pack()
namevalue = StringVar()
nameentry = Entry(root, textvariable=namevalue,font="lucida 40 bold")
nameentry.pack()

frame = Frame(root, borderwidth=6, bg="white",pady=6,padx=6, relief=SUNKEN)
frame.pack()
b1 = Button(frame, fg="green", text="crypt", command=encoder, font="lucida 35 bold")
b1.pack(side=LEFT, padx=15)
b2 = Button(frame, fg="red", text="decrypt", command=decoder, font="lucida 35 bold")
b2.pack(padx=15)
nameentry.update()
Label(root, text=namevalue)
root.mainloop()
