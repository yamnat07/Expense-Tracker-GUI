from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
from datetime import datetime
# Main Window and Expense Tracker Label
window=Tk()
window.title("Expense Tracker")
window.state("zoomed")
window.configure(bg="#1E1E1E")
def exit_fullscreen(event=None):
    window.attributes("-fullscreen",False)
window.bind("<Escape>",exit_fullscreen)
def enter_fullscreen(event=None):
    window.attributes("-fullscreen",True)
window.bind("<Alt-Return>",enter_fullscreen)    
exp_lbl=Label(window,text="Expense Tracker",font=("Segoe UI", 24, "bold", "underline"),fg="#E8EAED",bg="#1E1E1E")
exp_lbl.pack(side=TOP)

# Date Label and Its values comboboxes
date_lbl=Label(window,text="Date(Date/Month/Year):",font=("Segoe UI", 14, "bold"),fg="#E8EAED",bg="#1E1E1E")
date_lbl.place(x=100,y=150)
days=ttk.Combobox(window,state="readonly",justify="center")
days['values']=[str(i) for i in range(1,32)]
days.place(x=327,y=157,width=50)

# Month combobox
months=ttk.Combobox(window,state="readonly",justify="center")
months['values']=["January", "February", "March", "April", "May", "June",
 "July", "August", "September", "October", "November", "December"]
months.place(x=389,y=157,width=120)

# Years combobox
years=ttk.Combobox(window,state="readonly",justify="center")
years['values']=[str(year) for year in range(2026,2048)]
years.place(x=520,y=157)
# Category Label and Its values combobox
categories_lbl=Label(window,text="Category:",font=("Segoe UI", 14, "bold"),fg="#E8EAED",bg="#1E1E1E")
categories_lbl.place(x=230,y=230)
categories=ttk.Combobox(window,state="readonly",font="Arial 13",justify="center")
categories['values']=["Food", "Travel", "Shopping", "Bills", "Entertainment",
 "Education", "Health", "Rent", "Groceries", "Utilities",
 "Subscriptions", "Personal Care", "Other"]
categories.place(x=323,y=235,height=30)

# Amount Label and Its Entry widget
amount_lbl=Label(window,text="Amount (₹):",font=("Segoe UI", 14, "bold"),fg="#E8EAED",bg="#1E1E1E")
amount_lbl.place(x=207,y=290)
amount_widget=Entry(window)
amount_widget.place(x=323,y=297,height=26)

# Description label and its widget
description_lbl=Label(window,text="Description:",font=("Segoe UI", 14, "bold"),fg="#E8EAED",bg="#1E1E1E")
description_lbl.place(x=208,y=340)
description_widget=Text(window,width=30,height=5)
description_widget.place(x=323,y=349)
# Expense class
class Expense():
    def __init__(self,sel_date,sel_category,give_amount,give_des):
        self.date=sel_date
        self.category=sel_category
        self.amount=give_amount
        self.description=give_des
# Function taking values, validating them and inserting them in the table
def get_values():
    pattern=r"^[1-9]\d*$"
    result=re.fullmatch(pattern,amount_widget.get().strip())
    if days.get()=="" and months.get()=="" and years.get()=="" and categories.get()=="" and amount_widget.get().strip()=="" and description_widget.get("1.0",END).strip()=="":
        messagebox.showwarning("Warning","All fields must be filled!")
        return
    elif (days.get()=="" and months.get()=="" and years.get()=="")or days.get()=="" or months.get()=="" or years.get()=="":
        messagebox.showwarning("Warning","Please fill all Date related fields!")
        return
    chosen_date=f"{days.get()}/{months.get()}/{years.get()}"
    try:
        datetime.strptime(chosen_date,'%d/%B/%Y')
    except ValueError:
        messagebox.showwarning("Warning","Please enter a valid Date!")
        return    
    if categories.get()=="":
        messagebox.showwarning("Warning","Please enter a category!")
        return    
    elif description_widget.get("1.0",END).strip()=="":
        messagebox.showwarning("Warning","Please provide a short description!")
        return
    elif amount_widget.get().strip()=="":
        messagebox.showwarning("Warning","Please Enter an amount for the expense!")
        return 
    elif not result:
        messagebox.showwarning("Warning","Please Enter a valid amount!")
        return
    else:
        sel_category=categories.get()
        sel_date=chosen_date
        give_amount=int(amount_widget.get().strip())
        give_des=description_widget.get("1.0",END).strip()
        exp_obj=Expense(sel_date,sel_category,give_amount,give_des)
        def save():
            with open("expense_data.txt","a") as file:
                file.write(f"Date={sel_date}\nCategory={sel_category}\nAmount Spend={give_amount}\nDesc.={give_des.replace("\n"," ")}\n\n")
            table.insert("",END,values=(exp_obj.date,exp_obj.category,exp_obj.amount,exp_obj.description.replace("\n"," ")))
            messagebox.showinfo("Success","Data Added Successfully.")
            categories.set("")
            amount_widget.delete(0,END)
            description_widget.delete("1.0",END)
        save()
            
add_button=Button(window,text="Add Expense",bg="#2E7D32",font=("Segoe UI", 20, "bold"),relief="raised",borderwidth=2,fg="#FFFFFF",activebackground="#43A047",command=get_values)
add_button.place(x=565,y=540)
# Table and its configurations
style=ttk.Style()
style.theme_use("clam")
style.configure("Treeview",background="#2B2B2B",foreground="#E8EAED",fieldbackground="#2B2B2B",rowheight=28,font=("Segoe UI",11))
style.configure("Treeview.Heading",background="#2E7D32",foreground="#FFFFFF",font=("Segoe UI",11,"bold"))
style.map("Treeview",background=[("selected","#43A047")],foreground=[("selected","#FFFFFF")])
style.configure("Vertical.TScrollbar",background="#3A3A3A",troughcolor="#1E1E1E",arrowcolor="#E8EAED")
table=ttk.Treeview(window,columns=("Date","Category","Amount","Description"),show="headings",height=10)
table.heading("Date",text="Date")
table.heading("Category",text="Category")
table.heading("Amount",text="Amount(Rs.)")
table.heading("Description",text="Description")
table.column("Date",width=120,anchor="center")
table.column("Category",width=120,anchor="center")
table.column("Amount",width=100,anchor="center")
table.column("Description",width=240)
table.place(x=720,y=150)

# Scrollbar for table
scrollbar=ttk.Scrollbar(window,orient="vertical",command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
scrollbar.place(in_=table,relx=1.0,rely=0,relheight=1.0,anchor="nw")
window.mainloop()