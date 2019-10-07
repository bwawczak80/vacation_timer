from tkinter import *
from crontab import *
from tkinter import OptionMenu

job_list = []

def add():
    list_box.delete(0,END)
    pin = pin_var.get()
    month_on = month_on_var.get()
    day_on = day_on_var.get()
    hour_on = hour_on_var.get()
    minute_on = minute_on_var.get()
    month_off = month_off_var.get()
    day_off = day_off_var.get()
    hour_off = hour_off_var.get()
    minute_off = minute_off_var.get()
    sub_list = [pin, month_on, day_on, hour_on, minute_on, month_off, day_off, hour_off, minute_off]
    job_list.append(sub_list)

    for job in job_list:
        list_box.insert(END, str(job[0]) + " ON: "+str(job[1])+"/"+str(job[2])+" "+str(job[3])+":"
                        + str(job[4])+"Pin "+str(job[0]) + " OFF: "+str(job[5])+"/"+str(job[6])+" "+str(job[7])+":"
                        + str(job[8]))

        
    cron = CronTab(user='pi')
    command_string_on = 'python led_on_off_1.py ' + str(sub_list[0]) + " on"
    command_string_off = 'python led_on_off_1.py ' + str(sub_list[0]) + " off"

    
    job_on = cron.new(command=command_string_on, comment='jobs')
    job_off = cron.new(command=command_string_off, comment='jobs')
    job_on.setall(sub_list[4], sub_list[3], sub_list[2], sub_list[1])
    job_off.setall(sub_list[8], sub_list[7], sub_list[6], sub_list[5])
    cron.write()


def modify():
    x = list_box.get(list_box.curselection())
    
    # Tried to use string indices to populate optionBox with the selection
    # The index changes based on the date.  Couldn't find a solution to this.


def delete():
    
    # same problem as modify function.  Currently deletes all jobs.
    list_box.delete(0,END)
    cron = CronTab(user='pi')
    cron.remove_all(comment='jobs')
    cron.write()
    
def quit_program():
    cron = CronTab(user='pi')
    cron.remove_all(comment='jobs')
    cron.write()
    main.destroy()
    
main = Tk()
frame = Frame(main)
date_on_1 = StringVar()
main.geometry('400x500')
month_on_var = IntVar(main)
day_on_var = IntVar(main)
hour_on_var = IntVar(main)
minute_on_var = IntVar(main)
month_off_var = IntVar(main)
day_off_var = IntVar(main)
hour_off_var = IntVar(main)
minute_off_var = IntVar(main)
pin_var = IntVar(main)

# create widgets

title_label = Label(main, text="Vacation Timer")
on_label = Label(main, text="On")
pin_label = Label(main, text="Pin")
off_label = Label(main, text="Off")
month_label = Label(main, text="Month")
day_label = Label(main, text="Day")
hour_label = Label(main, text="Hour")
minute_label = Label(main, text="Minute")

month_on_var.set(1) # initial value
day_on_var.set(1)
hour_on_var.set(1)
minute_on_var.set(1)
month_off_var.set(1)
day_off_var.set(1)
hour_off_var.set(1)
minute_off_var.set(1)
pin_var.set(17)

month_entry_on = OptionMenu(main, month_on_var, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
day_entry_on = OptionMenu(main, day_on_var, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                          22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
month_entry_off = OptionMenu(main, month_off_var, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
day_entry_off = OptionMenu(main, day_off_var, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                           22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
pin_entry = OptionMenu(main, pin_var, 17, 18, 27, 22, 23, 24, 25, 2, 3, 8)
hour_entry_on = OptionMenu(main, hour_on_var, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                           22, 23)
minute_entry_on = OptionMenu(main, minute_on_var, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                             21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
                             44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59)
hour_entry_off = OptionMenu(main, hour_off_var, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23)
minute_entry_off = OptionMenu(main, minute_off_var, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                              20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
                              42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59)


list_box = Listbox(main, width=40)
btn_add = Button(text="Add", command=add)
btn_modify = Button(text="Modify", command=modify)
btn_delete = Button(text="Delete", command=delete)
btn_exit = Button(text="Quit", command=quit_program)

# add widgets to grid
title_label.grid(row=0, column=1, columnspan=4, pady=10)
on_label.grid(row=5, column=0, padx=10)
pin_label.grid(row=3, column=0)
off_label.grid(row=6, column=0, padx=10)
month_label.grid(row=4, column=1)
day_label.grid(row=4, column=2)
hour_label.grid(row=4, column=3)
minute_label.grid(row=4, column=4)
month_entry_on.grid(row=5, column=1, padx=10, pady=5)
day_entry_on.grid(row=5, column=2, padx=10, pady=5)
month_entry_off.grid(row=6, column=1, padx=10)
day_entry_off.grid(row=6, column=2, padx=10)
hour_entry_on.grid(row=5, column=3, padx=10, pady=5)
minute_entry_on.grid(row=5, column=4, padx=10, pady=5)
hour_entry_off.grid(row=6, column=3, padx=10, pady=5)
minute_entry_off.grid(row=6, column=4, padx=10)
pin_entry.grid(row=3, column=1, padx=10, pady=10, sticky='w')
list_box.grid(row=15, column=1, columnspan=6, pady=40)
btn_add.grid(row=14, column=1)
btn_delete.grid(row=14, column=2)
btn_modify.grid(row=14, column=3)
btn_exit.grid(row=14, column=4)

main.mainloop()
