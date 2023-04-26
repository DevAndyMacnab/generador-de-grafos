from tkinter import Tk
from app.mainView import Principal

if __name__=="__main__":
    
    wPrincipal=Tk()
    application=Principal(wPrincipal)
    wPrincipal.mainloop()