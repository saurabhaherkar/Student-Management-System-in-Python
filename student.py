import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter import *
import sys
import sqlite3

con = sqlite3.connect('student.db')
cur = con.cursor()

class Student:
    def __init__(self, root):
        self.root = root

#----------------All Variables-----------------------------------
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        self.lblheading = Label(self.root, text='Student Management System', font=('times new roman', 20,'bold'), bg='yellow', fg='black', height=2, relief=GROOVE)
        self.lblheading.pack(side=TOP, fill=X)

        self.frame1 = Frame(self.root, bd='2', bg='crimson', width=450, height=600, relief=RIDGE)
        self.frame1.place(x=30, y=70)

        self.frame2 = Frame(self.frame1, bg='white', width=400, height=50)
        self.frame2.place(x=30, y=500)

        self.frame3 = Frame(self.root, bd=2, bg='crimson', width=830, height=600, relief=RIDGE)
        self.frame3.place(x=490, y=70)

#---------------------------------------------Labels and Entries---------------------------------------------
        self.lblman_stud = Label(self.frame1, text='Manage Student', font=('times new roman', 18, 'bold'), bg='crimson', fg='white')
        self.lblman_stud.place(x=150, y=30)

        self.lblroll = Label(self.frame1, text='Roll No', font=('times new roman', 18, 'bold'), bg='crimson', fg='white', justify=LEFT)
        self.lblroll.place(x=40, y=80)
        self.txtroll = Entry(self.frame1, width=35, textvariable=self.Roll_No_var)
        self.txtroll.place(x=200, y=85)

        self.lblname = Label(self.frame1, text='Name', font=('times new roman', 18, 'bold'), bg='crimson', fg='white', justify=LEFT)
        self.lblname.place(x=40, y=120)
        self.txtname = Entry(self.frame1, width=35, relief=GROOVE, textvariable=self.name_var)
        self.txtname.place(x=200, y=125)

        self.lblemail = Label(self.frame1, text='Email', font=('times new roman', 18, 'bold'), bg='crimson', fg='white', justify=LEFT)
        self.lblemail.place(x=40, y=160)
        self.txtemail = Entry(self.frame1, width=35, relief=GROOVE, textvariable=self.email_var)
        self.txtemail.place(x=200, y=165)

        self.lblgender = Label(self.frame1, text='Gender', font=('times new roman', 18, 'bold'), bg='crimson', fg='white', justify=LEFT)
        self.lblgender.place(x=40, y=200)
        self.comgender = ttk.Combobox(self.frame1, font=('times new roman', 12), width=17, textvariable=self.gender_var)
        self.comgender['values'] = ('Male', 'Female', 'Other')
        self.comgender.set('Male')
        self.comgender.place(x=200, y=205)

        self.lblcontact = Label(self.frame1, text='Contact No', font=('times new roman', 18, 'bold'), bg='crimson', fg='white', justify=LEFT)
        self.lblcontact.place(x=40, y=240)
        self.txtcontact = Entry(self.frame1, width=35, relief=GROOVE, textvariable=self.contact_var)
        self.txtcontact.place(x=200, y=245)

        self.lbldob = Label(self.frame1, text='D.O.B', font=('times new roman', 18, 'bold'), bg='crimson', fg='white', justify=LEFT)
        self.lbldob.place(x=40, y=280)
        self.txtdob = Entry(self.frame1, width=35, relief=GROOVE, textvariable=self.dob_var)
        self.txtdob.place(x=200, y=285)

        self.lbladdr = Label(self.frame1, text='Address', font=('times new roman', 18, 'bold'), bg='crimson', fg='white', justify=LEFT)
        self.lbladdr.place(x=40, y=320)
        self.txtaddr = Text(self.frame1, bd='2', font=('times new roman', 12), width=20, height=4, relief=GROOVE)
        self.txtaddr.place(x=200, y=325)

#--------------------------------------------------Buttons---------------------------------------------
        self.btnadd = Button(self.frame2, text='Add', font=('times new roman', 15, 'bold'), bg='indigo', fg='white', width=5, command=self.add_student)
        self.btnadd.place(x=5, y=5)

        self.btnupdate = Button(self.frame2, text='Update', font=('times new roman', 15, 'bold'), bg='indigo', fg='white', width=5, command=self.update)
        self.btnupdate.place(x=85, y=5)

        self.btndelete = Button(self.frame2, text='Delete', font=('times new roman', 15, 'bold'), bg='indigo', fg='white', width=5, command=self.delete)
        self.btndelete.place(x=165, y=5)

        self.btnclear = Button(self.frame2, text='Clear', font=('times new roman', 15, 'bold'), bg='indigo', fg='white', width=5, command=self.clear)
        self.btnclear.place(x=245, y=5)

        self.btnexit = Button(self.frame2, text='Exit', font=('times new roman', 15, 'bold'), bg='indigo', fg='white', width=5, command=self.exit)
        self.btnexit.place(x=325, y=5)

        self.lblsearch = Label(self.frame3, text='Search By', font=('times new roman', 18, 'bold'), bg='crimson', fg='white')
        self.lblsearch.place(x=10, y=10)
        self.comsearch = ttk.Combobox(self.frame3, font=('arial', 12), width=15, textvariable=self.search_by)
        self.comsearch['values'] = ('Select Option', 'Roll_No', 'Name', 'Contact')
        self.comsearch.set('Select Option')
        self.comsearch.place(x=135, y=15)

        self.txtDemo = Entry(self.frame3, width=25, relief=GROOVE, textvariable=self.search_txt)
        self.txtDemo.place(x=310, y=15)

        self.btnsearch = Button(self.frame3, text='Search', font=('times new roman', 11, 'bold'), width=15, command=self.search)
        self.btnsearch.place(x=500, y=15)

        self.btnshow = Button(self.frame3, text='Show All', font=('times new roman', 11, 'bold'), width=15, command=self.fetch_all)
        self.btnshow.place(x=650, y=15)

        self.listBox = Listbox(self.frame3, bd=2, relief=RIDGE, bg='crimson')
        self.listBox.place(x=10, y=70, width=790, height=500)

        self.xscrollbar = Scrollbar(self.listBox, orient=HORIZONTAL)
        self.yscrollbar = Scrollbar(self.listBox, orient=VERTICAL)
        self.stud_table = ttk.Treeview(self.listBox, columns=('roll', 'name', 'email', 'gender', 'contact', 'dob', 'address'), xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)
        self.xscrollbar.pack(side=BOTTOM, fill=X)
        self.yscrollbar.pack(side=RIGHT, fill=Y)
        self.xscrollbar.config(command=self.stud_table.xview)
        self.yscrollbar.config(command=self.stud_table.yview)
        self.stud_table.heading('roll', text='Roll No')
        self.stud_table.heading('name', text='Name')
        self.stud_table.heading('email', text='Email')
        self.stud_table.heading('gender', text='Gender')
        self.stud_table.heading('contact', text='Contact')
        self.stud_table.heading('dob', text='DOB')
        self.stud_table.heading('address', text='Address')
        self.stud_table['show'] = 'headings'
        self.stud_table.column('roll', width=110)
        self.stud_table.column('name', width=110)
        self.stud_table.column('email', width=110)
        self.stud_table.column('gender', width=110)
        self.stud_table.column('contact', width=110)
        self.stud_table.column('dob', width=110)
        self.stud_table.column('address', width=110)
        self.stud_table.pack(fill=BOTH, expand=1)
        self.stud_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_all()

    def add_student(self):
        cur.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?)", (self.Roll_No_var.get(), self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.contact_var.get(), self.dob_var.get(), self.txtaddr.get('1.0', END)))
        self.fetch_all()
        self.clear()
        con.close()

    def fetch_all(self):
        cur.execute('SELECT * FROM student')
        rows = cur.fetchall()
        if len(rows) != 0:
            self.stud_table.delete(*self.stud_table.get_children())
            for i in rows:
                self.stud_table.insert('', END, values=i)
            con.commit()

    def clear(self):
        self.Roll_No_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.gender_var.set('')
        self.contact_var.set('')
        self.dob_var.set('')
        self.txtaddr.delete('1.0', END)

    def get_cursor(self, e):
        cursor_row = self.stud_table.focus()
        content = self.stud_table.item(cursor_row)
        row = content['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txtaddr.delete('1.0', END)
        self.txtaddr.insert(END, row[6])

    def update(self):
        cur.execute("UPDATE student SET name=?, email=?, gender=?, contact=?, dob=?, address=? WHERE roll_no=?", (self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.contact_var.get(), self.dob_var.get(), self.txtaddr.get('1.0', END), self.Roll_No_var.get()))
        con.commit()
        self.fetch_all()
        self.clear()

    def delete(self):
        cur.execute('DELETE FROM student WHERE roll_no=?', self.Roll_No_var.get())
        con.commit()
        self.fetch_all()
        self.clear()

    def search(self):
        cur.execute('SELECT * FROM student WHERE '+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.stud_table.delete(*self.stud_table.get_children())
            for i in rows:
                self.stud_table.insert('', END, values=i)
        con.commit()

    def exit(self):
        msg = tkinter.messagebox.askyesno('Warning', 'Do you want to close the project')
        if msg == True:
            quit()



if __name__ == '__main__':
    root = Tk()
    root.title('Student Management System')
    b = Student(root)
    root.geometry('1350x1000')
    root.config(bg='indigo')
    root.mainloop()