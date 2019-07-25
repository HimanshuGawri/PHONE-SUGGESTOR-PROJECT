
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import database_functionality

password = 'Himanshu'

class detail_page():

    def __init__(self,master):
        self.master = master
        self.canvas = Canvas(self.master, width=200, height=200, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # ====================================== functions ===================================================#
        def datacollect():

            self.camq= str(self.c1.get()) + str(self.c2.get()) + str(self.c3.get()) + str(self.c4.get())
            self.proq= str(self.p1.get()) + str(self.p2.get()) + str(self.p3.get()) + str(self.p4.get())
            self.batq= str(self.b1.get()) + str(self.b2.get()) + str(self.b3.get()) + str(self.b4.get())
            self.stoq = str(self.s1.get()) + str(self.s2.get()) + str(self.s3.get()) + str(self.s4.get())
            self.disq= str(self.d1.get()) + str(self.d2.get()) + str(self.d3.get()) + str(self.d4.get())
            self.ramq = str(self.r1.get()) + str(self.r2.get()) + str(self.r3.get()) + str(self.r4.get())
            self.cat = str(self.o1.get()) + str(self.o2.get()) + str(self.o3.get()) + str(self.o4.get()) + str(self.o5.get())
            self.name = self.name_in.get()
            self.mod = self.model_in.get()
            self.amt = self.price_in.get()
            self.cam = self.camera_in.get()
            self.pro = self.processor_in.get()
            self.bat = self.battery_in.get()
            self.sto = self.storage_in.get()
            self.dis = self.display_in.get()
            self.ram = self.ram_in.get()
            self.os = self.os_in.get()
            self.co = self.colors_in.get()
            self.rat = self.rating_in.get()
            self.pu1 = self.purchase_in_1.get()
            self.pu2 = self.purchase_in_2.get()

            self.result = database_functionality.add_phone(self.name,self.mod,self.amt,self.camq,self.proq,self.batq,self.stoq,self.disq,
                                                           self.ramq,self.cat,self.cam,self.ram,self.pro,self.bat,self.dis,self.sto,self.os,
                                                           self.co,self.rat,self.pu1,self.pu2)
            if (self.result == 'p'):
                messagebox.showinfo("Great !!!","Phone Added Successfully!")
            else:
                messagebox.showinfo("Uh-oh", "Wrong input(s)")


        self.header = Label(self.canvas,text = "Please Fill The following Details ",bg="lavender", relief="solid", width=32, font=("arial", 20))
        self.header.place(x=10, y=15)

        self.msg1 = Label(self.canvas, text="*All Fields are required.",bg="white",fg="red",font=("arial", 12))
        self.msg1.place(x=10, y=57)

        self.myfind = ImageTk.PhotoImage(file=r"find.png")
        self.find = Label(self.canvas, compound=TOP, image=self.myfind, width=125, height=150, bg="white")
        self.find.image = self.myfind
        self.find.place(x=655,y=75)


        self.name_tag = Label(self.canvas, text="Brand Name  : ", bg='white', font=("arial", 15, "bold"))
        self.name_tag.place(x=10, y=100)
        self.name_in = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.name_in.place(x=175, y=100)

        self.model_tag = Label(self.canvas, text="Model            : ", bg='white', font=("arial", 15, "bold"))
        self.model_tag.place(x=10, y=150)
        self.model_in = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.model_in.place(x=175, y=150)

        self.price_tag = Label(self.canvas, text="Price(₹)         : ", bg='white', font=("arial", 15, "bold"))
        self.price_tag.place(x=10, y=200)
        self.price_in = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.price_in.place(x=175, y=200)

        self.msg2 = Label(self.canvas, text="*Please check only one checkbox for each Column, except Categories Column.", bg='white', fg="red",
                          font=("arial", 11))
        self.msg2.place(x=10, y=515)

        self.specification = Label(self.canvas, text="Specifications :",bg = "white",width=12, font=("antaro", 24,"bold"))
        self.specification.place(x=10, y=535)


        self.camera_tag = Label(self.canvas, text="Camera(in MP)  :", bg='white', font=("arial", 15, "bold"))
        self.camera_tag.place(x=10, y=595)
        self.camera_in = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.camera_in.place(x=190, y=595)

        self.ram_tag = Label(self.canvas, text="RAM (in GB)      :", bg='white', font=("arial", 15, "bold"))
        self.ram_tag.place(x=10, y=645)
        self.ram_in = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.ram_in.place(x=190, y=645)

        self.processor_tag = Label(self.canvas, text="Processor         :", bg='white', font=("arial", 15, "bold"))
        self.processor_tag.place(x=10, y=695)
        self.processor_in = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.processor_in.place(x=190, y=695)

        self.battery_tag = Label(self.canvas, text="Battery(in mAh) :", bg='white', font=("arial", 15, "bold"))
        self.battery_tag.place(x=10, y=745)
        self.battery_in = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.battery_in.place(x=190, y=745)

        self.display_tag = Label(self.canvas, text="Display      :", bg='white', font=("arial", 15, "bold"))
        self.display_tag.place(x=550, y=595)
        self.display_in = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.display_in.place(x=680, y=595)

        self.storage_tag = Label(self.canvas, text="Storage     :", bg='white', font=("arial", 15, "bold"))
        self.storage_tag.place(x=550, y=645)
        self.storage_in = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.storage_in.place(x=680, y=645)

        self.os_tag = Label(self.canvas, text="OS             :", bg='white', font=("arial", 15, "bold"))
        self.os_tag.place(x=550, y=695)
        self.os_in = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.os_in.place(x=680, y=695)

        self.colors_tag = Label(self.canvas, text="Colors       :", bg='white', font=("arial", 15, "bold"))
        self.colors_tag.place(x=550, y=745)
        self.colors_in = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.colors_in.place(x=680, y=745)

        self.purchase_tag = Label(self.canvas, text="Purchase Link(s) :", bg='white', font=("arial", 20, "bold"))
        self.purchase_tag.place(x=1028, y=80)

        self.msg3 = Label(self.canvas, text="*Please Enter  'NIL'  if there is no purchase link:",bg='white',fg="red",font=("arial",11))
        self.msg3.place(x=1028, y=121)

        self.purchase_in_1 = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.purchase_in_1.place(x=1025, y=151)
        self.purchase_in_2 = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.purchase_in_2.place(x=1025, y=200)

        self.mybuy = ImageTk.PhotoImage(file=r"weblink.png")
        self.buy = Label(self.canvas, compound=TOP, image=self.mybuy, width=125,height=125, bg="white")
        self.buy.image = self.mybuy
        self.buy.place(x=1340, y=115)

        self.rating_tag = Label(self.canvas, text="     Rating       :", bg='white', font=("arial", 15, "bold"))
        self.rating_tag.place(x=1025, y=595)
        self.rating_in = Entry(self.canvas, bg='azure', relief="sunken", width=20, font=("arial", 20))
        self.rating_in.place(x=1175, y=595)


        self.button = Button(self.canvas, text="ADD", fg='WHITE', bg='lawngreen', relief="solid", width=8,height=1,font=("arial", 22, "bold"),command = datacollect)
        self.button.place(x=1200, y=685)

#=====================================CAMERA WITH CHECKBOX=========================================#

        self.mycamera = ImageTk.PhotoImage(file=r"mycamera.png")
        self.camera = Label(self.canvas, text="Camera\n Quality", compound=TOP, image=self.mycamera, width=54,height=74, bg="white")
        self.camera.image = self.mycamera
        self.camera.place(x=100, y=300)

        self.c1 = IntVar()
        self.C1 = Checkbutton(self.canvas, text="Excellent",bg="white",onvalue=1, offvalue=0,variable = self.c1)
        self.C1.place(x=87,y=405)

        self.c2 = IntVar()
        self.C2 = Checkbutton(self.canvas, text="Very Good", bg="white", onvalue=1, offvalue=0,variable = self.c2)
        self.C2.place(x=87, y=430)

        self.c3 = IntVar()
        self.C3 = Checkbutton(self.canvas, text="Good", bg="white", onvalue=1, offvalue=0,variable = self.c3)
        self.C3.place(x=87, y=455)

        self.c4 = IntVar()
        self.C4 = Checkbutton(self.canvas, text="Average", bg="white", onvalue=1, offvalue=0,variable = self.c4)
        self.C4.place(x=87, y=480)

#====================================================CHIP WITH CHECKBOX=================================================================#

        self.mychip = ImageTk.PhotoImage(file=r"mychip.png")
        self.chip = Label(self.canvas, text="Processor/\nchipset", compound=TOP, image=self.mychip, width=56, height=72,bg="white")
        self.chip.image = self.mychip
        self.chip.place(x=300, y=300)


        self.p1 = IntVar()
        self.P1 = Checkbutton(self.canvas, text="Excellent", bg="white", onvalue=1, offvalue=0,variable = self.p1)
        self.P1.place(x=287, y=405)

        self.p2 = IntVar()
        self.P2 = Checkbutton(self.canvas, text="Very Good", bg="white", onvalue=1, offvalue=0,variable = self.p2)
        self.P2.place(x=287, y=430)

        self.p3 = IntVar()
        self.P3 = Checkbutton(self.canvas, text="Good", bg="white", onvalue=1, offvalue=0,variable = self.p3)
        self.P3.place(x=287, y=455)

        self.p4 = IntVar()
        self.P4 = Checkbutton(self.canvas, text="Average", bg="white", onvalue=1, offvalue=0,variable = self.p4)
        self.P4.place(x=287, y=480)

#======================================================BATTERY WITH CHECK BOX===========================================================#

        self.mybattery = ImageTk.PhotoImage(file=r"mybattery.png")
        self.battery = Label(self.canvas, text="Battery\n Performance", compound=TOP, image=self.mybattery, width=66,height=74, bg="white")
        self.battery.image = self.mybattery
        self.battery.place(x=500, y=300)

        self.b1 = IntVar()
        self.B1 = Checkbutton(self.canvas, text="Excellent", bg="white", onvalue=1, offvalue=0,variable = self.b1)
        self.B1.place(x=487, y=405)

        self.b2 = IntVar()
        self.B2 = Checkbutton(self.canvas, text="Very Good", bg="white", onvalue=1, offvalue=0,variable = self.b2)
        self.B2.place(x=487, y=430)

        self.b3 = IntVar()
        self.B3 = Checkbutton(self.canvas, text="Good", bg="white", onvalue=1, offvalue=0,variable = self.b3)
        self.B3.place(x=487, y=455)

        self.b4 = IntVar()
        self.B4 = Checkbutton(self.canvas, text="Average", bg="white", onvalue=1, offvalue=0,variable = self.b4)
        self.B4.place(x=487, y=480)

#=====================================================STORAGE WITH CHECKBOX=============================================================#

        self.mystorage = ImageTk.PhotoImage(file=r"mystorage.png")
        self.storage = Label(self.canvas, text="Storage/\nROM", compound=TOP, image=self.mystorage, width=54, height=75,bg="white")
        self.storage.image = self.mystorage
        self.storage.place(x=700, y=300)

        self.s1 = IntVar()
        self.S1 = Checkbutton(self.canvas, text="256 GB & Above", bg="white", onvalue=1, offvalue=0,variable = self.s1)
        self.S1.place(x=687, y=405)

        self.s2 = IntVar()
        self.S2 = Checkbutton(self.canvas, text="128 GB", bg="white", onvalue=1, offvalue=0,variable = self.s2)
        self.S2.place(x=687, y=430)

        self.s3 = IntVar()
        self.S3 = Checkbutton(self.canvas, text="64 GB", bg="white", onvalue=1, offvalue=0,variable = self.s3)
        self.S3.place(x=687, y=455)

        self.s4 = IntVar()
        self.S4 = Checkbutton(self.canvas, text="32 GB & Below", bg="white", onvalue=1, offvalue=0,variable = self.s4)
        self.S4.place(x=687, y=480)

#=======================================================DISPLAY WITH CHECKBOX===========================================================#

        self.mydisplay = ImageTk.PhotoImage(file=r"mydisplay.png")
        self.display = Label(self.canvas, text="Display\nQuality", compound=TOP, image=self.mydisplay, width=54, height=76,bg="white")
        self.display.image = self.mydisplay
        self.display.place(x=900, y=300)

        self.d1 = IntVar()
        self.D1 = Checkbutton(self.canvas, text="Excellent (2560 X 1440) (4K)", bg="white", onvalue=1, offvalue=0,variable = self.d1)
        self.D1.place(x=887, y=405)

        self.d2 = IntVar()
        self.D2 = Checkbutton(self.canvas, text=" Very Good (1920 X 1080)", bg="white", onvalue=1, offvalue=0,variable = self.d2)
        self.D2.place(x=887, y=430)

        self.d3 = IntVar()
        self.D3 = Checkbutton(self.canvas, text="Good (1280 X 720)", bg="white", onvalue=1, offvalue=0,variable = self.d3)
        self.D3.place(x=887, y=455)

        self.d4 = IntVar()
        self.D4 = Checkbutton(self.canvas, text="Average (below 720p)", bg="white", onvalue=1, offvalue=0,variable = self.d4)
        self.D4.place(x=887, y=480)

#======================================================RAM WITH CHECKBOX================================================================#

        self.myram = ImageTk.PhotoImage(file=r"myram.png")
        self.ram = Label(self.canvas, text="RAM", compound=TOP, image=self.myram, width=54, height=61, bg="white")
        self.ram.image = self.myram
        self.ram.place(x=1110, y=310)

        self.r1 = IntVar()
        self.R1 = Checkbutton(self.canvas, text="8GB & Above", bg="white", onvalue=1, offvalue=0,variable = self.r1)
        self.R1.place(x=1097, y=405)

        self.r2 = IntVar()
        self.R2 = Checkbutton(self.canvas, text="6GB", bg="white", onvalue=1, offvalue=0,variable = self.r2)
        self.R2.place(x=1097, y=430)

        self.r3 = IntVar()
        self.R3 = Checkbutton(self.canvas, text="4GB", bg="white", onvalue=1, offvalue=0,variable = self.r3)
        self.R3.place(x=1097, y=455)

        self.r4 = IntVar()
        self.R4 = Checkbutton(self.canvas, text="3GB & Below", bg="white", onvalue=1, offvalue=0,variable = self.r4)
        self.R4.place(x=1097, y=480)

#========================================================CATEGORY======================================================================#

        self.mycategory = ImageTk.PhotoImage(file=r"qwer.png")
        self.category = Label(self.canvas, text="Categories", compound=TOP, image=self.mycategory, width=54, height=65, bg="white")
        self.category.image = self.mycategory
        self.category.place(x=1295, y=313)

        self.o1 = IntVar()
        self.cat1 = Checkbutton(self.canvas, text="Normal usage\n(online surfing)", bg="white", onvalue=1, offvalue=0,variable = self.o1)
        self.cat1.place(x=1280, y=400)

        self.o2 = IntVar()
        self.cat2 = Checkbutton(self.canvas, text="Photogenic\n(photography)", bg="white", onvalue=1, offvalue=0,variable = self.o2)
        self.cat2.place(x=1280, y=435)

        self.o3 = IntVar()
        self.cat3 = Checkbutton(self.canvas, text=" Travelling", bg="white", onvalue=1, offvalue=0,variable = self.o3)
        self.cat3.place(x=1280, y=470)

        self.o4 = IntVar()
        self.cat4 = Checkbutton(self.canvas, text="Gaming", bg="white", onvalue=1, offvalue=0,variable = self.o4)
        self.cat4.place(x=1280, y=490)

        self.o5 = IntVar()
        self.cat5 = Checkbutton(self.canvas, text="Premium",fg="dark goldenrod", bg="white", onvalue=1, offvalue=0, variable=self.o5)
        self.cat5.place(x=1280, y=510)

        self.mycrown = ImageTk.PhotoImage(file=r"crown2.png") #premium crown icon
        self.crown = Label(self.canvas, image=self.mycrown, width=15, height=15,bg="white")
        self.crown.image = self.mycrown
        self.crown.place(x=1354, y=511)

#=====================================================================================================================================#
#==========================================================LOGIN PAGE=================================================================#
#=====================================================================================================================================#


class mainscreen:
    def __init__(self,master):
        self.master = master
        self.canvas = Canvas(self.master, width=200, height=200, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        def calling():
            if(self.entry.get() != password):
                messagebox.showerror("Authentication Failed","INVALID PASSWORD")
            else:
                self.heading.place_forget()
                self.passkey.place_forget()
                self.entry.place_forget()
                self.button.place_forget()
                self.canvas.delete("all")
                page = detail_page(self.canvas)


        self.image = ImageTk.PhotoImage(file=r"haha.png")
        self.canvas.create_image(30, 18, image=self.image, anchor=NW)

        self.heading = Label(self.canvas, text="HEY GEEK!!! ,Welcome ",bg="lavender", fg='navy',font=("ansi", 50, "bold"))
        self.heading.place(x=735,y=100)

        self.passkey = Label(self.canvas, text="Please enter your password below :", bg='white', font=("arial",30, "bold"))
        self.passkey.place(x=800, y=350)

        self.entry = Entry(self.canvas, bg='gray86', relief="groove", width=40, font=("arial", 20),show = "●")
        self.entry.place(x=830, y=485)

        self.button = Button(self.canvas, text="SUBMIT", fg='WHITE', bg='limegreen', relief="solid", width=14,font=("arial", 24, "bold"), command = calling)
        self.button.place(x=1000, y=600)

window = Tk()
window.geometry('1920x1080')
window.title("Phone suggestor")
a = mainscreen(window)

window.mainloop()
