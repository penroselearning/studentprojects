from tkinter import *
screen=Tk()

screen.title("Measurement Convertor Software")
screen.configure(background="lightblue")

def convert():
    cm = float(inches.get())*2.54
    result.set(f'{cm} cm')

Label(text="Inches to Centimetre Convertor",bg="lightblue").pack()

inches=Entry(screen)
inches.pack()

Button(text="Convert",command=convert).pack()

result=IntVar()
Label(text="",textvariable=result,bg="lightblue").pack()

screen.mainloop()