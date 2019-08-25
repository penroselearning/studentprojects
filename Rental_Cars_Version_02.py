from tkinter import *
from tkinter.ttk import *
#from oauth2client.service_account import ServiceAccountCredentials
import os
#import gspread
import smtplib
from datetime import datetime
#from gtts import gTTS
#import playsound
from tkinter import filedialog
from email.message import EmailMessage

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

basedir = os.path.abspath(os.path.dirname(__file__))
data_json = basedir + '/GearsCRS.json'
#creds = ServiceAccountCredentials.from_json_keyfile_name(data_json, scope)
#client = gspread.authorize(creds)

#workbook1 = client.open("GearsCRS")
#w1 = workbook1.worksheet("Sheet1")
#all_records = w1.get_all_values()
# sort = sorted(all_records, key=lambda row: row[2], reverse=True)
#rows = list(all_records)

#tts = gTTS(text='Hello Welcome to Gears Car Rental Service, Please Pick an Option To begin the rental process', lang='en')
#tts.save("greeting.mp3")

#playsound.playsound("greeting.mp3",True)

class RentalCars():

    def __init__(self):
        self.screen = screen

        types = ['Rent A 2 Wheeler', 'Rent A 4 Wheeler', 'Rent An 18 Wheeler', 'Exit']

        s = Style()
        s.configure('.', font=('verdana', 9), background='lightblue')
        s.map('TButton', background=[('pressed', 'black'), ('active', 'white')],
              foreground=[('pressed', 'black'), ('active', 'black')])
        screen.configure(background='lightblue')
        screen.title("Gears Car Rental Service")
        Label(screen, text='Welcome to Gears Car Rental Service').grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lb1 = StringVar()
        self.lb1.set(types)
        self.LB1 = Listbox(screen, height=4, listvariable=self.lb1)
        self.LB1.grid(row=4, column=0, columnspan=2, sticky=NSEW)

        Button1 = Button(screen, text="Next", style='TButton', state=ACTIVE, command=self.vehicle)
        Button1.grid(row=6, column=0, columnspan=2, sticky=NSEW)

    def vehicle(self):

        def vehicle_selection(tw):

            def rental_period():

                def rate_calculation():

                    def pay():

                        def payment_method1():

                            def fileupload():
                                screen.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                                             filetypes=(
                                                                                 ("pdf files", "*.pdf"),
                                                                                 ("all files", "*.*")))
                                t.set(screen.filename)

                                print(cust_email.get())
                                print(selected_vehicle)
                                # w1.append_row([cust_email.get(), selected_vehicle, datetime.now()])

                            def email():

                                today = datetime.now()

                                date = today.date()

                                gmail_user = 'dhruvtreddy@gmail.com'
                                gmail_password = 'Blaze2019'

                                msg = EmailMessage()
                                msg['Subject'] = 'Gears Car Rental Service'
                                msg['To'] = cust_email.get()
                                msg['From'] = 'Gears Car Rental Service'

                                body = f'Your Car Rental Service order has been placed on {date}, you can pick it up at our Barsha Outlet and your order Reference Number is 47, Thank You for using Gears Car Rental Service'

                                msg.set_content(body)

                                start = 0
                                for x in range(len(screen.filename)):
                                    if screen.filename[x] == '/':
                                        start = x

                                stop = screen.filename.find('.pdf')

                                pdfname = screen.filename[start + 1:stop:1]

                                with open(f'{pdfname}.pdf', 'rb') as f:
                                    file_data = f.read()
                                    file_name = f.name

                                msg.add_attachment(file_data, maintype='text', subtype='text', filename=file_name)

                                try:
                                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                                        smtp.login(gmail_user, gmail_password)
                                        smtp.send_message(msg)
                                    Message1 = Message(screen, text="Email Sent")
                                    Message1.grid(row=25, column=0, columnspan=2, sticky=NSEW)
                                except:
                                    Message40 = Message(screen, text="Error")
                                    Message40.grid(row=25, column=0, columnspan=2, sticky=NSEW)



                            if LB1.get(LB1.curselection()) == 'Credit Card':
                                Label(screen, text="Card Number", background='lightblue').grid(row=17, column=0,
                                                                                               columnspan=1,
                                                                                               sticky=NSEW)
                                Entry1 = Entry(screen, style='TEntry')
                                Entry1.grid(row=17, column=1, columnspan=1, sticky=NSEW)
                                Label(screen, text="Security Code", background='lightblue').grid(row=18, column=0,
                                                                                                 columnspan=1,
                                                                                                 sticky=NSEW)
                                Entry2 = Entry(screen, show="*")  # Password Entry
                                Entry2.grid(row=18, column=1, columnspan=1, sticky=NSEW)
                                Button21 = Button(screen, text="Submit", style='TButton', state=ACTIVE, command=email)
                                Button21.grid(row=24, column=0, columnspan=2, sticky=NSEW)
                                Message3 = Message(screen,
                                                   text="You Can Pickup Your Vehicle at our Gears Car Rental Outlet located in Barsha, a receipt and reference number will be sent to you via email. Thank You")
                                Message3.grid(row=19, column=1, columnspan=2, sticky=NSEW)
                                Label(screen, text="Email Address", background='lightblue').grid(row=21, column=0,
                                                                                                 columnspan=1,
                                                                                                 sticky=NSEW)
                                cust_email = Entry(screen, style='TEntry')
                                cust_email.grid(row=21, column=1, columnspan=1, sticky=NSEW)
                                btn1 = Button(screen, text="Drivers License", command=fileupload)
                                btn1.grid(row=22, column=0, columnspan=2, sticky=NSEW)
                                t = StringVar()
                                Message50 = Message(screen, textvariable=t)
                                Message50.grid(row=23, column=0, columnspan=2, sticky=NSEW)


                            elif LB1.get(LB1.curselection()) == 'Cash':
                                Message2 = Message(screen,
                                                   text="You Can Pickup and Pay For Your Vehicle at our Gears Car Rental Outlet located in Barsha, an order receipt and reference number will be sent to you via email. Thank You")
                                Message2.grid(row=15, column=1, columnspan=2, sticky=NSEW)
                                Button22 = Button(screen, text="Submit", style='TButton', state=ACTIVE, command=email)
                                Button22.grid(row=19, column=0, columnspan=2, sticky=NSEW)
                                Label(screen, text="Email Address", background='lightblue').grid(row=16, column=0,
                                                                                                 columnspan=1,
                                                                                                 sticky=NSEW)
                                cust_email = Entry(screen, style='TEntry')
                                cust_email.grid(row=16, column=1, columnspan=1, sticky=NSEW)
                                btn1 = Button(screen, text="Browse", command=fileupload)
                                btn1.grid(row=17, column=0, columnspan=2, sticky=NSEW)
                                t = StringVar()
                                Message50 = Message(screen, textvariable=t)
                                Message50.grid(row=18, column=0, columnspan=2, sticky=NSEW)



                        payment = ['Credit Card', 'Cash']
                        Label(screen, text="Payment Method", background='lightblue').grid(row=15, column=0,
                                                                                          columnspan=1, sticky=NSEW)
                        lb1 = StringVar()
                        lb1.set(payment)
                        LB1 = Listbox(screen, height=2, listvariable=lb1)
                        LB1.grid(row=15, column=1, columnspan=2, sticky=NSEW)
                        Button19 = Button(screen, text="Next", style='TButton', state=ACTIVE, command=payment_method1)
                        Button19.grid(row=16, column=0, columnspan=2, sticky=NSEW)


                    selected_vehicle = cmbvar.get()
                    start = cmbvar.get().find('|  ')

                    stop = cmbvar.get().find('AED')

                    pricetwo = cmbvar.get()[start + 2:stop:1]

                    Message1 = Message(screen, text=f'Final Price is {int(pricetwo) * spinboxvar.get()} AED')
                    Message1.grid(row=13, column=0, columnspan=2, sticky=NSEW)

                    Button20 = Button(screen, text="Next", style='TButton', state=ACTIVE, command=pay)
                    Button20.grid(row=14, column=0, columnspan=2, sticky=NSEW)

                Label(screen, text='No. of Days').grid(row=9, column=0, columnspan=1, sticky=NSEW)
                spinboxvar = IntVar(screen)
                SpinBox1 = Spinbox(screen, width=10, from_=1, to=1000, increment=1, textvariable=spinboxvar)
                SpinBox1.grid(row=9, column=1, columnspan=1, sticky=NSEW)
                Button5 = Button(screen, text="Next", style='TButton', state=ACTIVE, command=rate_calculation)
                Button5.grid(row=10, column=0, columnspan=2, sticky=NSEW)

            displaytwo = lambda d: f'{d[0]}  |  {str(d[1])}AED'
            tw_copy = list(map(displaytwo, tw))

            Label(screen, text='Vehicle').grid(row=7, column=0, columnspan=1, sticky=NSEW)
            cmbvar = StringVar(screen)
            Combo1 = Combobox(screen, height=10, width=25, values=tw_copy, textvariable=cmbvar)
            Combo1.grid(row=7, column=1, columnspan=1, sticky=NSEW)
            Button4 = Button(screen, text="Next", style='TButton', state=ACTIVE, command=rental_period)
            Button4.grid(row=8, column=0, columnspan=2, sticky=NSEW)


        if self.LB1.get(self.LB1.curselection()) == "Rent A 2 Wheeler":
            twowheeler = [['Motor Bike', 60], ['Road Bike', 30], ['Mountain Bike', 30]]
            vehicle_selection(twowheeler)
            # email()
        elif self.LB1.get(self.LB1.curselection()) == "Rent A 4 Wheeler":
            fourwheeler = [['4 Door Salon Car', 100], ['2 Door Salon Car', 150], ['Pickup Truck', 125], ['SUV', 110],
                           ['Van', 130]]
            vehicle_selection(fourwheeler)
            # email()
        elif self.LB1.get(self.LB1.curselection()) == "Rent An 18 Wheeler":
            eighteenwheeler = [['Mercedes Eighteen Wheeler', 200], ['MAN Eighteen Wheeler', 175],
                               ['ISUZU Eighteen Wheeler', 175]]
            vehicle_selection(eighteenwheeler)
            # email()
        elif self.LB1.get(self.LB1.curselection()) == "Exit":
            exit()

if __name__ == '__main__':
    screen = Tk()
    app = RentalCars()
    screen.mainloop()