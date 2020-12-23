#!/usr/bin/env python
# coding: utf-8

# In[22]:


from tkinter import *
import base64
global namevalue
root = Tk()
def encoder():
    stringname= namevalue.get()
    Utf_encode_first = stringname.encode('utf-8','strict')
    stringvalue = base64.b64encode(Utf_encode_first)
    print(stringvalue)
    namevalue.set(stringvalue)
    
def decoder():
    stringname= namevalue.get()
    stringvalue = base64.b64decode(stringname)
    print(stringvalue)
    namevalue.set(stringvalue)
    
root.geometry("1100x434")
root.title("B64 Encoder and Decoder")
root.wm_iconbitmap("C:/Users/user/Desktop/Python/encrypt.ico")
root.configure(background="black")
root.minsize(400,300)
root.maxsize(3000,1600)
Label(root, text="Base64 Encode and Decode", font="comicsansms 60 bold",bg="black",fg="white", pady=15).pack()
Label(root, text="Enter The Text", font="comicsansms 40 bold",bg="black",fg="white", pady=15).pack()
namevalue = StringVar()
nameentry = Entry(root, textvariable=namevalue,font="lucida 40 bold")
nameentry.pack()

frame = Frame(root, borderwidth=6, bg="white",pady=6,padx=6, relief=SUNKEN)
frame.pack()
b1 = Button(frame, fg="green", text="encode", command=encoder, font="lucida 35 bold")
b1.pack(side=LEFT, padx=15)
b2 = Button(frame, fg="red", text="decode", command=decoder, font="lucida 35 bold")
b2.pack(padx=15)
nameentry.update()
Label(root, text=namevalue)
root.mainloop()

