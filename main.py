

from tkinter import *
from PIL import ImageTk
import database_functionality
from tkinter import messagebox
import webbrowser


class show_details:
    def __init__(self,canvas,name):
        self.canvas = canvas
        self.name = name
        self.brand,self.model = self.name.split(";")

        def callback(url):
            webbrowser.open_new(url)

        self.heading = Label(self.canvas, text= self.brand + " " + self.model, bg='lightyellow2', fg='midnight blue', relief="solid",font=("arial",30, "bold"))
        self.heading.pack(pady=2)

        self.r = ImageTk.PhotoImage(file="s65.png")
        self.canvas.create_image(747,432,image=self.r)
        self.canvas.image = self.r

        self.label = Label(self.canvas, text="Purchase Here by Clicking icon(s) below", bg="white",font=("arial",15, "bold"))
        self.label.place(x=1050, y=550)

        self.spec = Label(self.canvas, text="Specifications", fg="black", compound=TOP, bg="white", font=("arial", 26, "bold"))
        self.spec.place(x=627, y=125)


        data = database_functionality.details(self.brand,self.model)

        self.ram = Label(self.canvas, text="RAM      :  " + str(data[0][11]) +" GB", bg="white",font=("arial",10,"bold"))
        self.ram.place(x=600, y=275)

        self.rom = Label(self.canvas, text="Storage :  " + str(data[0][15])+" GB", bg="white",font=("arial",10,"bold"))
        self.rom.place(x=600, y=325)

        self.display = Label(self.canvas, text="Screen  :  " + str(data[0][14]) + " inches", bg="white",font=("arial", 10, "bold"))
        self.display.place(x=600, y=375)

        self.camera = Label(self.canvas, text="Camera :  " + str(data[0][10]) + " MP", bg="white",font=("arial", 10, "bold"))
        self.camera.place(x=600, y=425)

        self.bat = Label(self.canvas, text="Battery  :  " + str(data[0][13]) + " mAh" , bg="white",font=("arial", 10, "bold"))
        self.bat.place(x=600, y=475)

        self.processor = Label(self.canvas, text="Processor  :  " + str(data[0][12]), bg="white",font=("arial", 10, "bold"))
        self.processor.place(x=600, y=525)

        self.rom = Label(self.canvas, text="Operating System:  " + str(data[0][16]), bg="white",font=("arial", 10, "bold"))
        self.rom.place(x=600, y=575)

        self.price = Label(self.canvas, text=" Price : ₹ " + str(data[0][2]) + " ", bg="white",relief="solid",font=("arial",30, "bold"))
        self.price.place(x=1060, y=325)

        def fun1():
            if (data[0][19] == "NIL"):
                messagebox.showinfo("Uh-Oh", "Sorry,No link for Amazon : (")

        def fun2():
            if (data[0][20] == "NIL"):
                messagebox.showinfo("Uh-Oh", "Sorry,no link for Flipkart : (")

        self.logo1 = ImageTk.PhotoImage(file="amazonlogo.png")   #Amazon
        self.link1 = Button(self.canvas,image = self.logo1,text="  "+data[0][19]+"  ", fg="blue", cursor="hand2", bg="white",relief="solid"
                            ,command = fun1,font=("arial",12, "bold"))
        self.link1.image = self.logo1
        self.link1.place(x=1125,y=615)
        if(data[0][19]!="NIL"):
            self.link1.bind("<Button-1>", lambda e: callback(data[0][19]))

        self.logo2 = ImageTk.PhotoImage(file="flipf.png")    #Flipkart
        self.link2 = Button(self.canvas,image = self.logo2, text="  "+data[0][20]+"  ", fg="blue", cursor="hand2", bg="white"
                            ,relief="solid",command = fun2,font=("arial",12, "bold"))
        self.link2.image = self.logo2
        self.link2.place(x=1275, y=615)

        if (data[0][20] != "NIL"):
            self.link2.bind("<Button-1>", lambda e: callback(data[0][20]))


        self.rating = Label(self.canvas, text="Rating : " + str(data[0][18]) + " / 10 ", bg="white",font=("arial", 40, "bold"))
        self.rating.place(x=1030, y=175)

        a = str(data[0][17]).replace(",","\n")

        self.color = Label(self.canvas,text = a, bg="white",font=("arial",20),justify = LEFT)
        self.color.place(x=50, y=560)
        print(data)

        self.label = Label(self.canvas, text="Colours Available :", bg="white",font=("arial", 26, "bold"))
        self.label.place(x=10, y=500)


class showphone:
    def __init__(self,canvas,result):
        self.canvas = canvas
        self.result = result
        self.d = list()

        self.heading = Label(self.canvas, text=" Here are some Suggested phone(s) ", fg='navy', bg='lavender',anchor = NW,font=("arial", 38, "bold"))
        self.heading.pack(pady=20)

        self.label = Label(self.canvas, text="Click on Phone for its Specifictions and Price :",bg="white",font=("arial", 28, "bold"))
        self.label.place(x=675,y=130)

        self.image = ImageTk.PhotoImage(file="men.png")
        self.canvas.create_image(385, 470, image=self.image)


        def func(name):

            for i in range(0, len(self.d)):
                self.d[i].place_forget()
            self.canvas.delete("all")
            self.heading.pack_forget()
            self.label.place_forget()
            page6 = show_details(self.canvas,name)

        j = 0
        yvar = 225
        for i in self.result:
            self.d.append(Button(self.canvas,text = result[j][0] + " " + result [j][1],fg='springgreen4', bg='honeydew2', relief="solid",
                                 width=35,height=1,font=("arial",18, "bold"),command = lambda x=result[j][0] + ";" + result [j][1]: func(x)))
            self.d[j].place(x=810,y=yvar)
            yvar=58+yvar

            j+=1

#======================================================PRICE PAGE====================================================================#

class pricepage:


    def __init__(self,canvas):
        self.canvas = canvas
        self.heading = Label(self.canvas, text=" PHONE SUGGESTOR ", fg='orange2', bg='navy', relief="solid",
                             font=("arial", 42, "bold"))
        self.heading.pack(pady=20)

                #-------------------------------------------Functions-----------------------------------------#

        def button_a_func():
            min = 59999
            max = 200000
            r = database_functionality.value(min,max)
            self.canvas.delete("all")
            self.text.place_forget()
            self.button_a.place_forget()
            self.button_b.place_forget()
            self.button_c.place_forget()
            self.button_d.place_forget()
            self.button_e.place_forget()
            self.button_f.place_forget()
            self.button_g.place_forget()
            self.button_h.place_forget()
            self.heading.pack_forget()

            page7 = showphone(self.canvas,r)

        def button_b_func():
            min = 50000
            max = 60000
            self.r = database_functionality.value(min, max)
            self.canvas.delete("all")
            self.text.place_forget()
            self.button_a.place_forget()
            self.button_b.place_forget()
            self.button_c.place_forget()
            self.button_d.place_forget()
            self.button_e.place_forget()
            self.button_f.place_forget()
            self.button_g.place_forget()
            self.button_h.place_forget()
            self.heading.pack_forget()
            page7 = showphone(self.canvas, self.r)

        def button_c_func():
            min = 40000
            max = 50000
            self.r = database_functionality.value(min, max)
            self.canvas.delete("all")
            self.text.place_forget()
            self.button_a.place_forget()
            self.button_b.place_forget()
            self.button_c.place_forget()
            self.button_d.place_forget()
            self.button_e.place_forget()
            self.button_f.place_forget()
            self.button_g.place_forget()
            self.button_h.place_forget()
            self.heading.pack_forget()
            page7 = showphone(self.canvas, self.r)

        def button_d_func():
            min = 30000
            max = 40000
            self.r = database_functionality.value(min, max)
            self.canvas.delete("all")
            self.text.place_forget()
            self.button_a.place_forget()
            self.button_b.place_forget()
            self.button_c.place_forget()
            self.button_d.place_forget()
            self.button_e.place_forget()
            self.button_f.place_forget()
            self.button_g.place_forget()
            self.button_h.place_forget()
            self.heading.pack_forget()
            page7 = showphone(self.canvas, self.r)

        def button_e_func():
            min = 20000
            max = 30000
            self.r = database_functionality.value(min, max)
            self.canvas.delete("all")
            self.text.place_forget()
            self.button_a.place_forget()
            self.button_b.place_forget()
            self.button_c.place_forget()
            self.button_d.place_forget()
            self.button_e.place_forget()
            self.button_f.place_forget()
            self.button_g.place_forget()
            self.button_h.place_forget()
            self.heading.pack_forget()
            page7 = showphone(self.canvas, self.r)

        def button_f_func():
            min = 15000
            max = 20000
            self.r = database_functionality.value(min, max)
            self.canvas.delete("all")
            self.text.place_forget()
            self.button_a.place_forget()
            self.button_b.place_forget()
            self.button_c.place_forget()
            self.button_d.place_forget()
            self.button_e.place_forget()
            self.button_f.place_forget()
            self.button_g.place_forget()
            self.button_h.place_forget()
            self.heading.pack_forget()
            page7 = showphone(self.canvas, self.r)

        def button_g_func():
            min = 10000
            max = 15000
            self.r = database_functionality.value(min, max)
            self.canvas.delete("all")
            self.text.place_forget()
            self.button_a.place_forget()
            self.button_b.place_forget()
            self.button_c.place_forget()
            self.button_d.place_forget()
            self.button_e.place_forget()
            self.button_f.place_forget()
            self.button_g.place_forget()
            self.button_h.place_forget()
            self.heading.pack_forget()
            page7 = showphone(self.canvas, self.r)

        def button_h_func():
            min = 0
            max = 10000
            self.r = database_functionality.value(min, max)
            self.canvas.delete("all")
            self.text.place_forget()
            self.button_a.place_forget()
            self.button_b.place_forget()
            self.button_c.place_forget()
            self.button_d.place_forget()
            self.button_e.place_forget()
            self.button_f.place_forget()
            self.button_g.place_forget()
            self.button_h.place_forget()
            self.heading.pack_forget()
            page7 = showphone(self.canvas, self.r)

             # ---------------------------------------------------------------------------------------------#

             #----------------------------------Buttons and Labels------------------------------------------#

        self.text = Label(self.canvas, text=" Select Price(₹) Range according to your choice:", bg="white",font=("arial", 26, "bold"))
        self.text.place(x=660, y=200)

        self.button_a = Button(self.canvas, text="60,000 & Above", fg='black', bg='white', relief="groove", width=26,font=("arial", 18, "bold"),command = button_a_func)
        self.button_a.config(activebackground = "red")
        self.button_a.place(x=850, y=320)

        self.button_b = Button(self.canvas, text="50,000 - 60,000", fg='black', bg='white', relief="groove", width=26,font=("arial", 18, "bold"),command = button_b_func)
        self.button_b.config(activebackground="tomato")
        self.button_b.place(x=850, y=370)

        self.button_c = Button(self.canvas, text="40,000 - 50,000", fg='black', bg='white', relief="groove", width=26,font=("arial", 18, "bold"),command = button_c_func)
        self.button_c.config(activebackground="DarkOrange3")
        self.button_c.place(x=850, y=420)

        self.button_d = Button(self.canvas, text="30,000 - 40,000", fg='black', bg='white', relief="groove", width=26,font=("arial", 18, "bold"),command = button_d_func)
        self.button_d.config(activebackground="orange")
        self.button_d.place(x=850, y=470)

        self.button_e = Button(self.canvas, text="20,000 - 30,000", fg='black', bg='white', relief="groove", width=26,font=("arial", 18, "bold"),command = button_e_func)
        self.button_e.config(activebackground="yellow3")
        self.button_e.place(x=850, y=520)

        self.button_f = Button(self.canvas, text="15,000 - 20,000", fg='black', bg='white', relief="groove", width=26,font=("arial", 18, "bold"),command = button_f_func)
        self.button_f.config(activebackground="greenyellow")
        self.button_f.place(x=850, y=570)

        self.button_g = Button(self.canvas, text="10,000 - 15,000", fg='black', bg='white', relief="groove", width=26,font=("arial", 18, "bold"),command = button_g_func)
        self.button_g.config(activebackground="chartreuse3")
        self.button_g.place(x=850, y=620)

        self.button_h = Button(self.canvas, text="10,000 & Below", fg='black', bg='white', relief="groove", width=26,font=("arial", 18, "bold"),command = button_h_func)
        self.button_h.config(activebackground="light sea green")
        self.button_h.place(x=850, y=670)

        def backbutton_calling():

           self.canvas.pack_forget()
           a = mainscreen(window)

        self.mybackbutton = ImageTk.PhotoImage(file=r"mybackbutton.png")
        self.backbutton = Button(self.canvas, text="BACK", compound=TOP,image = self.mybackbutton, width=55, height=62,relief = "solid", bg="white",command = backbutton_calling)
        self.backbutton.image = self.mybackbutton
        self.backbutton.place(x=1460, y=720)

#=========================================================FEATURE PAGE================================================================#

class featurepage:


    def __init__(self,canvas):
        self.canvas = canvas

        self.heading = Label(self.canvas, text=" PHONE SUGGESTOR ", fg='orange2', bg='navy', relief="solid",font=("arial", 42, "bold"))
        self.heading.pack(pady=20)

        self.text = Label(self.canvas, text=" Select Features according to your choice:",bg="white",font=("arial",26,"bold"))
        self.text.place(x=680, y=175)

        self.tip = Label(self.canvas, text=" * TIP : For Better RESULTS,Make a Balanced combination of given Features.",fg="red", bg="white",font=( 6))
        self.tip.place(x=15, y=765)

        def commonfunction(r):
            if (r == " Excellent "):
                return '1000'
            elif (r == " Very Good "):
                return '0100'
            elif (r == " Good "):
                return '0010'
            elif (r == " Average "):
                return '0001'

        def romfunction(r):
            if (r == " 256 GB & Above"):
                return '1000'
            elif (r == "128 GB"):
                return '0100'
            elif (r == "64 GB"):
                return '0010'
            elif (r == "32 GB & Below "):
                return '0001'

        def displayfunction(r):
            if (r == " Excellent (2560 X 1440) (4K) "):
                return '1000'
            elif (r == " Very Good (1920 X 1080) "):
                return '0100'
            elif (r == " Good (1280 X 720) "):
                return '0010'
            elif (r == " Average (below 720p) "):
                return '0001'

        def ramfunction(r):
            if (r == " 8GB & Above (Excellent) "):
                return '1000'
            elif (r == " 6GB (Very Good) "):
                return '0100'
            elif (r == " 4GB (Good) "):
                return '0010'
            elif (r == " 3GB & Below (Average) "):
                return '0001'

        def collect():
            cq = commonfunction(self.camera_input.get())
            pq = commonfunction(self.mychip_input.get())
            bq = commonfunction(self.mybattery_input.get())
            sq = romfunction(self.mystorage_input.get())
        
            dq = displayfunction(self.mydisplay_input.get())
            rq = ramfunction(self.myram_input.get())
            r = database_functionality.find_phone(cq,pq,bq,sq,dq,rq)
            if(r == 'e'):
                messagebox.showinfo("uh-oh","No Phone found   : ( ")
            else:
                self.canvas.delete("all")
                self.text.place_forget()
                self.tip.place_forget()
                self.camera.place_forget()
                self.chip.place_forget()
                self.battery.place_forget()
                self.storage.place_forget()
                self.display.place_forget()
                self.ram.place_forget()
                self.heading.pack_forget()
                self.camera_menu.place_forget()
                self.mychip_menu.place_forget()
                self.mybattery_menu.place_forget()
                self.mystorage_menu.place_forget()
                self.mydisplay_menu.place_forget()
                self.myram_menu.place_forget()
                self.submit_button.place_forget()
                self.backbutton.place_forget()
                result_page = showphone(self.canvas,r)

        self.submit_button = Button(self.canvas, text="SUBMIT", fg='thistle2', bg='spring GREEN4', relief="solid", width=10,font=("arial", 20, "bold"),command = collect)
        self.submit_button.place(x=890,y=710)

        def backbutton_calling():

           self.canvas.pack_forget()
           a = mainscreen(window)

        self.mybackbutton = ImageTk.PhotoImage(file=r"mybackbutton.png")
        self.backbutton = Button(self.canvas, text="BACK", compound=TOP,image = self.mybackbutton, width=55, height=62,relief = "solid", bg="white",command = backbutton_calling)
        self.backbutton.image = self.mybackbutton
        self.backbutton.place(x=1460, y=720)

        # ----------------------------------Icon with dropdowns------------------------------------------#

        # CAMERA

        self.mycamera = ImageTk.PhotoImage(file=r"mycamera.png")
        self.camera = Label(self.canvas,text = "Camera\n Quality",compound = TOP,image = self.mycamera,width = 54,height = 74,bg="white")
        self.camera.image = self.mycamera
        self.camera.place(x=725,y=300)

        self.feature_list = [" Excellent ", " Very Good ", " Good ", " Average "]
        self.camera_input = StringVar()
        self.camera_menu = OptionMenu(self.canvas, self.camera_input, *self.feature_list)
        self.camera_menu.configure(bg='white')
        self.camera_menu.place(x=790, y=310)

        # PROCESSOR/CHIP

        self.mychip = ImageTk.PhotoImage(file=r"mychip.png")
        self.chip = Label(self.canvas, text="Processor/\nchipset", compound=TOP, image=self.mychip, width=56, height=72,bg="white")
        self.chip.image = self.mychip
        self.chip.place(x=725, y=440)

        self.feature_list = [" Excellent "," Very Good "," Good "," Average "]
        self.mychip_input = StringVar()
        self.mychip_menu = OptionMenu(self.canvas, self.mychip_input, *self.feature_list)
        self.mychip_menu.configure(bg='white')
        self.mychip_menu.place(x=792, y=450)

        # BATTERY

        self.mybattery = ImageTk.PhotoImage(file=r"mybattery.png")
        self.battery = Label(self.canvas, text="Battery\n Performance", compound=TOP, image=self.mybattery, width=66, height=74,bg="white")
        self.battery.image = self.mybattery
        self.battery.place(x=1100, y=300)

        self.feature_list = [" Excellent ", " Very Good ", " Good ", " Average "]
        self.mybattery_input = StringVar()
        self.mybattery_menu = OptionMenu(self.canvas, self.mybattery_input, *self.feature_list)
        self.mybattery_menu.configure(bg='white')
        self.mybattery_menu.place(x=1176, y=315)

        # STORAGE

        self.mystorage = ImageTk.PhotoImage(file=r"mystorage.png")
        self.storage = Label(self.canvas, text="Storage/\nROM", compound=TOP, image=self.mystorage, width=54, height=75,bg="white")
        self.storage.image = self.mystorage
        self.storage.place(x=1110, y=437)

        self.feature_list = [" 256 GB & Above", "128 GB", "64 GB", "32 GB & Below "]
        self.mystorage_input = StringVar()
        self.mystorage_menu = OptionMenu(self.canvas, self.mystorage_input, *self.feature_list)
        self.mystorage_menu.configure(bg='white')
        self.mystorage_menu.place(x=1180, y=445)

        # DISPLAY

        self.mydisplay = ImageTk.PhotoImage(file=r"mydisplay.png")
        self.display = Label(self.canvas, text="Display\nQuality", compound=TOP, image=self.mydisplay, width=54, height=76,bg="white")
        self.display.image = self.mydisplay
        self.display.place(x=725, y=580)

        self.feature_list = [" Excellent (2560 X 1440) (4K) ", " Very Good (1920 X 1080) ", " Good (1280 X 720) ", " Average (below 720p) "]
        self.mydisplay_input = StringVar()
        self.mydisplay_menu = OptionMenu(self.canvas, self.mydisplay_input, *self.feature_list)
        self.mydisplay_menu.configure(bg='white')
        self.mydisplay_menu.place(x=790, y=590)

        # RAM

        self.myram = ImageTk.PhotoImage(file=r"myram.png")
        self.ram = Label(self.canvas, text="RAM", compound=TOP, image=self.myram, width=54, height=61, bg="white")
        self.ram.image = self.myram
        self.ram.place(x=1114, y=582)

        self.feature_list = [" 8GB & Above (Excellent) ", " 6GB (Very Good) ", " 4GB (Good) ", " 3GB & Below (Average) "]
        self.myram_input = StringVar()
        self.myram_menu = OptionMenu(self.canvas, self.myram_input, *self.feature_list)
        self.myram_menu.configure(bg='white')
        self.myram_menu.place(x=1180, y=590)

                  #-------------------------------------------------------------------------------------#

#=====================================================INTERSET/PURPOSE PAGE===========================================================#

class interestpage:


    def __init__(self,canvas):

        self.canvas = canvas

        self.heading = Label(self.canvas, text=" PHONE SUGGESTOR ", fg='orange2', bg='navy', relief="solid",
                             font=("arial", 42, "bold"))
        self.heading.pack(pady=20)

        def nf():
            result = database_functionality.internor()
            self.canvas.delete("all")
            self.text.place_forget()
            self.photo.place_forget()
            self.normal.place_forget()
            self.travel.place_forget()
            self.game.place_forget()
            self.pro.place_forget()
            self.heading.pack_forget()
            page8 = showphone(self.canvas,result)

        def pf():
            result = database_functionality.intercam()
            self.canvas.delete("all")
            self.text.place_forget()
            self.photo.place_forget()
            self.normal.place_forget()
            self.travel.place_forget()
            self.game.place_forget()
            self.pro.place_forget()
            self.heading.pack_forget()
            page8 = showphone(self.canvas,result)

        def tf():
            result = database_functionality.intertravel()
            self.canvas.delete("all")
            self.text.place_forget()
            self.photo.place_forget()
            self.normal.place_forget()
            self.travel.place_forget()
            self.game.place_forget()
            self.pro.place_forget()
            self.heading.pack_forget()
            page8 = showphone(self.canvas,result)

        def gf():
            result = database_functionality.intergame()
            self.canvas.delete("all")
            self.text.place_forget()
            self.photo.place_forget()
            self.normal.place_forget()
            self.travel.place_forget()
            self.game.place_forget()
            self.pro.place_forget()
            self.heading.pack_forget()
            page8 = showphone(self.canvas,result)

        def prof():
            result = database_functionality.interprop()
            self.canvas.delete("all")
            self.text.place_forget()
            self.photo.place_forget()
            self.normal.place_forget()
            self.travel.place_forget()
            self.game.place_forget()
            self.pro.place_forget()
            self.heading.pack_forget()
            page8 = showphone(self.canvas,result)


        self.text = Label(self.canvas, text=" Select Category According to your Interest:", fg='black', bg='white',font=("arial", 26, "bold"))
        self.text.place(x=680,y=180)

        self.myphoto = ImageTk.PhotoImage(file=r"self.png")
        self.photo = Button(self.canvas, text="Photogenic\n(Photography/\nBest Camera)", compound=TOP,
                            image=self.myphoto, width=100, height=100,relief="solid",bg="white",command = pf)
        self.photo.image = self.myphoto
        self.photo.place(x=900, y=300)

        self.mynormal = ImageTk.PhotoImage(file=r"normall.png")
        self.normal = Button(self.canvas, text="Normal Usage/\nOnline Surfing/\nStudent", compound=TOP,
                             image=self.mynormal, width=100, height=100, relief="solid", bg="white",command = nf)
        self.normal.image = self.mynormal
        self.normal.place(x=1060, y=300)

        self.mytravel = ImageTk.PhotoImage(file=r"travel.png")
        self.travel = Button(self.canvas, text="Travelling/\nBusiness/\nGreat Battery", compound=TOP,
                            image=self.mytravel, width=100, height=100, relief="solid", bg="white",command =tf)
        self.travel.image = self.mytravel
        self.travel.place(x=900, y=450)

        self.mygame = ImageTk.PhotoImage(file=r"game.png")
        self.game = Button(self.canvas, text="Gaming/\nFast Processing/\nLag Free Experince", compound=TOP,
                             image=self.mygame, width=100, height=100, relief="solid", bg="white",command =gf)
        self.game.image = self.mytravel
        self.game.place(x=1060, y=450)

        self.mypro = ImageTk.PhotoImage(file=r"pro1"r".png")
        self.pro = Button(self.canvas, text="    PREMIUM\n    PHONES",fg="Darkgoldenrod3",font=("times new roman",20,"bold"),
                          compound=LEFT,image=self.mypro, width=263, height=100, relief="sunken", bg="gray9",command =prof)
        self.pro.image = self.mypro
        self.pro.place(x=900, y=600)

        def backbutton_calling():

           self.canvas.pack_forget()
           a = mainscreen(window)

        self.mybackbutton = ImageTk.PhotoImage(file=r"mybackbutton.png")
        self.backbutton = Button(self.canvas, text="BACK", compound=TOP,image = self.mybackbutton, width=55, height=62,relief = "solid", bg="white",command = backbutton_calling)
        self.backbutton.image = self.mybackbutton
        self.backbutton.place(x=1460, y=720)

#=========================================================HOME PAGE===================================================================#

class mainscreen:


    def __init__(self,master):
        self.master = master


        self.canvas = Canvas(self.master,width=200,height=200,bg='white')
        self.canvas.pack(expand = YES , fill = BOTH)

        self.image = ImageTk.PhotoImage(file="smart.png")
        self.canvas.create_image(30,180, image=self.image, anchor=NW)

        self.heading = Label(self.canvas, text=" PHONE SUGGESTOR ", fg='orange2', bg='navy', relief="solid",font=("arial",42, "bold"))
        self.heading.pack(pady=20)

        self.askme = Label(self.canvas, text="Suggest me Phone by : ",bg='white', font=("arial", 32, "bold"))
        self.askme.place(x=825, y=225)

        #=================================CLASSES=================================#

    #class page_1_calling
        def pricepage_calling():
            self.askme.pack_forget()
            self.askme.place_forget()
            self.button1.pack_forget()
            self.button1.place_forget()
            self.button2.pack_forget()
            self.button2.place_forget()
            self.button4.pack_forget()
            self.button4.place_forget()
            self.recommended.pack_forget()
            self.recommended.place_forget()
            self.heading.pack_forget()
            page1 = pricepage(self.canvas)

    # class page_2_calling
        def featurepage_calling():
            self.heading.pack_forget()
            self.askme.pack_forget()
            self.askme.place_forget()
            self.button1.pack_forget()
            self.button1.place_forget()
            self.button2.pack_forget()
            self.button2.place_forget()
            self.button4.pack_forget()
            self.button4.place_forget()
            self.recommended.pack_forget()
            self.recommended.place_forget()
            page2 = featurepage(self.canvas)

    # class page_3_calling
        def interestpage_calling():
            self.heading.pack_forget()
            self.askme.pack_forget()
            self.askme.place_forget()
            self.button1.pack_forget()
            self.button1.place_forget()
            self.button2.pack_forget()
            self.button2.place_forget()
            self.button4.pack_forget()
            self.button4.place_forget()
            self.recommended.pack_forget()
            self.recommended.place_forget()
            page4 = interestpage(self.canvas)

        self.button1 = Button(self.canvas, text="PRICE RANGE", fg='WHITE', bg='dark ORANGE', relief="raised", width=20,
                             font=("arial", 24, "bold"),command = pricepage_calling)
        self.button1.place(x=850, y=375)

        self.button2 = Button(self.canvas, text="FEATURES", fg='white', bg='springgreen4', relief="raised", width=20,
                             font=("arial", 24, "bold"),command = featurepage_calling)
        self.button2 .place(x=850, y=475)

        self.recommended = Label(self.canvas, text="(Recommended)", bg='white', font=("arial",20, "bold"))
        self.recommended.place(x=1250, y=486)

        self.button4 = Button(self.canvas, text="PURPOSE", fg='white', bg='steel blue', relief="raised", width=20,font=("arial", 24, "bold"),command = interestpage_calling)
        self.button4.place(x=850, y=575)
#==========================================================MAINLOOP=====================================================================#

window = Tk()
window.geometry('1920x1080')
window.title("Phone suggestor")
a = mainscreen(window)

window.mainloop()