from tkinter import   *
import datetime

print(datetime.datetime.now())

def date_time():
    time = datetime.datetime.now()
    hr   = time.strftime('%I')
    mi   = time.strftime('%M')
    sec  = time.strftime('%S')
    am   = time.strftime("%p")
    date  = time.strftime("%d")
    month= time.strftime("%m")
    year   = time.strftime("%y")
    day  = time.strftime("%a")
     
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_MON.config(text=month)
    lab_ye.config(text=year)
    lab_day.config(text=day)
    lab_hr.after(200,date_time)
    
clock =Tk()
clock.title('clock by nancy ')
clock.geometry('1000x500')
clock.config(bg='#E52B50')

##***time***##

lab_hr=Label(clock,text="00",font=('Helvetica',55,"bold","italic"),bg='#FFBF00',fg="White")
lab_hr.place(x=120,y=45,height=100,width=95)
    
lab_hr_txt=Label(clock,text="HOUR",font=('Helvetica  ',20,"bold","italic"),bg='blue',fg="White")
lab_hr_txt.place(x=120,y=190,height=40,width=95)

lab_min=Label(clock,text="00",font=('Helvetica',55,"bold","italic"),bg='#9966CC',fg="White")
lab_min.place(x=340,y=45,height=100,width=95)

lab_min_txt=Label(clock,text="MIN.",font=('Helvetica',20,"bold","italic"),bg='blue',fg="White")
lab_min_txt.place(x=340,y=190,height=40,width=95)

lab_sec=Label(clock,text="00",font=('Helvetica',55,"bold","italic"),bg='#50c878',fg="White")
lab_sec.place(x=560,y=45,height=100,width=95)

lab_sec_txt=Label(clock,text="SEC.",font=('Helvetica',20,"bold","italic"),bg='#02a4d3',fg="White")
lab_sec_txt.place(x=560,y=190,height=40,width=95)


lab_am=Label(clock,text="00",font=('Helvetica',40,"bold","italic"),bg='#c8a2c8',fg="White")
lab_am.place(x=780,y=45,height=100,width=95)

lab_am_txt=Label(clock,text="AM/PM",font=('Helvetica',20,"bold","italic"),bg='#000080',fg="White")
lab_am_txt.place(x=780,y=190,height=40,width=95)

######Date*******###

lab_date=Label(clock,text="00",font=('Helvetica',55,"bold","italic"),bg='#ffd700',fg="White")
lab_date.place(x=120,y=270,height=100,width=95)
    
lab_date_txt=Label(clock,text="DATE",font=('Helvetica',20,"bold","italic"),bg='blue',fg="White")
lab_date_txt.place(x=120,y=410,height=40,width=95)

lab_MON=Label(clock,text="00",font=('Helvetica',55,"bold","italic"),bg='#009900',fg="White")
lab_MON.place(x=340,y=270,height=100,width=95)

lab_MON_txt=Label(clock,text="MONTH",font=('Helvetica',15,"bold","italic"),bg='blue',fg="White")
lab_MON_txt.place(x=340,y=410,height=40,width=95)

lab_ye=Label(clock,text="00",font=('Helvetica',55,"bold","italic"),bg='#1c39bb',fg="White")
lab_ye.place(x=560,y=270,height=100,width=95)

lab_ye_txt=Label(clock,text="YEAR",font=('Helvetica',20,"bold","italic"),bg='blue',fg="White")
lab_ye_txt.place(x=560,y=410,height=40,width=95)

lab_day=Label(clock,text="00",font=('Helvetica',35,"bold","italic"),bg='#c3cde6',fg="White")
lab_day.place(x=780,y=270,height=100,width=95)

lab_day_txt=Label(clock,text="DAY",font=('Helvetica',20,"bold","italic"),bg='blue',fg="White")
lab_day_txt.place(x=780,y=410,height=40,width=95)


date_time()

clock.mainloop()
