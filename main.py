"""
this app gives the user an easy to use interface to analyze medical insurance bills

*autor ARobatjazi*
startation date: 1402/05/31

current task/state:
    define functionality for opn_clicked method        

"""

from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import pyperclip
import sys
sys.path.insert(0, "./calculate.png")

tarafe_opg = 1861720
franshize = 10

root = Tk()
root.title("محاسبه‌گر خسارت درمانی")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int( (screen_width/2) - (500/2) )
y = int( (screen_height/2) - (500/2) )
root.geometry(f"{400}x{400}+{x}+{y}")
root.config(bg = "#ebecee")
root.resizable(False, False)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.columnconfigure(1, weight = 2)


opg_total = StringVar()
opg_sazman = StringVar()
opg_bimar = StringVar()
opg_pay = StringVar()

azmayesh_total = StringVar()
azmayesh_sazman = StringVar()
azmayesh_bimar = StringVar()
azmayesh_pay = StringVar()



def opg_clicked(e = 1):
    global opg_index
    opg_index = 0
    
    def up(e):
        global opg_index
        if opg_index == 0:
            opg_index = 3
        else:
            opg_index -= 1
        entries[opg_index].focus_set()
        

    def down(e):
        global opg_index
        if opg_index == 3:
            opg_index = 0
        else:
            opg_index += 1
        entries[opg_index].focus_set()

    def opg_calculate(e = 1):
        
        total = opg_total.get()
        sazman = opg_sazman.get()
        bimar = opg_bimar.get()
        pay = opg_pay.get()
        ghabel_pardakht = 0
        
        try:
            int(total)
            int(sazman)
            int(bimar)
            int(pay)
        except:
            print("ERROR")
            messagebox.showerror("خطا در ورودی اطلاعات","  لطفا مقادیر ورودی را کنترل نمایید")
            opg_window.focus_set()
            total_Entry.focus_set()
            global opg_index
            opg_index = 0
        else:
            print("convert to int sucsesful")      
            
            if (sazman == "0" or sazman == "") and (bimar != "0" and bimar != ""):
                if int(pay) > (tarafe_opg*0.9):
                    bedone_kasr = tarafe_opg - int(bimar)
                    ba_kasr = int(pay) - bedone_kasr
                    ghabel_pardakht = (ba_kasr*0.9) + bedone_kasr
                    print(int(ghabel_pardakht))
                    pyperclip.copy(int(ghabel_pardakht))
                    opg_window.destroy()

                else:
                    ghabel_pardakht = int(pay)
                    print(ghabel_pardakht)
                    pyperclip.copy(int(ghabel_pardakht))
                    opg_window.destroy()
                
                
            elif (sazman != "0" and sazman != "") and (bimar == "0" or bimar == ""):
                sahm_bimar = (int(sazman) / 30) * 70
                ba_kasr = (int(pay) - sahm_bimar) *0.9
                ghabel_pardakht = int(sahm_bimar + ba_kasr)
                print(ghabel_pardakht)
                pyperclip.copy(int(ghabel_pardakht))
                opg_window.destroy()

            elif (sazman != "0" and sazman != "") and (bimar != "0" and bimar != ""):
                if int(pay) > (tarafe_opg*0.9):
                    bedone_kasr = tarafe_opg - int(bimar)
                    ba_kasr = int(pay) - bedone_kasr
                    ghabel_pardakht = (ba_kasr*0.9) + bedone_kasr
                    print(int(ghabel_pardakht))
                    pyperclip.copy(int(ghabel_pardakht))
                    opg_window.destroy()

                else:
                    ghabel_pardakht = int(pay)
                    print(ghabel_pardakht)
                    pyperclip.copy(int(ghabel_pardakht))
                    opg_window.destroy()
        
    

    opg_window = Toplevel()
    opg_window.title("محسابه خسارات پاراکلینیکی")
    opg_window.geometry(f"{400}x{400}+{x}+{y}")
    opg_window.config(bg = "#e6e6e6")
    opg_window.resizable(False, False)
    opg_window.rowconfigure(0, weight = 1)
    opg_window.rowconfigure(1, weight = 1)
    opg_window.rowconfigure(2, weight = 1)
    opg_window.rowconfigure(3, weight = 1)
    opg_window.rowconfigure(4, weight = 1)
    opg_window.columnconfigure(0, weight = 1)
    opg_window.columnconfigure(1, weight = 1)
    opg_window.bind('<Return>', opg_calculate)
    opg_window.bind('<Up>', up)
    opg_window.bind('<Down>', down)

    total_Label = Label(opg_window, text = "مبلغ کل", bg = "#e6e6e6", fg = "black", font = "Btitr 14 bold");
    total_Label.grid(row = 0, column = 1, sticky=NSEW)
    total_Entry = Entry(opg_window, font="Bnazanin 14", highlightcolor="#d4e4f4", highlightthickness=2, textvariable = opg_total); 
    total_Entry.grid(row = 0, column = 0)
    
    sazman_Label = Label(opg_window, text = "سهم سازمان", bg = "#e6e6e6", fg = "black", font = "Btitr 14 bold"); 
    sazman_Label.grid(row = 1, column = 1, sticky=NSEW)
    sazman_Entry = Entry(opg_window, font="Bnazanin 14", highlightcolor="#d4e4f4", highlightthickness=2, textvariable = opg_sazman); 
    sazman_Entry.grid(row = 1, column = 0)
    
    bimar_Label = Label(opg_window, text = "سهم بیمار", bg = "#e6e6e6", fg = "black", font = "Btitr 14 bold");
    bimar_Label.grid(row = 2, column = 1, sticky=NSEW)
    bimar_Entry = Entry(opg_window, font="Bnazanin 14", highlightcolor="#d4e4f4", highlightthickness=2, textvariable = opg_bimar);
    bimar_Entry.grid(row = 2, column = 0)
    
    pay_Label = Label(opg_window, text = "مبلغ پرداختی", bg = "#e6e6e6", fg = "black", font = "Btitr 14 bold");
    pay_Label.grid(row = 3, column = 1, sticky=NSEW)
    pay_Entry = Entry(opg_window, font="Bnazanin 14", highlightcolor="#d4e4f4", highlightthickness=2, textvariable = opg_pay);
    pay_Entry.grid(row = 3, column = 0)
    global photo
    photo = PhotoImage(file=r'calculate.png')
    calculate_Button = Button(opg_window, image = photo, borderwidth=0,  command=opg_calculate)
    calculate_Button.grid(row = 4, column = 0, columnspan = 2)
    
    
    entries = [total_Entry, sazman_Entry, bimar_Entry, pay_Entry]
    entries[opg_index].focus_set()
    


def azmayesh_clicked(e = 1):
    global azmayesh_index
    azmayesh_index = 0
    def up(e):
        global azmayesh_index
        if azmayesh_index == 0:
            azmayesh_index = 3
        else:
            azmayesh_index -= 1
        entries[azmayesh_index].focus_set()
        

    def down(e):
        global azmayesh_index
        if azmayesh_index == 3:
            azmayesh_index = 0
        else:
            azmayesh_index += 1
        entries[azmayesh_index].focus_set()

    def azmayesh_calculate(e = 1):
        az_total = azmayesh_total.get()
        az_sazman = azmayesh_sazman.get()
        az_bimar = azmayesh_bimar.get()
        az_pay = azmayesh_pay.get()
        az_ghabel_pardakht = 0    

        try:
            int(az_total)
            int(az_sazman)
            int(az_bimar)
            int(az_pay)
        except:
            print(azmayesh_total.get())
            print("ERROR")
            messagebox.showerror("خطا در ورودی اطلاعات","  لطفا مقادیر ورودی را کنترل نمایید")
            azmayesh_window.focus_set()
            total_Entry.focus_set()
            global azmayesh_index
            azmayesh_index = 0

        else:
            
            if int(az_sazman) != 0:
                bedone_kasr = int(az_sazman)/22 *78
                ba_kasr = (int(az_pay) - bedone_kasr) *0.9
                az_ghabel_pardakht = int(ba_kasr + bedone_kasr)
                print(az_ghabel_pardakht)
                pyperclip.copy(int(az_ghabel_pardakht))
                azmayesh_window.destroy()
            else:
                az_sazman = int(az_bimar) /78 *22
                bedone_kasr = int(az_sazman)/22 *78
                ba_kasr = (int(az_pay) - bedone_kasr) *0.9
                az_ghabel_pardakht = int(ba_kasr + bedone_kasr)
                print(az_ghabel_pardakht)
                pyperclip.copy(int(az_ghabel_pardakht))
                azmayesh_window.destroy()
        
    azmayesh_window = Toplevel()
    azmayesh_window.title("محاسبه هزینه‌ی آزمایش")
    azmayesh_window.geometry(f"{400}x{400}+{x}+{y}")
    azmayesh_window.config(bg = "#e6e6e6")
    azmayesh_window.resizable(False, False)
    azmayesh_window.rowconfigure(0, weight = 1)
    azmayesh_window.rowconfigure(1, weight = 1)
    azmayesh_window.rowconfigure(2, weight = 1)
    azmayesh_window.rowconfigure(3, weight = 1)
    azmayesh_window.rowconfigure(4, weight = 1)
    azmayesh_window.columnconfigure(0, weight = 1)
    azmayesh_window.columnconfigure(1, weight = 1)
    azmayesh_window.bind("<Return>", azmayesh_calculate)
    azmayesh_window.bind('<Up>', up)
    azmayesh_window.bind('<Down>', down)
    azmayesh_window.grab_set()

    total_Label = Label(azmayesh_window, text = "مبلغ کل", bg = "#e6e6e6", fg = "black", font = "Btitr 14 bold");
    total_Label.grid(row = 0, column = 1, sticky=NSEW)
    total_Entry = Entry(azmayesh_window, font="Bnazanin 14", highlightcolor="#d4e4f4", highlightthickness=2, textvariable = azmayesh_total); 
    total_Entry.grid(row = 0, column = 0)
    
    sazman_Label = Label(azmayesh_window, text = "سهم سازمان", bg = "#e6e6e6", fg = "black", font = "Btitr 14 bold"); 
    sazman_Label.grid(row = 1, column = 1, sticky=NSEW)
    sazman_Entry = Entry(azmayesh_window, font="Bnazanin 14", highlightcolor="#d4e4f4", highlightthickness=2, textvariable = azmayesh_sazman); 
    sazman_Entry.grid(row = 1, column = 0)
    
    bimar_Label = Label(azmayesh_window, text = "سهم بیمار", bg = "#e6e6e6", fg = "black", font = "Btitr 14 bold");
    bimar_Label.grid(row = 2, column = 1, sticky=NSEW)
    bimar_Entry = Entry(azmayesh_window, font="Bnazanin 14", highlightcolor="#d4e4f4", highlightthickness=2, textvariable = azmayesh_bimar);
    bimar_Entry.grid(row = 2, column = 0)
    
    pay_Label = Label(azmayesh_window, text = "مبلغ پرداختی", bg = "#e6e6e6", fg = "black", font = "Btitr 14 bold");
    pay_Label.grid(row = 3, column = 1, sticky=NSEW)
    pay_Entry = Entry(azmayesh_window, font="Bnazanin 14", highlightcolor="#d4e4f4", highlightthickness=2, textvariable = azmayesh_pay);
    pay_Entry.grid(row = 3, column = 0)
    global photo
    photo = PhotoImage(file=r'calculate.png')
    calculate_Button = Button(azmayesh_window, image=photo, command=azmayesh_calculate, borderwidth=0)
    calculate_Button.grid(row = 4, column = 0, columnspan = 2)

    entries = [total_Entry,sazman_Entry, bimar_Entry, pay_Entry]
    entries[azmayesh_index].focus_set()


text = Label(root, text = "انتخاب نوع خسارت", bg = "#eff2f5", fg = "black", font = "Btitr 18 bold")
text.grid(row = 0, column = 1, sticky=NSEW)

opg_Button = Button(root, text = "رادیوگرافی پانورکس و غیره", bg = "#e6e6e6", fg = "black", font="Bnazanin 18 bold",borderwidth=0,  command = opg_clicked)
opg_Button.grid(row = 1, column = 1, sticky=NSEW)

azmayesh_Button = Button(root, text = "انواع آزمایش", bg = "#e6e6e6", fg = "black", font="Bnazanin 18 bold", borderwidth=0,command = azmayesh_clicked)
azmayesh_Button.grid(row = 2, column = 1, sticky=NSEW)




root.mainloop()
