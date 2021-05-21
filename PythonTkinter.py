from tkinter import *

from tkinter import scrolledtext

list_ = ["Т-26","БТ-7","Т-70","Т-28","КВ-1","КВ-2","Т-34","Т-34-85","ИС-2"]
foto_list=["t26.gif","bt7.gif","t70.gif","t28.gif","kv1.gif","kv2.gif","t34_1941.gif","t34_85.gif","is2.gif"]
 

def list_to_txt(event):
    txt.delete(0.0,END)
    valik=lbox.curselection()
    txt.insert(END,lbox.get(valik[0]))


def description():
    global photo
    desc.delete(1.0, END)
    show.config(text=lbox.get(ANCHOR))
    if lbox.get(ANCHOR)=="Т-26":
        t=open("t26.txt", encoding="utf-8-sig")
        f=t.read()
        desc.insert(INSERT,f)
        t.close()
        photo = PhotoImage(file="t26.gif")
        can.create_image(0, 0, anchor='nw',image=photo)
    elif lbox.get(ANCHOR)=="БТ-7":
        t=open("bt7.txt", encoding="utf-8-sig")
        f=t.read()
        desc.insert(INSERT,f)
        t.close()
        photo = PhotoImage(file="bt7.gif")
        can.create_image(0, 0, anchor='nw',image=photo)
    elif lbox.get(ANCHOR)=="Т-70":
        t=open("t70.txt", encoding="utf-8-sig")
        f=t.read()
        desc.insert(INSERT,f)
        t.close()
        photo = PhotoImage(file="t70.gif")
        can.create_image(0, 0, anchor='nw',image=photo)
    elif lbox.get(ANCHOR)=="Т-28":
        t=open("t28.txt", encoding="utf-8-sig")
        f=t.read()
        desc.insert(INSERT,f)
        t.close()
        photo = PhotoImage(file="t28.gif")
        can.create_image(0, 0, anchor='nw',image=photo)
    elif lbox.get(ANCHOR)=="КВ-1":
        t=open("kv1.txt", encoding="utf-8-sig")
        f=t.read()
        desc.insert(INSERT,f)
        t.close()
        photo = PhotoImage(file="kv1.gif")
        can.create_image(0, 0, anchor='nw',image=photo)
    elif lbox.get(ANCHOR)=="КВ-2":
        t=open("kv2.txt", encoding="utf-8-sig")
        f=t.read()
        desc.insert(INSERT,f)
        t.close()
        photo = PhotoImage(file="kv2.gif")
        can.create_image(0, 0, anchor='nw',image=photo)
    elif lbox.get(ANCHOR)=="Т-34":
        t=open("t34_1941.txt", encoding="utf-8-sig")
        f=t.read()
        desc.insert(INSERT,f)
        t.close()
        photo = PhotoImage(file="t34_1941.gif")
        can.create_image(0, 0, anchor='nw',image=photo)
    elif lbox.get(ANCHOR)=="Т-34-85":
        t=open("t34_85.txt", encoding="utf-8-sig")
        f=t.read()
        desc.insert(INSERT,f)
        t.close()
        photo = PhotoImage(file="t34_85.gif")
        can.create_image(0, 0, anchor='nw',image=photo)
    elif lbox.get(ANCHOR)=="ИС-2":
        t=open("is2.txt", encoding="utf-8-sig")
        f=t.read()
        desc.insert(INSERT,f)
        t.close()
        photo = PhotoImage(file="is2.gif")
        can.create_image(0, 0, anchor='nw',image=photo)

aken=Tk()
aken.title("Самые знаменитые танки времён ВОВ")
aken.resizable(width=False,height=False)
aken.iconbitmap('b_icon_warthunder.ico')
lbox=Listbox(aken,width=10,height=9,selectmode=SINGLE)
lbox.insert(0, "Т-26")
lbox.insert(1, "БТ-7")
lbox.insert(2, "Т-70")
lbox.insert(3, "Т-28")
lbox.insert(4, "КВ-1")
lbox.insert(5, "КВ-2")
lbox.insert(6, "Т-34")
lbox.insert(7, "Т-34-85")
lbox.insert(8, "ИС-2")


lbox.grid(row=0,column=0,sticky="w")
lbox.bind("<<ListboxSelect>>",list_to_txt)

txt=Text(aken,height=1,width=20,wrap=WORD)
txt.grid(row=0,column=2)

bt=Button(text='Информация', command=description).grid(row=1,column=0)

desc=scrolledtext.ScrolledText(aken, width=86, height=10, borderwidth=5)
desc.grid(row=3,column=3)

can = Canvas(aken)
can.grid(row=0, column=3)

show = Label(aken)

aken.mainloop()