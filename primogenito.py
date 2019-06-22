from tkinter import *
from tkinter import scrolledtext
from pyswip import Prolog


def main():
    prolog = Prolog()
    prolog.consult("prolog_example.pl")
    prologfile = open("prolog_example.pl", "a+")

    #Para poder hacer un query en prolog
    #for search in prolog.query("progenitor(X,Y)"):
        #print(search["X"] + " is the father of " + search["Y"])

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
    father_son_list.grid(column=4, row=10)


    searchfatherlabel = Label(window, text="Busque al padre/madre")
    searchfatherlabel.grid(column=0, row=6)
    searchfathertxt = Entry(window, width=10)
    searchfathertxt.grid(column=1, row=6)
    searchfatherbutton = Button(window, text="Buscar")
    searchfatherbutton.grid(column=2, row=6)

    searchsonlabel = Label(window, text="Busque al hijo/a")
    searchsonlabel.grid(column=4, row=6)
    searchsontxt = Entry(window, width=10)
    searchsontxt.grid(column=5, row=6)
    searchsonbutton = Button(window, text="Buscar")
    searchsonbutton.grid(column=6, row=6)

    window.geometry('1000x500')
    window.mainloop()


main()
