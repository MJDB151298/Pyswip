from tkinter import *
from tkinter import scrolledtext
from pyswip import Prolog


def main():
    prolog = Prolog()
    prolog.consult("prolog_example.pl")
    

    # Para poder hacer un query en prolog
    # for search in prolog.query("progenitor(X,Y)"):
    #print(search["X"] + " is the father of " + search["Y"])

    openwindow(prolog)


def openwindow(prolog):
    window = Tk()
    window.title("Consulta de progenitores")

    fatherlabel = Label(window, text="Escriba el nombre del padre: ")
    fatherlabel.grid(column=0, row=0)
    fathertext = Entry(window, width=20)
    fathertext.grid(column=1, row=0)

    sonlabel = Label(window, text="Escriba el nombre del hijo/a: ")
    sonlabel.grid(column=2, row=0)
    sontext = Entry(window, width=20)
    sontext.grid(column=3, row=0)

    def save():
        prologfile = open("prolog_example.pl", "a+")
        prolog.assertz("progenitor("+fathertext.get()+","+sontext.get()+")")
        print("progenitor("+fathertext.get()+","+sontext.get()+")")
        prologfile.write(
            "progenitor("+fathertext.get()+","+sontext.get()+")."+'\n')
        fathertext.delete('0', END)
        fathertext.update()
        sontext.delete('0', END)
        sontext.update()
        fathertext.focus
        prologfile.close()

    def search_children():
        progenitor = searchfathertxt.get()
        children = list(prolog.query("progenitor(%s ,Child)" % progenitor))
        for child in children:
            children_list.insert(
                INSERT, child["Child"] + " es descendiente de " + progenitor + "\n")

    def search_progenitor():
        children = searchsontxt.get()
        progenitores = list(prolog.query("progenitor(Progrenitor , %s)" % children))
        for progenitor in progenitores:
            progenitor_list.insert(
                INSERT, progenitor["Progrenitor"] + " es progenitor de " + children + "\n")

    btn = Button(window, text="Guardar", command=save)
    btn.grid(column=5, row=0)

    searchfatherlabel = Label(window, text="Busque los hijos de una persona")
    searchfatherlabel.grid(column=0, row=6)
    searchfathertxt = Entry(window, width=20)
    searchfathertxt.grid(column=1, row=6)
    searchfatherbutton = Button(window, text="Buscar", command=search_children)
    searchfatherbutton.grid(column=2, row=6)

    searchsonlabel = Label(window, text="Busque al padre de una persona")
    searchsonlabel.grid(column=3, row=6)
    searchsontxt = Entry(window, width=20)
    searchsontxt.grid(column=4, row=6)
    searchsonbutton = Button(window, text="Buscar", command=search_progenitor)
    searchsonbutton.grid(column=5, row=6)

    # No se esta usando para nada en este momento
    children_list = scrolledtext.ScrolledText(window, width=40, height=10)
    children_list.grid(column=1, row=12)

    progenitor_list = scrolledtext.ScrolledText(window, width=40, height=10)
    progenitor_list.grid(column=4, row=12)

    window.geometry('1000x500')
    window.mainloop()


main()
