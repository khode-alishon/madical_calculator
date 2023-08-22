"""
this app gives the user an easy to use interface to analyze medical insurance bills

*autor ARobatjazi*
startation date: 1402/05/31

current task/state:
    define functionality for opn_clicked method        

"""


from tkinter import *

root = Tk()
root.title("محاسبه گر خسارت درمانی")

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

def opg_clicked():
    if Toplevel.winfo_exists(opg_window):
        print(1)
    opg_window = Toplevel()
    opg_window.title("محسابه خسارات پاراکلینیکی")
    opg_window.geometry(f"{400}x{400}+{x}+{y}")
    opg_window.config(bg = "#ebecee")
    opg_window.resizable(False, False)
    opg_window.rowconfigure(0, weight = 1)
    opg_window.rowconfigure(1, weight = 1)
    opg_window.rowconfigure(2, weight = 1)
    opg_window.columnconfigure(0, weight = 1)
    opg_window.columnconfigure(1, weight = 1)
    opg_window.protocol("WM_DELETE_WINDOW", root.destroy)

def azmayesh_clicked():
    azmayesh_window = Toplevel(root)
    azmayesh_window.title("محسابه خسارات آزمایش")
    azmayesh_window.geometry(f"{400}x{400}+{x}+{y}")
    azmayesh_window.config(bg = "#ebecee")
    oazmayesh_window.resizable(False, False)
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
