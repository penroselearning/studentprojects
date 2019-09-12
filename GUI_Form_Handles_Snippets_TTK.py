from tkinter import *
from tkinter.ttk import * # Form Template
root=Tk()

# Specifies the Template Design for all the Form Handles
s=Style() # Default Theme is Default - Other Themes are Clam, Alt and Classic
s.theme_use('clam') #Code to Change the Theme

s.configure('.', font=('verdana', 14),background='lightblue') #Applies to All
s.configure('TEntry',foreground='darkblue')
s.configure('TLabel',foreground='black',background='lightblue')
s.configure('TFrame',foreground='white',background='lightblue')
s.configure('TProgressbar',background='green')
s.map('TButton',background=[('pressed','lightblue'),('active','white')],foreground=[('pressed','red'),('active','blue')])
######################################################

root.configure(background='lightblue')
root.geometry("510x600")
root.title("Penrose Learning")
root.resizable(False,False)

# Retrieve Form Data
def formdata():
    print(f'Regular Entry:  {Entry1.get()}')
    print(f'Password Entry: {Entry2.get()}')
    print(f'Radio Button:   {gender.get()}')                #Used Control Variable
    print(f'Check Button:   {check1.get()}-{check2.get()}') #Used Control Variable
    print(f'List Box:       {LB1.get(LB1.curselection())}')
    print(f'Option Menu:    {omvar.get()}')                 #Used Control Variable
    print(f'Combo Box:      {cmbvar.get()}')                # Used Control Variable
    print(f'Scale:          {scalevar.get()}')              # Used Control Variable
    print(f'Progress:       {progressvar.get()}')
    print(f'Spin Box:       {spinboxvar.get()}')
    print(f'Text Box:       {Text1.get(1.0,END)}')


# Label ****************
# URL https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Label.html
Label(root,text="Python Tkinter GUI Form Handles",background='lightblue').pack()


# Notebook *************
# URL https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Notebook.html
Notebook1=Notebook(root,width=500)
Notebook1.pack()

#Frames ******************
NewFrame = Frame(root)
Notebook1.add(NewFrame,text="GUI TKK Template ")


form_handles=['Regular Entry','Password Entry','Radio Button',
              'Check Button','List Box','Option Menu','Combo Box',
              'Scale','Progress Bar','SpinBox','Seperator','Text Editor','Button','Message Box']

r=0
for form_handle in form_handles:
    Label1 = Label(NewFrame, text=form_handle,style='TLabel')
    Label1.grid(row=r, column=0, sticky=NSEW)
    r+=1


# Entry - Visble *******************
# URL https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Entry.html
Entry1=Entry(NewFrame,style='TEntry')
Entry1.grid(row=0,column=1,columnspan=2,sticky=NSEW) #When using NSEW, it occupies the full area of the Row and Columns specified


# Entry - Password *******************
# https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Entry.html
Entry2=Entry(NewFrame,show="*") #Password Entry
Entry2.grid(row=1,column=1,columnspan=2,sticky=NSEW)


# Radio Button *******************
# https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Radiobutton.html
gender=StringVar()
gender.set('Gender')
Radio1=Radiobutton(NewFrame,text="Male",value="Male",variable=gender) #Value ensures both Radio Buttons are unique, while Variable ensures they are grouped under one category
Radio1.grid(row=2,column=1,sticky=NSEW)
Radio2=Radiobutton(NewFrame,text="Female",value="Female",variable=gender)
Radio2.grid(row=2,column=2,sticky=NSEW)



# CheckButton *******************
# https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Checkbutton.html
check1=StringVar()
Check1=Checkbutton(NewFrame,text="Male",state=ACTIVE,onvalue="Male",variable=check1) #You can add Variable and Command
Check1.grid(row=3,column=1,sticky=NSEW)

check2=StringVar()
Check2=Checkbutton(NewFrame,text="Female",state=ACTIVE,onvalue="Female",variable=check2)
Check2.grid(row=3,column=2,sticky=NSEW)



#List Box *******************
Options=['Level 1','Level 2','Level 3','Level 4']

lb1=StringVar()
lb1.set(Options)

LB1=Listbox(NewFrame,height=4,listvariable=lb1)

# Individually Adding Items in the listbox
#LB1.insert(1,"Math")
#LB1.insert(2,"Coding")
#LB1.insert(3,"Robotics")
#LB1.insert(4,"Fine Arts")
LB1.grid(row=4,column=1,columnspan=2,sticky=NSEW)



#Option Menu *******************
omvar=StringVar(NewFrame)       # Creates a String Variable that will store the Value from the Option Menu
omvar.set(Options[0])            # Will Display the first List Value within the Option Menu
#omvar.trace('w',OptionChange)    # Calls a Function when the Option Menu Value is selected

OM1=OptionMenu(NewFrame,omvar,*Options) # * Key allow the Drop Down Values to be listed one below the other
OM1.grid(row=5,column=1,columnspan=2,sticky=NSEW)



# Combo Box Widget *******************
# URL https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Combobox.html
cmbvar=StringVar(NewFrame)
cmbvar.set(Options[0])
Combo1=Combobox(NewFrame,height=10,width=25,values=Options,textvariable=cmbvar) #Height refers to number of values it will list without scroll
Combo1.grid(row=6,column=1,columnspan=2,sticky=NSEW)


def showscale(val):
    scalevar.set(round(float(val)))

# Scale  *******************
# URL https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Scale.html
#scalevar.trace('w',ScaleChange)    # Calls a Function when the Option Menu Value is selected
scalevar=IntVar()
scalevar.set(0)
Scale1=Scale(NewFrame,orient=HORIZONTAL,length=200,from_=1,to=10,command=showscale)
Scale1.grid(row=7,column=1,columnspan=2)
scalelabel=Label(NewFrame,textvariable=scalevar,background='lightblue').grid(row=7,column=3)



# Progress Bar  *******************
# URL https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Progressbar.html
progressvar=IntVar()

Progress1=Progressbar(NewFrame,orient=HORIZONTAL,length=200,maximum=1000,mode='determinate',style='TProgressbar',variable=progressvar)
Progress1.start(1)
Progress1.step(1)
Progress1.grid(row=8,column=1,columnspan=2)
progressabel=Label(NewFrame,textvariable=progressvar,background='lightblue').grid(row=8,column=3)



# Spin Box  *******************
spinboxvar=StringVar(NewFrame)       # Creates a String Variable that will store the Value from the Option Menu

SpinBox1=Spinbox(NewFrame,width=10,from_=1,to=10,increment=0.5,textvariable=spinboxvar) # Always Stores Values as Text
SpinBox1.grid(row=9,column=1,columnspan=2,sticky=NSEW)



# Seperator Widget *******************
# URL https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Separator.html
Seperator1=Separator(NewFrame,orient=HORIZONTAL)
Seperator1.grid(row=10,column=1,columnspan=2,sticky=NSEW)



# Text Editor Widget *******************
Text1=Text(NewFrame,height=5,width=25,insertborderwidth=0) #Height is measures in lines and Width is defined in characters and not Pixels
Text1.grid(row=11,column=1,columnspan=2,sticky=NSEW)



# Button Widget *******************
# URL - https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Button.html
Button1=Button(NewFrame,text="Button",style='TButton',state=ACTIVE,command=formdata) #Height is measures in lines and Width is defined in characters and not Pixels
Button1.grid(row=12,column=1,columnspan=2,sticky=NSEW)

Separator


# Message Widget *******************
# URL - https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/message.html

test = StringVar()

Message1=Message(NewFrame,text="This is a form designed by\nPenrose Learning",textvariable=test)
test.set("great")#Height is measures in lines and Width is defined in characters and not Pixels
Message1.grid(row=13,column=1,columnspan=2,sticky=NSEW)

root.mainloop()
