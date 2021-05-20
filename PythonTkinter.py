from tkinter import *

list_ = ["Т-26","БТ-7","Т-70","Т-28","КВ-1","КВ-2","Т-34","Т-34-85","ИС-2"]
foto_list=["t26.gif","bt7.gif","t70.gif","t28.gif","kv1.gif","kv2.gif","t34_1941.gif","t34_85.gif","is2.gif"]
global can, pc
def list_to_txt(event):
    global can,pc#
    txt.delete(0.0,END)
    valik=lbox.curselection()
    txt.insert(END,lbox.get(valik[0]))
    can.delete(ALL)#
    foto=PhotoImage(file=foto_list[valik[0]])#
    can.create_image(0,0,image=foto,anchor=NW)#
def txt_to_list(event):
    text=txt.get(0.0,END)
    text=text[-2:-1]
    if text=="\n":
        pass
    else:
        list_.append(text)
        print(list_)
        lbox.config(height=len(list_))
        lbox.insert(END,text)   
        txt.delete(0.0,END)

def description():
    text=txt.get(0.0,END)
    print(list(text))
    if text=="t26.gif\n":
        t26=open("t26.txt", encoding="utf-8-sig")
    elif text=="bt7.gif\n":
        bt7=open("bt7.txt", encoding="utf-8-sig")
    elif text=="t70.gif\n":
        t70=open("t70.txt", encoding="utf-8-sig")
    elif text=="t28.gif\n":
        t28=open("t28.txt", encoding="utf-8-sig")
    elif text=="kv1.gif\n":
        kv1=open("kv1.txt", encoding="utf-8-sig")
    elif text=="kv2.gif\n":
        kv2=open("kv2.txt", encoding="utf-8-sig")
    elif text=="t34_1941.gif\n":
        t34_1941=open("t34_1941.txt", encoding="utf-8-sig")
    elif text=="t34_85.gif\n":
        t34_85=open("t34_85.txt", encoding="utf-8-sig")
    elif text=="is2.gif\n":
        is2=open("is2.txt", encoding="utf-8-sig")

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
txt.bind("<Return>",txt_to_list)
pc=PhotoImage(file="")
panel = Label(aken,image=pc)
panel.grid(row=2,column=3,)
bt=Button(text='Информация', command=description).grid(row=1,column=0)
desc=Label(aken, text="Описание", width=40, height=40)
desc.grid(row=3,column=3)
aken.mainloop()