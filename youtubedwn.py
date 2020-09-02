from tkinter import *

from pytube import YouTube

from tkinter import messagebox as mb

window=Tk()
window.title("YTD")

window.minsize(width=300,height=300)

photo=PhotoImage(file="D:\Python Programs\ytd.png")
window.iconphoto(False,photo)

img=PhotoImage(file=r"D:\Python Programs\yt.png",width=300,height=200)
Button(window,image=img).grid(row=1,column=0)

l=Label(window,text="YouTube Downloader").grid(row=0,column=0)

e=Entry(window,bd=10,width=25)
e.grid(row=2,column=0)



def dow():
    win=Tk()
    win.title("Select")
    
    win.minsize(width=300,height=50)
    
    ff=Frame(win)
    ff.pack()
    
    fff=Frame(win)
    fff.pack()

    l1=Label(fff,text="Enter Location")
    l1.pack(side=LEFT)

    e1=Entry(fff,bd=10,width=25)
    e1.pack(side=TOP)


    scroll=Scrollbar(ff,orient=VERTICAL)
    select=Listbox(ff,yscrollcommand=scroll.set,width=50,height=6)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT,fill=Y)
    select.pack(side=LEFT,fill=BOTH,expand=1)



    
    global e
    string=e.get()
    yt=YouTube(str(string))
    videos=yt.streams.order_by('resolution')
    s=1
    
    for v in videos:
        c=(str(s)+'.'+str(v))
        select.insert(END,c)
        s +=1
    
    
    
    def which_selected():
        print("at{0}".format(select.curselection()))
        n=int(select.curselection()[0])
        vid=videos[n-1]
        
        u=e1.get()
        destination=str(u)
        vid.download(destination)
        
        mb.showinfo('Success',"Video Downloaded")

    

    bb=Button(fff,text="Download",bg="red",fg="white",padx=10,command=which_selected)
    bb.pack(side=BOTTOM)



    
b=Button(window,text="Download",bg="red",fg="white",padx=10,command=dow)
b.grid(row=3,column=0)

window.mainloop()
