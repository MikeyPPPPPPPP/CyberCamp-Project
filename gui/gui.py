from tkinter import *  # Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import *
import gui_helper
import subprocess
import os
import threading
import sys
import random


class Example(Frame):
    def __init__(self):
        super().__init__()
        self.wordgen = []
        self.alphabets = 'abcdefghijklmnopqrstuvwxyz'
        self.a = sys.argv
        self.threads = []
        self.up = []
        self.ips = '10.15.143.'#128.'
        self.helper = gui_helper.vincipher()
        self.helper2 = gui_helper.rail2()
        self.helper3 = gui_helper.rail2()
        self.helper4 = gui_helper.rail2()
        self.helper5 = gui_helper.rail2()
        self.helper6 = gui_helper.rail2()
        self.helper7 = gui_helper.rail2()
        self.helper8 = gui_helper.rail2()
        self.helper9 = gui_helper.rail2()
        self.var = StringVar()
        self.numoftrys = 3
        self.newMessage = ""
        self.master.title("Michael - Login")
        self.pack(fill=BOTH, expand=True)
        self.frame50 = Frame(self)
        self.frame50.pack(fill=BOTH)
        self.labellog = Label(self.frame50, text='Username:', width=16)
        self.labellog.pack(side=LEFT, padx=5, pady=5)
        self.entry50 = Entry(self.frame50)
        self.entry50.pack(fill=X, padx=5, expand=True)
        self.frame51 = Frame(self)
        self.frame51.pack(fill=BOTH)
        self.labelpas = Label(self.frame51, text='Password:', width=16)
        self.labelpas.pack(side=LEFT, padx=5, pady=5)

        self.entry51 = Entry(self.frame51, show="*")

        self.entry51.bind('<Return>', self.bruteforce)#self.loginForm)

        self.entry51.pack(fill=X, padx=5, expand=True)
        self.frame52 = Frame(self)
        self.frame52.pack(fill=BOTH)
        self.lbl42 = Label(self.frame52, text="number of trys:")
        self.lbl42.pack(side=LEFT, anchor=N, padx=5, pady=5)
        self.labeltrys = Label(self.frame52, textvariable=self.var, width=16)#labelText
        self.labeltrys.pack(side=LEFT, padx=5, pady=5)
        self.var.set(str(self.numoftrys))

    def bruteforce(self, event):
        try:
            u = str(self.a[1])
            p = str(self.a[2])

            self.loginForm(u, p)
        except:
            u = str(self.entry50.get())
            p = str(self.entry51.get())

            self.loginForm(u, p)

    def loginForm(self, unam, pas): #(self, event)
        """
        try:
            self.a[1], self.a[2] = self.username, self.password
        except:
            self.username = str(self.entry50.get())
            self.password = str(self.entry51.get())
        """
        self.username = unam
        self.password = pas
        varaf = 0
        pasvar = 0
        #self.username = str(self.entry50.get())
        #self.password = str(self.entry51.get())
        if self.numoftrys == 1:
            if self.username == 'test' and self.password == 'test':
                self.mainmenu()
            elif self.username == 'god' and self.password == 'god':
                self.mainmenu()
            elif self.username == 'test' and self.password != 'test':
                self.numoftrys -= 1
                self.var.set(str(self.numoftrys))
                self.destroy()
                #self.wrong()
            elif self.username != 'test' and self.password == 'test':
                self.numoftrys -= 1
                self.var.set(str(self.numoftrys))
                self.destroy()
                #self.wrong()
            else:
                self.numoftrys -= 1
                self.var.set(str(self.numoftrys))
                self.destroy()
        elif self.numoftrys == 2:
            self.wrong()
            if self.username == 'test' and self.password == 'test':
                self.mainmenu()
            elif self.username == 'god' and self.password == 'god':
                self.mainmenu()
            elif self.username == 'test' and self.password != 'test':
                self.numoftrys -= 1
                self.var.set(str(self.numoftrys))
                #self.wrong()
            elif self.username != 'test' and self.password == 'test':
                self.numoftrys -= 1
                self.var.set(str(self.numoftrys))
                #self.wrong()
            else:
                self.numoftrys -= 1
                self.var.set(str(self.numoftrys))
                self.var.set(str(self.numoftrys))
        else:
            if self.username == 'test' and self.password == 'test':
                self.mainmenu()
            elif self.username == 'god' and self.password == 'god':
                self.mainmenu()
            elif self.username == 'test' and self.password != 'test':
                self.numoftrys -= 1
                self.var.set(str(self.numoftrys))
                #self.wrong()
            elif self.username != 'test' and self.password == 'test':
                self.numoftrys -= 1
                self.var.set(str(self.numoftrys))
                #self.wrong()
            else:
                self.numoftrys -= 1
                self.var.set(str(self.numoftrys))
                #self.wrong()

    def wrong(self):
        tops = Toplevel(self)
        tops.title("About this application...")
        tops.geometry("200x100")
        msg = Message(tops, text='Hint: test')
        msg.pack()
        button = Button(tops, text="Dismiss" , command=tops.destroy)
        button.pack()

    def icmp_ping(self):
        h = 1
        s = 45
        for i in range(4):
            self.t = threading.Thread(target=self.worker2, args=(h, s, ))
            self.threads.append(self.t)
            self.t.start()
            h += 45
            s += 45

    def fastping(self):
        h = 1
        s = 9
        for i in range(45):
            self.t = threading.Thread(target=self.worker, args=(h, s, ))
            self.threads.append(self.t)
            self.t.start()
            h += 9
            s += 9
        for x in self.up:
            print(x)

    def connect_serv(self):
        h = 1
        s = 45
        for i in range(4):
            self.t = threading.Thread(target=self.worker, args=(h, s,))
            self.threads.append(self.t)
            self.t.start()
            h += 45
            s += 45

    def worker(self, x, y):
        #self.ips ='10.15.128.'
        """thread worker function"""
        for x in range(x, y):
            response = os.system("ping -l 1 " + self.ips + str(x))  # icmp "ping -c 5 " + self.ips + str(x))

            # and then check the response...
            if response == 0:
                a = self.ips + str(x)
                self.lisbox2gets.insert(0, a + ' is up!')
                self.up.append(a)
            else:
                pass
        return

    def worker3(self, x, y):
        #self.ips ='10.15.128.'
        """thread worker function"""
        for x in range(x, y):
            response = os.system("ping -6 -l 1 " + self.ips + str(x))  # icmp "ping -c 5 " + self.ips + str(x))

            # and then check the response...
            if response == 0:
                a = self.ips + str(x)
                self.lisbox2gets.insert(0, a + ' is up!')
                self.up.append(a)
            else:
                pass
        return

    def worker2(self, x, y):
        #self.ips ='10.15.128.'
        """thread worker function"""
        for x in range(x, y):
            response = os.system("ping -4 -l 1 " + self.ips + str(x))

            # and then check the response...
            if response == 0:
                a = self.ips + str(x)
                self.lisbox2gets.insert(0, a + ' is up!')
                self.up.append(a)
            else:
                pass
        return

    def the_rail(self):
        """
        message = str(self.entryrail.get())
        evod = self.helper2.evensimsg(message)
        helpers = self.helper3.the_rail_help2(message, evod)
        self.lisbox2get.insert(0, helpers)#str1)
        """
        message = str(self.entryrail.get())
        get_rows = int(self.entry2.get())
        if get_rows == 2:
            evod = self.helper2.two_rails(message)
            helpers = self.helper3.the_rail_help1(message, evod)
            self.lisbox2get.insert(0, helpers)  # str1)
        elif get_rows == 3:
            evod = self.helper2.evensimsg(message)
            helpers = self.helper3.the_rail_help2(message, evod)
            self.lisbox2get.insert(0, helpers)  # str1)
        elif get_rows == 4:
            evod = self.helper6.the_rail_4(message)
            helpers = self.helper7.the_rail_help3(message, evod)
            self.lisbox2get.insert(0, helpers)  # str1)
        elif get_rows == 5:
            evod = self.helper8.the_rail_5(message)
            helpers = self.helper3.the_rail_help4(message, evod)
            self.lisbox2get.insert(0, helpers)  # str1)
        else:
            self.lisbox2get.insert(0, str("Enter row 2, 3, 4, 5"))

    def vendef(self):
        ventop = Toplevel(self)
        ventop.geometry("350x200")
        ventop.title("Vigenere Cipher")
        self.ven = Frame(ventop)
        self.ven.pack(fill=BOTH)
        self.venc = Label(self.ven, text="Message: ", width=16)
        self.venc.pack(side=LEFT, pady=5)
        self.entryven = Entry(self.ven)
        self.entryven.pack(fill=X, expand=True)
        self.ven2 = Frame(ventop)
        self.ven2.pack(fill=BOTH)
        self.venc2 = Label(self.ven2, text="Key len^>: ", width=16)
        self.venc2.pack(side=LEFT, pady=5)
        self.entryven2 = Entry(self.ven2)
        self.entryven2.pack(fill=X, expand=True)
        self.frame2ven = Frame(ventop)
        self.frame2ven.pack(fill=BOTH)
        self.lbl42 = Button(self.frame2ven, text="Vigenere",command=self.get_inputs4vc)  # self.mainmenu
        self.lbl42.pack(side=LEFT, anchor=N, padx=5, pady=5)
        self.lisboxmad123 = Listbox(self.frame2ven)
        self.lisboxmad123.pack(fill=BOTH, pady=5, padx=5, expand=True)

    def new_key(self):
        self.newk = Toplevel(self)
        self.labelck = Label(self.newk, text="Pick a different keyword")
        self.labelck.pack()

    def random_word(self, length):
        try:
            self.wordgen.remove(self.wordgen[0])
        except:
            pass
        s = random.randint(0, 25)
        rannum = None
        for x in range(0, int(length)):
            for y in range(0, s):
                s = random.randint(0, 25)
            self.wordgen.append(self.alphabets[s])

    def get_inputs4vc(self):

        self.string = self.entryven.get().upper()

        #print(self.string)
        self.random_word(len(self.string))
        self.keyword = ''.join(self.wordgen).upper()#self.entryven2.get()
        self.check_key = open("keys.txt","+r")
        chckkey = self.check_key.read()
        if self.keyword in chckkey:
                self.new_key()


        else:
            self.check_key.write(str("\n"+self.keyword))
            self.check_key.close()


            self.key = self.helper.generateKey(self.string, self.keyword)
            self.cipher_text = self.helper.cipherText(self.string, self.key)
            self.org = self.helper.originalText(self.cipher_text, self.key)
            self.lisboxmad123.insert(0, "Ciphertext :" + self.cipher_text)
            self.lisboxmad123.insert(1, "Original/Decrypted Text :" + self.helper.originalText(self.cipher_text, self.key))
            #self.lisboxmad123.insert(2, "Random Keyword: " + str(''.join(self.key)))


    def shiftcipher(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        partialOne = ""
        partialTwo = ""
        newAlphabet = ""
        message = str(self.entry1.get())
        key = int(self.entry2.get())
        if key == 0:
            newAlphabt = alphabet
        elif key > 0:
            partialOne = alphabet[:key]
            partialTwo = alphabet[key:]
            newAlphabet = partialTwo + partialOne

        else:
            partialOne = alphabet[:(26 + key)]
            partialTwo = alphabet[(26 + key):]
            newAlphabet = partialTwo + partialOne
        myMessage = message
        for i in range(0, len(myMessage)):
            index = alphabet.find(myMessage[i])
            if index < 0:
                self.newMessage += myMessage[i]
                # print(newMessage)
            else:
                self.newMessage += newAlphabet[index]
        for k in range(len(alphabet)):
            newAlphabet = alphabet[k:] + alphabet[:k]
            attempt = ""
            for i in range(len(myMessage)):
                index = alphabet.find(myMessage[i])
                if index < 0:
                    attempt += myMessage[i]
                else:
                    attempt += newAlphabet[index]
            if k == key:
                self.lisbox.insert(0, "Key: " + str(k) + " - " + attempt)  # print("Key: " + str(k) + " - " + attempt)
            else:
                pass

    def shiftcipher2(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        partialOne = ""
        partialTwo = ""
        newAlphabet = ""
        message = str(self.entry1.get())
        key = 26 - int(self.entry2.get())
        if key == 0:
            newAlphabt = alphabet
        elif key > 0:
            partialOne = alphabet[:key]
            partialTwo = alphabet[key:]

            newAlphabet = partialTwo + partialOne
        else:
            partialOne = alphabet[:(26 + key)]
            partialTwo = alphabet[(26 + key):]
            newAlphabet = partialTwo + partialOne
        myMessage = message
        for i in range(0, len(myMessage)):
            index = alphabet.find(myMessage[i])
            if index < 0:
                self.newMessage += myMessage[i]
                # print(newMessage)
            else:
                self.newMessage += newAlphabet[index]
        for k in range(len(alphabet)):
            newAlphabet = alphabet[k:] + alphabet[:k]
            attempt = ""
            for i in range(len(myMessage)):
                index = alphabet.find(myMessage[i])
                if index < 0:
                    attempt += myMessage[i]
                else:
                    attempt += newAlphabet[index]
            if k == 0:
                self.lisbox2.insert(0, "Key: " + str(
                    k) + " - " + attempt)  # print("Key: " + str(k) + " - " + attempt)
            else:
                pass

    def shift_test(self):###################################shift cipher tab
        top = Toplevel(self)
        top.title("Shift Cipher")
        top.geometry("350x350")
        self.master.title("Michael")
        self.pack(fill=BOTH, expand=True)
        self.frame1 = Frame(top)
        self.frame1.pack(fill=X)
        self.lbl1 = Label(self.frame1, text="shift cipher", width=16)
        self.lbl1.pack(side=LEFT, padx=5, pady=5)
        self.entry1 = Entry(self.frame1)
        self.entry1.pack(fill=X, padx=5, expand=True)
        self.frame2 = Frame(top)
        self.frame2.pack(fill=X)
        self.lbl2 = Label(self.frame2, text="num of shifts", width=16)
        self.lbl2.pack(side=LEFT, padx=5, pady=5)
        self.entry2 = Entry(self.frame2)
        self.entry2.pack(fill=X, padx=5, expand=True)
        self.frame3 = Frame(top)
        self.frame3.pack(fill=BOTH, expand=True)
        self.lbl3 = Button(self.frame3, text="Encrypt", command=self.shiftcipher)  # , command=shiftcipher)
        self.lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)
        self.lisbox = Listbox(self.frame3)
        self.lisbox.pack(fill=BOTH, pady=5, padx=5, expand=True)
        self.frame52 = Frame(top)
        self.frame52.pack(fill=BOTH)
        self.lbl42 = Button(self.frame52, text="Decrypt", command=self.shiftcipher2)  # shiftcipher2)  # , command=shiftcipher)
        self.lbl42.pack(side=LEFT, anchor=N, padx=5, pady=5)
        self.lisbox2 = Listbox(self.frame52)
        self.lisbox2.pack(fill=BOTH, pady=5, padx=5, expand=True)

    def railfencetab(self):##########################################railfence gui part
        rai = Toplevel(self)
        rai.title("3 Rail:Rail Fence")
        rai.geometry("350x200")
        self.frameget = Frame(rai)
        self.frameget.pack(fill=BOTH)
        self.labeltext = Label(self.frameget, text="Enter a text:")
        self.labeltext.pack(side=LEFT, padx=5, pady=5)
        self.entryrail = Entry(self.frameget)
        self.entryrail.pack(fill=X, padx=5, expand=True)

        self.Frame2 = Frame(rai)
        self.Frame2.pack(fill=BOTH)

        self.label2 = Label(self.Frame2, text="Rows: ", width=16)
        self.label2.pack(side=LEFT, padx=5, pady=5)

        self.entry2 = Entry(self.Frame2)
        self.entry2.pack(fill=X, padx=5, expand=True)

        self.frame2get = Frame(rai)
        self.frame2get.pack(fill=BOTH)
        self.lbl42 = Button(self.frame2get, text="Encode", command=self.the_rail)  # self.mainmenu
        self.lbl42.pack(side=LEFT, anchor=N, padx=5, pady=5)
        self.lisbox2get = Listbox(self.frame2get)
        self.lisbox2get.pack(fill=BOTH, pady=5, padx=5, expand=True)

    def the_libs(self):
        madtop = Toplevel(self)
        madtop.title("madlib")
        madtop.geometry("350x650")
        self.framestory = Frame(madtop)
        self.framestory.pack(fill=BOTH, expand=True)
        self.lbl3 = Button(self.framestory, text="Story", width=12, command=self.madlib_story1)#genrats the story   Button
        self.lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)
        self.lisboxmad1 = Listbox(self.framestory)
        self.lisboxmad1.pack(fill=BOTH, pady=5, padx=5, expand=True)
        self.master.title("Michael - Login")
        self.pack(fill=BOTH, expand=True)
        self.framemad = Frame(madtop)
        self.framemad.pack(fill=BOTH)
        self.lbl42 = Label(self.framemad, text="Adja1", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entryadja1 = Entry(self.framemad)
        self.entryadja1.pack(fill=X, expand=True)
        self.frame2mad = Frame(madtop)
        self.frame2mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame2mad, text="Adja2", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entryadja2 = Entry(self.frame2mad)
        self.entryadja2.pack(fill=X, expand=True)
        self.frame3mad = Frame(madtop)
        self.frame3mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame3mad, text="body part1", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entrybody1 = Entry(self.frame3mad)
        self.entrybody1.pack(fill=X, expand=True)
        self.frame4mad = Frame(madtop)
        self.frame4mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame4mad, text="body part2", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entrybody2 = Entry(self.frame4mad)
        self.entrybody2.pack(fill=X, expand=True)
        self.frame5mad = Frame(madtop)
        self.frame5mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame5mad, text="body part3", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entrybody3 = Entry(self.frame5mad)
        self.entrybody3.pack(fill=X, expand=True)
        self.frame7mad = Frame(madtop)
        self.frame7mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame7mad, text="number", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entrynum = Entry(self.frame7mad)
        self.entrynum.pack(fill=X, expand=True)
        self.frame8mad = Frame(madtop)
        self.frame8mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame8mad, text="color", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entrycolor = Entry(self.frame8mad)
        self.entrycolor.pack(fill=X, expand=True)
        self.frame9mad = Frame(madtop)
        self.frame9mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame9mad, text="varb1", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entryverb1 = Entry(self.frame9mad)
        self.entryverb1.pack(fill=X, expand=True)
        self.frame10mad = Frame(madtop)
        self.frame10mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame10mad, text="varb2", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entryverb2 = Entry(self.frame10mad)
        self.entryverb2.pack(fill=X, expand=True)
        self.frame11mad = Frame(madtop)
        self.frame11mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame11mad, text="varb3", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entryverb3 = Entry(self.frame11mad)
        self.entryverb3.pack(fill=X, expand=True)
        self.frame12mad = Frame(madtop)
        self.frame12mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame12mad, text="varb4", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entryverb4 = Entry(self.frame12mad)
        self.entryverb4.pack(fill=X, expand=True)
        self.frame13mad = Frame(madtop)
        self.frame13mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame13mad, text="noun1", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entrynoun1 = Entry(self.frame13mad)
        self.entrynoun1.pack(fill=X, expand=True)
        self.frame14mad = Frame(madtop)
        self.frame14mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame14mad, text="noun2", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entrynoun2 = Entry(self.frame14mad)
        self.entrynoun2.pack(fill=X, expand=True)
        self.frame15mad = Frame(madtop)
        self.frame15mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame15mad, text="plurl noun1", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entrypnoun1 = Entry(self.frame15mad)
        self.entrypnoun1.pack(fill=X, expand=True)
        self.frame16mad = Frame(madtop)
        self.frame16mad.pack(fill=BOTH)
        self.lbl42 = Label(self.frame16mad, text="plurl noun2", width=16)
        self.lbl42.pack(side=LEFT, pady=5)
        self.entrypnoun2 = Entry(self.frame16mad)
        self.entrypnoun2.pack(fill=X, expand=True)

    def madlib_story1(self):
        self.body11 = self.entrybody1.get()
        self.body12 = self.entrybody2.get()
        self.body13 = self.entrybody3.get()
        self.num1 = self.entrynum.get()
        self.adj11 = self.entryadja1.get()
        self.adj12 = self.entryadja2.get()
        self.color1 = self.entrycolor.get()
        self.verb11 = self.entryverb1.get()
        self.verb12 = self.entryverb2.get()
        self.verb13 = self.entryverb3.get()
        self.verb14 = self.entryverb4.get()
        self.noun11 = self.entrynoun1.get()
        self.noun12 = self.entrynoun2.get()
        self.pnoun11 = self.entrypnoun1.get()
        self.pnoun12 = self.entrypnoun2.get()
        self.lisboxmad1.insert(0, str('He holds out his ' + self.body11 + ', and in his ' + self.body12 + ' are' + self.num1))
        self.lisboxmad1.insert(1, str(self.adj11 + self.color1 + self.pnoun11 + ' linked with a thick black thread ...'))
        self.lisboxmad1.insert(2, str('Inside me! ! ' + self.verb12 + ' and all the, ' + self.pnoun12 + ' deep in my'))
        self.lisboxmad1.insert(3, str(self.body12 + ' clench. My inner' + self.noun11 + ' is doing the ' + self.verb13))
        self.lisboxmad1.insert(4, str('of the seven veils'))
        self.lisboxmad1.insert(5, str("It's" + self.adj12 + "feeling. Once they're inside me, I'"))
        self.lisboxmad1.insert(6, str("can't really " + self.verb11 + ' them-but then again I know'))
        self.lisboxmad1.insert(7, str("they're,I may have to " + self.verb13 + ' these. They'))
        self.lisboxmad1.insert(8, str('make me needy, needy for ' + self.noun12 + '.'))

    def vendef(self):
        ventop = Toplevel(self)
        ventop.geometry("350x200")
        ventop.title("Vigenere Cipher")
        self.ven = Frame(ventop)
        self.ven.pack(fill=BOTH)
        self.venc = Label(self.ven, text="Message: ", width=16)
        self.venc.pack(side=LEFT, pady=5)
        self.entryven = Entry(self.ven)
        self.entryven.pack(fill=X, expand=True)
        self.ven2 = Frame(ventop)
        self.ven2.pack(fill=BOTH)
        self.venc2 = Label(self.ven2, text="Key: ", width=16)
        self.venc2.pack(side=LEFT, pady=5)
        self.entryven2 = Entry(self.ven2)
        self.entryven2.pack(fill=X, expand=True)
        self.frame2ven = Frame(ventop)
        self.frame2ven.pack(fill=BOTH)
        self.lbl42 = Button(self.frame2ven, text="Vigenere",command=self.get_inputs4vc)  # self.mainmenu
        self.lbl42.pack(side=LEFT, anchor=N, padx=5, pady=5)
        self.lisboxmad123 = Listbox(self.frame2ven)
        self.lisboxmad123.pack(fill=BOTH, pady=5, padx=5, expand=True)


    def testsub(self):
        a = str(self.command.get())
        #self.suboutput.insert(0, subprocess.run(a))
        self.testproc = subprocess.run(a, stderr=subprocess.PIPE)
        #self.suboutput.insert(0, str(self.testproc))

    def stegB1(self):
        b1s = Toplevel(self)
        self.framesss = Frame(b1s)
        self.framesss.pack(fill=BOTH, expand=True)
        self.image = PhotoImage(file="example - Copy.png")  # myfile.gif")
        self.labelss = Label(self.framesss, image=self.image)
        self.labelss.pack()

    def stegB2(self):
        b2s = Toplevel(self)
        self.framessss = Frame(b2s)
        self.framessss.pack(fill=BOTH, expand=True)
        self.image = PhotoImage(file="example - Copy - Copy.png")  # myfile.gif")
        self.labelss = Label(self.framessss, image=self.image)
        self.labelss.pack()

    def stegB3(self):
        b3s = Toplevel(self)
        self.framesssss = Frame(b3s)
        self.framesssss.pack(fill=BOTH, expand=True)
        self.image = PhotoImage(file="example.png")  # myfile.gif")
        self.labelss = Label(self.framesssss, image=self.image)
        self.labelss.pack()

    def ping_scan(self):
        PingS = Toplevel(self)
        PingS.title("Michael - pingscan")
        PingS.geometry("350x200")
        self.topFrames = Frame(PingS)
        self.topFrames.pack(fill=BOTH)
        self.labelones = Label(self.topFrames, text="EX:10.15.128.1/24 :", width=16)
        self.labelones.pack(side=LEFT, padx=5, pady=5)

        self.icmps = Button(self.topFrames, text="IPV4", command=self.icmp_ping)
        self.icmps.pack(side=LEFT, padx=5, pady=5)
        # self.entryword = Entry(self.topFrame)

        # self.entryword.pack(fill=X, padx=5, expand=True)

        self.normals = Button(self.topFrames, text="IPV6", command=self.connect_serv)
        self.normals.pack(side=LEFT, padx=5, pady=5)

        self.frame2gets = Frame(PingS)
        self.frame2gets.pack(fill=BOTH)
        self.lbl42s = Button(self.frame2gets, text="!!PING!!", command=self.fastping)  # self.mainmenu
        self.lbl42s.pack(side=LEFT, anchor=N, padx=5, pady=5)
        self.lisbox2gets = Listbox(self.frame2gets)
        self.lisbox2gets.pack(fill=BOTH, pady=5, padx=5, expand=True)



    def stegMenu(self):
        steg = Toplevel(self)
        steg.title("Steganography")
        steg.geometry("200x100")

        self.topFrame = Frame(steg)
        self.topFrame.pack(fill=BOTH, expand=True)
        self.labss = Label(self.topFrame, text="Can you see the changes?")
        self.labss.pack(side=LEFT)

        self.frame4b1 = Frame(steg)
        self.frame4b1.pack(fill=BOTH, expand=True)
        self.button1 = Button(self.frame4b1, text="Normal Image", command=self.stegB1)
        self.button1.pack(fill=BOTH, expand=True)

        self.frame4b2 = Frame(steg)
        self.frame4b2.pack(fill=BOTH, expand=True)
        self.button2 = Button(self.frame4b1, text="New Image", command=self.stegB2)
        self.button2.pack(fill=BOTH, expand=True)

        self.frame4b3 = Frame(steg)
        self.frame4b3.pack(fill=BOTH, expand=True)
        self.button3 = Button(self.frame4b3, text="Image", command=self.stegB3)
        self.button3.pack(fill=BOTH, expand=True)
    def mainmenu(self):           ################################################main menu
        men = Toplevel(self)
        men.title("Menu")
        men.geometry("300x200")
        self.mainmenuf = Frame(men)
        self.mainmenuf.pack(fill=BOTH, expand=True)
        self.lbl42 = Button(self.mainmenuf, text="shift cipher", command=self.shift_test)
        self.lbl42.pack(side=LEFT, padx=5, pady=5)
        self.lbl42 = Button(self.mainmenuf, text="rail cipher", command=self.railfencetab)
        self.lbl42.pack(side=LEFT, padx=5, pady=5)
        self.lbl42 = Button(self.mainmenuf, text="Vigenere Cipher", command=self.vendef)
        self.lbl42.pack(side=LEFT, padx=5, pady=5)
        self.mainmenumad = Frame(men)
        self.mainmenumad.pack(fill=BOTH, expand=True)
        self.lbl42 = Button(self.mainmenumad, text="madlibs 1", command=self.the_libs)
        self.lbl42.pack(side=LEFT, padx=5, pady=5)

        #add madlibs story 1 and 3
        self.lbl421 = Button(self.mainmenumad, text="madlibs 2", command=self.the_libs)
        self.lbl421.pack(side=LEFT, padx=5, pady=5)
        self.lbl422 = Button(self.mainmenumad, text="madlibs 3", command=self.the_libs)
        self.lbl422.pack(side=LEFT, padx=5, pady=5)

        self.sub = Frame(men)
        self.sub.pack(fill=BOTH, expand=True)

        self.thirdButton = Button(self.sub, text="Steganography", command=self.stegMenu)
        self.thirdButton.pack(side=LEFT, padx=5, pady=5)    #fill=BOTH, expand=True)

        self.fourthButton = Button(self.sub, text="nothing related", command=self.ping_scan)
        self.fourthButton.pack(side=LEFT, padx=5, pady=5)
        """
        self.subprocess_button = Button(self.sub, text="command:", command=self.testsub)
        self.subprocess_button.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.command = Entry(self.sub)
        self.command.pack(fill=X, expand=True)


        self.subout = Frame(men)
        self.subout.pack(fill=BOTH, expand=True)

        self.suboutput = Listbox(self.subout)
        self.suboutput.pack(fill=BOTH, pady=5, padx=5, expand=True)
        """
def main():
    root = Tk()
    root.geometry("200x100")
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    main()