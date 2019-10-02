from tkinter import *
from crontab import *

job_list = []

def add():
    
    pin = pin_entry.get()
    month_on = month_entry_on.get()
    day_on = day_entry_on.get()
    hour_on = hour_entry_on.get()
    minute_on = minute_entry_on.get()
    month_off = month_entry_off.get()
    day_off = day_entry_off.get()
    hour_off = hour_entry_off.get()
    minute_off = minute_entry_off.get()
    
    sub_list = [pin, month_on, day_on, hour_on, minute_on,month_off, day_off, hour_off, minute_off]
    job_list.append(sub_list)
    print(len(job_list))
    print(job_list)
   
    text_display.insert(END, "Light number "+ str(pin)+ " is set for "+ str(month_on)+ "/"+ str(day_on)+" at "+ str(hour_on)+ ":"+ str(minute_on)+"\n")
            
   
## chron
## command_string_on = 'python_led_on_off_1.py ' + pin + " on"
## command_string_off = 'python_led_on_off_1.py ' + pin + " off"
##    cron = CronTab(user='pi')
##    job = cron.new(command='python LED_Bar.py on (pin)')
##    job.minute.every(1)
##    cron.write()


def modify():
    print("modify")
    ## ask for pin, delete job, add new job


def delete():
    
    ## on button click, ask which pin.  Delete all jobs for that pin
    print("delete")


def quit_program():
    main.destroy()
    ## add comment to jobs, delete all jobs with comment on quit.


main = Tk()
main.title = "My Vacation Timer"
frame = Frame(main)
date_on_1 = StringVar()
main.geometry('650x600')
# create widgets

title_label = Label(main, text="Vacation Timer")
on_label = Label(main, text="On")
pin_label = Label(main, text="Pin")
off_label = Label(main, text="Off")

month_label = Label(main, text="Month")
day_label = Label(main, text="Day")
hour_label = Label(main, text="Hour")
minute_label = Label(main, text="Minute")

month_entry_on = Entry(main, width=12)
day_entry_on = Entry(main, width=12)
month_entry_off = Entry(main, width=12)
day_entry_off = Entry(main, width=12)
pin_entry = Entry(main, width=2)
hour_entry_on = Entry(main, width=12)
minute_entry_on = Entry(main, width=12)
hour_entry_off = Entry(main, width=12)
minute_entry_off = Entry(main, width=12)

text_display = Text(main)

btn_add = Button(text="Add", command=add)
btn_modify = Button(text="Modify", command=modify)
btn_delete = Button(text="Delete", command=delete)
btn_exit = Button(text="Quit", command=quit_program)

# add widgets to grid
title_label.grid(row=0, column=1,columnspan=4,pady=10)
on_label.grid(row=5, column=0,padx=10)
pin_label.grid(row=3, column=0)
off_label.grid(row=6, column=0,padx=10)
month_label.grid(row=4, column=1)
day_label.grid(row=4, column=2)
hour_label.grid(row=4, column=3)
minute_label.grid(row=4, column=4)

month_entry_on.grid(row=5, column=1,padx=10,pady=5)
day_entry_on.grid(row=5, column=2,padx=10,pady=5)
month_entry_off.grid(row=6, column=1,padx=10)
day_entry_off.grid(row=6, column=2,padx=10)
hour_entry_on.grid(row=5, column=3,padx=10,pady=5)
minute_entry_on.grid(row=5, column=4,padx=10,pady=5)
hour_entry_off.grid(row=6, column=3,padx=10,pady=5)
minute_entry_off.grid(row=6, column=4,padx=10)
pin_entry.grid(row=3, column=1,padx=10,pady=10,sticky='w')

text_display.grid(row=15, column=1, columnspan=4, pady=40)

btn_add.grid(row=14, column=1)
btn_delete.grid(row=14, column=2)
btn_modify.grid(row=14, column=3)
btn_exit.grid(row=14, column=4)


main.mainloop()