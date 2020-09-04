
from  tkinter import  *
from  tkinter import  ttk
from  tkinter import  messagebox
from  DbConnectClass import DBConnect
class ListTickets:
    def __init__(self):
           self._dbConnect=DBConnect()
           self._root=Tk()
           tv=ttk.Treeview(self._root)
           tv.pack()
           tv.heading("#0",text="ID")
           tv.configure(column=('Name','IDP','Gender','Residence'))
           tv.heading("Name",text="Full Name")
           tv.heading("IDP",text="IDP")
           tv.heading("Gender",text="Gender")
           tv.heading("Residence",text="Residence")
           cursor=self._dbConnect.ListTickets()
           for row in cursor:
               tv.insert('','end','#{}'.format(row["ID"]),text=row["ID"])
               tv.set('#{}'.format(row["ID"]),'Name',row["Name"])
               tv.set('#{}'.format(row["ID"]),'IDP',row["IDP"])
               tv.set('#{}'.format(row["ID"]),'Gender',row["Gender"])
               tv.set('#{}'.format(row["ID"]),'Residence',row["Residence"])
               # print("ID:{},Name:{},IDP:{},Gender:{},Comment:{}".format(row["ID"],row["Name"],row["IDP"],row["Gender"],row["Residence"]))



           self._root.mainloop()

