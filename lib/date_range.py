from tkinter import *
from tkcalendar import *
from datetime import datetime


class DateRange:

    def __init__(self):

        self.root = Tk()
        self.root.title('Date Picker')
        self.root.geometry("1024x768")
        self.start_date = ''
        self.end_date = ''

        self.start_cal = Calendar(self.root, selectmode="day", year=2020, month=1, day=1)
        self.start_cal.pack(pady=20)

        self.end_cal = Calendar(self.root, selectmode="day", year=2020, month=12, day=31)
        self.end_cal.pack(pady=20)

        self.start_button = Button(self.root, text="Confirm Start Date", command=self.get_start_date)
        self.start_button.pack(pady=20, padx=2)

        self.end_button = Button(self.root, text="Confirm End Date", command=self.get_end_date)
        self.end_button.pack(pady=20, padx=2)

        self.start_label = Label(self.root, text=f'Start Date: {self.start_date}')
        self.start_label.pack(pady=20)

        self.end_label = Label(self.root, text=f'End Date: {self.end_date}')
        self.end_label.pack(pady=20)

        self.exit_button = Button(self.root, text="Confirm and Exit", command=self.root.destroy)
        self.exit_button.pack(pady=20)

        self.root.mainloop()

    def get_start_date(self):
        self.start_label.config(textvariable=self.start_cal.get_date(), text=f'Start Date: {self.start_cal.get_date()}')
        self.start_date = self.start_label['textvariable']
        self.start_date = str(int(datetime.strptime(str(self.start_date), '%m/%d/%y').timestamp()))

    def get_end_date(self):
        self.end_label.config(textvariable=self.end_cal.get_date(), text=f'Start Date: {self.end_cal.get_date()}')
        self.end_date = self.end_label['textvariable']
        self.end_date = str(int(datetime.strptime(str(self.end_date), '%m/%d/%y').timestamp()))

        








