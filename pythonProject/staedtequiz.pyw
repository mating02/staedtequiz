from tkinter import *
from PIL import Image, ImageTk
from random import choice, randint
staedte_schwer = ['german_cities/Aachen.jpg', 'german_cities/Augsburg.jpg', 'german_cities/Bielefeld.JPG',
'german_cities/Bonn.jpg', 'german_cities/Braunschweig.jpg', 'german_cities/Chemnitz.jpg',
'german_cities/Essen.jpg', 'german_cities/Gelsenkirchen.jpg',
'german_cities/Karlsruhe.jpg', 'german_cities/Ludwigshafen.jpg', 'german_cities/Mannheim.jpg',
'german_cities/Münster.jpg', 'german_cities/Ulm.jpg', 'german_cities/Wiesbaden.jpg', 'german_cities/Wuppertal.jpg']
staedte_schwer_cop = list(staedte_schwer)

staedte_leicht = ['german_cities/Berlin.jpg', 'german_cities/Düsseldorf.jpg', 'german_cities/Frankfurt_Main.jpg',
'german_cities/Köln.jpg', 'german_cities/Hamburg.JPG', 'german_cities/München.JPG']
staedte_leicht_cop = list(staedte_leicht)

staedte_mittel = ['german_cities/Bochum.jpg', 'german_cities/Bremen.jpg',  'german_cities/Dresden.jpg',
'german_cities/Hannover.jpg', 'german_cities/Kiel.jpg', 'german_cities/Leipzig.jpg', 'german_cities/Stuttgart.jpg',
'german_cities/Nürnberg.jpg', 'german_cities/Dortmund.jpg', 'german_cities/Duisburg.jpg']
staedte_mittel_cop = list(staedte_mittel)
score = 0

def showresult():
    global score
    global staedte_leicht, staedte_mittel, staedte_schwer
    res = stadt.get()
    if res == current_image_path:
        auswahl.config(bg='green')
        score += 1
    else:
        auswahl.config(bg='red')
    fenster.after(500, changepic)



def showselected():
    selected = stadt.get()
    auswahl.config(text=selected.replace('german_cities/', '').replace('.jpg', '').replace('.JPG', ''))

def changepic():
    global score
    global staedte_leicht, staedte_mittel, staedte_schwer
    if not staedte_schwer and not staedte_mittel and not staedte_leicht:
        show_text()
        return

    liste = [staedte_leicht, staedte_mittel, staedte_schwer]
    staedte = choice(liste)   #Wähle eine Städteliste die nicht leer ist
    if not staedte:
        while not staedte:
            staedte = choice(liste)
    city = choice(staedte)
    staedte.remove(city)     # Lass die Stadt nicht wieder vorkommen
    global current_image_path
    current_image_path = city
    imgraw = Image.open(city)
    imgres = imgraw.resize((550, 300))
    imgnew = ImageTk.PhotoImage(imgres)
    ausgabe.config(image=imgnew)         #Änderung des Bildes
    ausgabe.image = imgnew
    auswahl.config(text='Welche Stadt ist das?', bg='dark blue')
    # Änderung der Radiobuttons
    while True:
        rand_schwer = choice(staedte_schwer_cop)
        rand_mittel = choice(staedte_mittel_cop)
        rand_leicht = choice(staedte_leicht_cop)
        if rand_schwer != city and rand_mittel != city and rand_leicht != city:
            break
    myauswahl = [rand_schwer, rand_mittel, rand_leicht, city]
    num1 = randint(0,3)
    radiob1.config(text=myauswahl[num1].replace('german_cities/', '').replace('.jpg', '').replace('.JPG',''),
    value=myauswahl.pop(num1))
    num2 = randint(0,2)
    radiob2.config(text=myauswahl[num2].replace('german_cities/', '').replace('.jpg', '').replace('.JPG',''),
    value=myauswahl.pop(num2))
    num3 = randint(0,1)
    radiob3.config(text=myauswahl[num3].replace('german_cities/', '').replace('.jpg', '').replace('.JPG',''),
    value=myauswahl.pop(num3))
    radiob4.config(text=myauswahl[0].replace('german_cities/', '').replace('.jpg', '').replace('.JPG',''),
    value=myauswahl[0])

def show_text():
    fenster.destroy()
    fensterneu = Tk()
    fensterneu.title('Ergebnis')
    fensterneu.configure(bg='orange')
    ueberschrift = Label(master=fensterneu, text='Städtequiz', font=("Comic Sans MS Bold", 18), fg='white', bg='orange')
    ausgabe2 = Text(master=fensterneu, fg='white', bg='orange', font=("Comic Sans MS Bold", 28), wrap=WORD,
                    height=6, width=33)
    ausgabe2.config(state=NORMAL)  # Enable the widget
    ausgabe2.delete("1.0", END)  # Clear any existing content
    if score > 24:
        ausgabe2.insert("1.0", "Du hast " + str(score) + "/32 Städten korrekt genannt! DU bist ein echter Patriot!")
    elif 12 <= score <= 24:
        ausgabe2.insert("1.0", "Du hast " + str(
            score) + "/32 Städten korrekt genannt! Ein bisschen mehr Integration schadet nicht!")
    else:
        ausgabe2.insert("1.0", "Du hast nur " + str(
            score) + "/32 Städten korrekt genannt! Vielleicht solltest du lieber auswandern!")
    ausgabe2.config(state=DISABLED)  # Disable the widget again
    ueberschrift.pack()
    ausgabe2.pack(pady=15)
    fensterneu.mainloop()

fenster = Tk()
fenster.title('Städtequiz')
fenster.configure(bg='orange')
ueberschrift = Label(master=fenster, text='Städtequiz', font=( "Comic Sans MS Bold", 18), fg='white', bg='orange')
img1raw = Image.open('german_cities/Heidelberg.jpg')
current_image_path = 'german_cities/Heidelberg.jpg'
img1res = img1raw.resize((550, 300))
img1 = ImageTk.PhotoImage(img1res)
ausgabe = Label(master=fenster, image=img1)
ausgabe.image = img1
auswahl = Label(master=fenster, bg='dark blue', fg='white', width=40, text='Welche Stadt ist das?')
centered_frame = Frame(fenster, bg='orange')
stadt = StringVar()
radiob1 = Radiobutton(centered_frame, text='Kiel', variable=stadt, value='german_cities/Kiel.jpg', command=showselected,
                      bg='orange')
radiob2 = Radiobutton(centered_frame, text='Münster', variable=stadt, value='german_cities/Münster.jpg', command=showselected,
                      bg='orange')
radiob3 = Radiobutton(centered_frame, text='Heidelberg', variable=stadt, value='german_cities/Heidelberg.jpg', command=showselected,
                      bg='orange')
radiob4 = Radiobutton(centered_frame, text='Berlin', variable=stadt, value='german_cities/Berlin.jpg', command=showselected,
                      bg='orange')
radiob4.select()
button = Button(master=fenster, text='Auswählen', command=showresult, font=('Arial', 12), bg='white')
ueberschrift.pack()
ausgabe.pack()
auswahl.pack()
centered_frame.pack()
radiob1.pack(anchor=NW, padx=10)
radiob2.pack(anchor=NW, padx=10)
radiob3.pack(anchor=NW, padx=10)
radiob4.pack(anchor=NW, padx=10)
button.pack()
fenster.mainloop()







