from tkinter import *
principal = Tk()
listbox = Listbox(principal)
for item in ["Jose", "Luis", "Miguel", "Erik", "Abel", "Heidi", "Cris", "Laura"]:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de los nombres de las personas")
label.pack()
principal.mainloop()

