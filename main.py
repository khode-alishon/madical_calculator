"""
this app gives the user an easy to use interface to analyze medical insurance bills

*autor ARobatjazi*
startation date: 1402/05/31

current task/state:
    define functionality for opn_clicked method        

"""


from tkinter import *
from tkinter import messagebox

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

def opg_clicked():

    def opg_calculate():
        
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
          
        else:
            print("convert to int sucsesful")      
            
            if (sazman == "0" or sazman == "") and (bimar != "0" and bimar != ""):
                if int(pay) > (tarafe_opg*0.9):
                    bedone_kasr = tarafe_opg - int(bimar)
                    ba_kasr = int(pay) - bedone_kasr
                    ghabel_pardakht = (ba_kasr*0.9) + bedone_kasr
                    print(int(ghabel_pardakht))

                else:
                    ghabel_pardakht = int(pay)
                    print(ghabel_pardakht)
                
                
            elif (sazman != "0" and sazman != "") and (bimar == "0" or bimar == ""):
                sahm_bimar = (int(sazman) / 30) * 70
                ba_kasr = (int(pay) - sahm_bimar) *0.9
                ghabel_pardakht = int(sahm_bimar + ba_kasr)
                print(ghabel_pardakht)

            elif (sazman != "0" and sazman != "") and (bimar != "0" and bimar != ""):
                if int(pay) > (tarafe_opg*0.9):
                    bedone_kasr = tarafe_opg - int(bimar)
                    ba_kasr = int(pay) - bedone_kasr
                    ghabel_pardakht = (ba_kasr*0.9) + bedone_kasr
                    print(int(ghabel_pardakht))

                else:
                    ghabel_pardakht = int(pay)
                    print(ghabel_pardakht)
    
    
    opg_window = Toplevel()
    opg_window.title("محسابه خسارات پاراکلینیکی")
    opg_window.geometry(f"{400}x{400}+{x}+{y}")
    opg_window.config(bg = "#234884")
    opg_window.resizable(False, False)
    opg_window.rowconfigure(0, weight = 1)
    opg_window.rowconfigure(1, weight = 1)
    opg_window.rowconfigure(2, weight = 1)
    opg_window.rowconfigure(3, weight = 1)
    opg_window.rowconfigure(4, weight = 1)
    opg_window.columnconfigure(0, weight = 1)
    opg_window.columnconfigure(1, weight = 1)
    opg_window.attributes('-topmost', True)

    total_Label = Label(opg_window, text = "مبلغ کل", bg = "#234884", fg = "#ffffff", font = "Btitr 14 bold");
    total_Label.grid(row = 0, column = 1, sticky=NSEW)
    total_Entry = Entry(opg_window, font="Bnazanin 14", highlightcolor="#d4e4f4", highlightthickness=2, textvariable = opg_total); 
    total_Entry.grid(row = 0, column = 0)
    
    sazman_Label = Label(opg_window, text = "سهم سازمان", bg = "#234884", fg = "#ffffff", font = "Btitr 14 bold"); 
    sazman_Label.grid(row = 1, column = 1, sticky=NSEW)
    sazman_Entry = Entry(opg_window, font="Bnazanin 14", highlightcolor="#d4e4f4", highlightthickness=2, textvariable = opg_sazman); 
    sazman_Entry.grid(row = 1, column = 0)
    
    bimar_Label = Label(opg_window, text = "سهم بیمار", bg = "#234884", fg = "#ffffff", font = "Btitr 14 bold");
    bimar_Label.grid(row = 2, column = 1, sticky=NSEW)
    bimar_Entry = Entry(opg_window, font="Bnazanin 14", highlightcolor="#d4e4f4", highlightthickness=2, textvariable = opg_bimar);
    bimar_Entry.grid(row = 2, column = 0)
    
    pay_Label = Label(opg_window, text = "مبلغ پرداختی", bg = "#234884", fg = "#ffffff", font = "Btitr 14 bold");
    pay_Label.grid(row = 3, column = 1, sticky=NSEW)
    pay_Entry = Entry(opg_window, font="Bnazanin 14", highlightcolor="#d4e4f4", highlightthickness=2, textvariable = opg_pay);
    pay_Entry.grid(row = 3, column = 0)
    
    calculate_Button = Button(opg_window, text = "محاسبه", font="Btitr 14",bg = "#a3e3ec", command=opg_calculate)
    calculate_Button.grid(row = 4, column = 0, columnspan = 2)



def azmayesh_clicked():
    azmayesh_window = Toplevel(root)
    azmayesh_window.title("محسابه خسارات آزمایش")
    azmayesh_window.geometry(f"{400}x{400}+{x}+{y}")
    azmayesh_window.config(bg = "#ebecee")
    azmayesh_window.resizable(False, False)
    azmayesh_window.rowconfigure(0, weight = 1)
    azmayesh_window.rowconfigure(1, weight = 1)
    azmayesh_window.rowconfigure(2, weight = 1)
    azmayesh_window.columnconfigure(0, weight = 1)
    azmayesh_window.columnconfigure(1, weight = 1)
    azmayesh_window.protocol("WM_DELETE_WINDOW", root.destroy)


text = Label(root, text = "انتخاب نوع خسارت", bg = "#234884", fg = "#ffffff", font = "Btitr 18 bold")
text.grid(row = 0, column = 1, sticky=NSEW)

opg_Button = Button(root, text = "رادیوگرافی پانورکس و غیره", bg = "#d4e4f4", fg = "black", font="Bnazanin 18 bold", command = opg_clicked)
opg_Button.grid(row = 1, column = 1, sticky=NSEW)

azmayesh_Button = Button(root, text = "انواع آزمایش", bg = "#d4e4f4", fg = "black", font="Bnazanin 18 bold", command = azmayesh_clicked)
azmayesh_Button.grid(row = 2, column = 1, sticky=NSEW)




root.mainloop()
