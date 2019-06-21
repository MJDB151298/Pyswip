from tkinter import *
from tkinter import scrolledtext
from pyswip import Prolog


def main():
    prolog = Prolog()
    prologfile = open("prolog_example.pl", "a+")

    openwindow(prolog, prologfile)


def openwindow(prolog, prologfile):
    window = Tk()
    window.title("Test de prolog")

    fatherlabel = Label(window, text="Escriba el nombre del padre: ")
    fatherlabel.grid(column=0, row=0)
    fathertext = Entry(window, width=10)
    fathertext.grid(column=1, row=0)

    sonlabel = Label(window, text="Escriba el nombre del hijo/a: ")
    sonlabel.grid(column=2, row=0)
    sontext = Entry(window, width=10)
    sontext.grid(column=3, row=0)

    def clicked():
        prolog.assertz("progenitor("+fathertext.get()+","+sontext.get()+")")
        print("progenitor("+fathertext.get()+","+sontext.get()+")")
        prologfile.write("progenitor("+fathertext.get()+","+sontext.get()+")."+'\n')
        fathertext.delete('0', END)
        fathertext.update()
        sontext.delete('0', END)
        sontext.update()
        fathertext.focus

    btn = Button(window, text="Guardar", command=clicked)
    btn.grid(column=5, row=0)

    #No se esta usando para nada en este momento
    father_son_list = scrolledtext.ScrolledText(window, width=40, height=10)
    father_son_list.grid(column=3, row=3)

    window.geometry('1000x500')
    window.mainloop()


main()
