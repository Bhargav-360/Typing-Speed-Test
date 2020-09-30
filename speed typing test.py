from tkinter import *
from tkinter.messagebox import *
from time import *
import random

sentence = ["The air between them was as calm and peaceful as it was raging around them.","Excuse me, could you tell me the way to the station, please?" , "I went out in the sun. Then, all of a sudden, it started to rain" ,"She's been out of work for years. How can she make ends meet with four children?" , "Andrew had an accident while playing ice-hockey. Little by little he begins to walk","Sorry, I can't go out with you. I'm up to my ears in work.","The Mahabharata is the longest epic poem known and has been described as the longest poem ever written."]
j = 0

def submit():
    global j
    j = 0
    if j<len(sentence):
        sen = sentence[j]
    wpm = 0
    c = 0
    total_time = 0
    time_start = 0
    time_stop = int(time())
    total_time = time_stop - time_start
    text = ent.get()
    w1 = text.split(" ")
    wpm = len(w1)

    
    for i in range(0,len(text)):
        if sen[i] == text[i]:
            c += 1

    acc = int((c/len(sen))*100)
    showinfo("Progress","1.TIME : "+str(total_time*0.001) +" milisecs\n"+"2.Words : "+str(wpm) +"\n"+"3.Accuracy : "+str(acc) +"%\n")


def reset():
    global j
    j += 1
    if j<len(sentence):
        ent.delete(0,END)
        text.set(sentence[j])
    else:
        showwarning("Complete!","You are done!,If you want to join again please restart the application")

    
root = Tk()
root.title("SPEED TYPING TEST")
root.geometry("1200x600+50+100")
root.configure(background = "Black")

text = StringVar()
text.set(sentence[0])

lbl = Label(root,text = "TYPING SPEED TEST", font=('Bold Italic' , 40 ,'bold'),fg = "yellow",bg = "black")

lbl_sen = Label(root, font=('Bold Italic' , 18 ,'bold'),fg = "orange",bg = "black",textvariable = text)
ent = Entry(root ,font=('Bold Italic' , 18 ,'bold'), width = 70)
sub_btn = Button(root , text = "SUBMIT" , font=('Bold Italic' , 18 ,'bold'),width =10,command = submit)
res_btn = Button(root , text = "RESET" , font=('Bold Italic' , 18 ,'bold'),width = 10,command = reset)

lbl.pack(pady = 90)
lbl_sen.pack(pady = 20)
ent.pack(pady = 50,padx = 20)
sub_btn.pack(pady = 20)
res_btn.pack()

root.mainloop()
