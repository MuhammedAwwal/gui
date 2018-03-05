from tkinter import *
from tkinter import StringVar, ttk, Tk
import os

creds = 'tempfile.temp'

def signup ():

    global pwordE
    global nameE
    global roots

    roots = Tk()
    roots.title ('signup')
    introduction = Label (roots, text = 'Please Enter new Credentials\n')
    introduction.grid (row = 0, column = 0, sticky = E)

    nameL = Label(roots, text= 'New UserNmae')
    pwordL = Label(roots, text = 'New Password')
    nameL.grid(row = 1, column = 0 , sticky = W)
    pwordL.grid(row=2, column=0, sticky=W)

    nameE = Entry (roots)
    nameE = Entry (roots, show = '*')
    nameE.grid (row = 1, column = 1)
    pwordE.grid(row=1, column=1)

    signupButton = Button(roots, text = 'signup', command = FSSignup)
    signupButton.grid (columnspan = 2, sticky = W)
    roots.mainloop ()


def FSSignup ():
    with open(creds, 'w') as f:
        f.write(nameE.get ())
        f.write('\n')
        f.write(pwordE.get ())
        f.close()


    roots.destroy()
    Login ()


def Login ():

    global nameEL
    global pwordEL

    rootA = Tk()
    rootA.title ('Login')

    instruction = Label (rootA, text = 'Please Login\n')
    instruction.grid(sticky = E)

    nameL = Label (rootA, text = 'Username: ')
    pwordL = Label(rootA, text='password: ')
    nameL.grid (row = 1, sticky = E)
    pwordL.grid(row=2, sticky=E)

    nameEL = Entry(rootA)
    pwordEL =  Entry (rootA, show='*')
    nameEL.grid (row = 1, column = 1)
    pwordEL.grid(row=2, column=1)

    loginB = Button (rootA, text = 'Login', command = CheckLogin)
    loginB.grid (columnspan = 2, sticky = W)

    rmuser = Button (rootA, text = 'Delete User', fg = 'red', command = DelUser)
    rmuser.grid (columnspan = 2, sticky = W)
    rootA.mainloop()


def CheckLogin ():
    with open(creds) as f:
        data = f.readline()
        uname = data [0].rstrip()
        pword = data [0].rstrip()

    if NameEl.get () == uname and pwordEL == pword:
        r = Tk ()
        r.title(':D')
        r.geometry ('150x50')
        rlbl = Label (r, text ='\n[+] Looged In ')
        rlbl.pack ()
        r.mainloop()

    else:
        r = Tk ()
        r.title (' :D')
        r.geometry ('150x50')
        rlbl = Label (r, text = '\n[!] Invalid Login')
        rlbl.pack ()
        r.mainloop()
def DelUser ():
    os.remove(creds)
    rootA.destroy()
    signup()


if os.path.isfile(creds):
        Login()



























