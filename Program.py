from tkinter import *
okno = Tk()
okno.geometry("420x250")
okno.title("Manager zadań")
lista = open("Lista_Zadan","a+")
lista.close()

#Panel
panedwindow = PanedWindow(okno, orient=HORIZONTAL, relief=SUNKEN)
panedwindow.pack(fill=BOTH, expand=True)
#Ramki
frame1 = Frame(panedwindow,relief=SUNKEN,borderwidth=2, bg="white")
frame2 = Frame(panedwindow,relief=SUNKEN,borderwidth=2)
frame3 = Frame(panedwindow,relief=SUNKEN,borderwidth=2)
panedwindow.add(frame1)
panedwindow.add(frame2)
panedwindow.add(frame3)
#FUNKCJE
def pokaż():
    lista_zd_ok = Tk()
    lista_zd_ok.title("Oto lista twoich zadań")
    lista_zd_ok.geometry("300x300")
    lista = open("Lista_Zadan","r")
    for i,line in enumerate(lista.readlines()):
        Label(lista_zd_ok,text=line).grid(row=i,column=0)
    lista.close()
def dodawanie():
    zadanie = pole.get()
    lista = open("Lista_Zadan", "a+")
    lista.write(zadanie+"\n")
    lista.close()

def usuwanie():
    zadanie = pole2.get()
    with open("Lista_Zadan", "r") as f:
        lines = f.readlines()
    with open("Lista_Zadan", "w") as f:
        for line in lines:
            if line.strip("\n") != zadanie:
                f.write(line)

#OKNO LISTY ZADAŃ
etykieta_listy = Label(frame1,text="Lista zadań:").grid(row=0,column=0)
Button(frame1,text="Pokaż całą\nlistę zadań",command=pokaż).grid(row=1,column=0)

#DODAWANIE
etykieta_dodawania = Label(frame2,text="Dodawanie").grid(row=0,column=0)
Label(frame2,text="Wpisz w okienko\nnazwę zadania i kliknij\nprzycisk dodaj").grid(row=1,column=0,columnspan=2)
pole = Entry(frame2)
pole.grid(row=2,column=0)
Button(frame2,text="dodaj",command=dodawanie).grid(row=2,column=1)

#USUWANIE
etykieta_usuwania = Label(frame3,text="Usuwanie").grid(row=0,column=0)
Label(frame3,text="Wpisz nazwę zadania,\n które chcesz usunąć.\nnastępnie kliknij przycisk usuń").grid(row=1,column=0,columnspan=2)
pole2 = Entry(frame3)
pole2.grid()
Button(frame3,text="usuń",command=usuwanie).grid(row=2,column=1)

okno.mainloop()