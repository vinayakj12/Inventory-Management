#import all the modules
from tkinter import *
from tkinter import messagebox
import os
import sys

import mysql.connector
from mysql.connector import Error
import tkinter.messagebox
import datetime
import math

date=datetime.datetime.now().date()
#temporary list like sessions
products_list=[]
product_price=[]
product_quantity=[]
product_id=[]
r = []

class Application():
    def __init__(self,master,*args,**kwargs):
        self.master=master

        self.left=Frame(master,width=700,height=768,bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=666, height=768, bg='gray')
        self.right.pack(side=RIGHT)


        #components
        self.heading=Label(self.left,text="VRANDY OIL COMPANY",font=('arial 40 bold'),fg='white',bg='black')
        self.heading.place(x=0,y=0)

        self.date_l=Label(self.right,text="Today's Date: "+str(date),font=('arial 16 bold'),bg='gray',fg='white')
        self.date_l.place(x=0,y=0)

        #table invoice=======================================================
        self.tproduct=Label(self.right,text="Products",font=('arial 18 bold'),bg='gray',fg='white')
        self.tproduct.place(x=0,y=60)

        self.tquantity = Label(self.right, text="Quantity", font=('arial 18 bold'), bg='gray', fg='white')
        self.tquantity.place(x=300, y=60)

        self.tamount = Label(self.right, text="Amount", font=('arial 18 bold'), bg='gray', fg='white')
        self.tamount.place(x=500, y=60)

        #enter stuff
        self.enterid=Label(self.left,text="Enter Product's ID",font=('arial 18 bold'),fg='white',bg='black')
        self.enterid.place(x=0,y=80)


        self.enteride=Entry(self.left,width=25,font=('arial 18 bold'),bg='lightblue')
        self.enteride.place(x=220,y=80)
        self.enteride.focus()

        #button
        self.search_btn=Button(self.left,text="Search",width=22,height=2,bg='orange',command=self.ajax)
        self.search_btn.place(x=380,y=120)
        #fill it later by the fuction ajax

        query_btn = Button(root, text="Show Records", width=22, height=2, bg='orange', command=self.query)
        query_btn.place(x=400, y=200)

        add_db = Button(root, text="Add to data", width=22,
                           height=2, bg='orange', command=self.add_to_db)
        add_db.place(x=400, y=250)

        add_db = Button(root, text="update data", width=22,
                        height=2, bg='orange', command=self.update_db)
        add_db.place(x=400, y=300)





        self.productname=Label(self.left,text="",font=('arial 27 bold'),bg='white',fg='steelblue')
        self.productname.place(x=0,y=250)

        self.pprice = Label(self.left, text="", font=('arial 27 bold'), bg='white', fg='steelblue')
        self.pprice.place(x=0, y=290)

        #total label
        self.total_l=Label(self.right,text="",font=('arial 40 bold'),bg='lightblue',fg='white')
        self.total_l.place(x=0,y=600)
    def ajax(self,*args,**kwargs):
        self.conn = mysql.connector.connect(host='localhost',
                                       database='inventory_system',
                                       user='root',
                                       password='')
        self.get_id=self.enteride.get()
        #get the product info with that id and fill i the labels above
        self.mycursor = self.conn.cursor()
        self.mycursor.execute("SELECT * FROM inventory WHERE id= %s",[self.get_id])
        self.pc = self.mycursor.fetchall()
        if self.pc:
          for self.r in self.pc:
            self.get_id=self.r[0]
            self.get_name=self.r[1]
            self.get_price=self.r[3]
            self.get_stock=self.r[2]
          self.productname.configure(text="Product's Name: " +str(self.get_name),fg='white',bg='black')
          self.pprice.configure(text="Price:RS. "+str(self.get_price),fg='white',bg='black')


        #craete the quantity and the discount label
          self.quantityl=Label(self.left,text="Enter Quantity",font=('arial 18 bold'),fg='white',bg='black')
          self.quantityl.place(x=0,y=370)

          self.quantity_e=Entry(self.left,width=25,font=('arial 18 bold'),bg='lightblue')
          self.quantity_e.place(x=190,y=370)
          self.quantity_e.focus()

        #discount
          self.discount_l = Label(self.left, text="Enter Discount", font=('arial 18 bold'),fg='white',bg='black')
          self.discount_l.place(x=0, y=410)


          self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
          self.discount_e.place(x=190, y=410)
          self.discount_e.insert(END,0)


        #add to cart button
          self.add_to_cart_btn = Button(self.left, text="Add to Cart", width=22, height=2, bg='orange',command=self.add_to_cart)
          self.add_to_cart_btn.place(x=350, y=450)

        #genrate bill and change
          self.change_l=Label(self.left,text="Given Amount",font=('arial 18 bold'),fg='white',bg='black')
          self.change_l.place(x=0,y=550)

          self.change_e=Entry(self.left,width=25,font=('arial 18 bold'),bg='lightblue')
          self.change_e.place(x=190,y=550)

          self.change_btn= Button(self.left, text="Calculate Change", width=22, height=2, bg='orange',command=self.change_func)
          self.change_btn.place(x=350, y=590)

        #geneerate bill button
          self.bill_btn = Button(self.left, text="Generate Bill", width=100, height=2, bg='red',fg='white',command=self.generate_bill)
          self.bill_btn.place(x=0, y=640)
        else:
             messagebox.showinfo("success", "Done everything smoothly")



    def add_to_db(self,*args,**kwargs):
        root.withdraw()
        db=Tk()
        
        db.geometry("1366x768+0+0")
        db.title("Add in the database")
        conn=mysql.connector.connect(host='localhost',
                                        database='inventory_system',
                                        user='root',
                                        password='')
        mycursor = conn.cursor()
        mycursor.execute("SELECT Max(id) from inventory")
        result = mycursor.fetchall()
        for r in result:
            id=r[0]
            
        class Database:
            


            def __init__(self,master,*args,**kwargs):
                self.master=master
                self.heading=Label(master,text="Add in the database",font=('arial 40 bold'),fg='steelblue')
                self.heading.place(x=400,y=0)


                #lables  for the window
                self.name_l=Label(master,text="Enter Product Name",font=('arial 18 bold'))
                self.name_l.place(x=0,y=70)

                self.stock_l=Label(master,text="Enter Stocks",font=('arial 18 bold'))
                self.stock_l.place(x=0,y=120)

                self.cp_l = Label(master, text="Enter Cost Price ", font=('arial 18 bold'))
                self.cp_l.place(x=0, y=170)


                #enteries for window

                self.name_e=Entry(master,width=25,font=('arial 18 bold'))
                self.name_e.place(x=380,y=70)

                self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
                self.stock_e.place(x=380, y=120)

                self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
                self.cp_e.place(x=380, y=170)

                #button to add to the database
                self.btn_add=Button(master,text='Add to Database',width=25,height=2,bg='steelblue',fg='white',command=self.get_items)
                self.btn_add.place(x=520,y=220)

                self.btn_clear=Button(master,text="Clear All Fields",width=18,height=2,bg='red',fg='white',command=self.clear_all)
                self.btn_clear.place(x=350,y=220)

                self.btn_exit = Button(
                  master, text="EXIT", width=18, height=2, bg='red', fg='white', command=self.dest)
                self.btn_exit.place(x=350, y=280)

                

                #text box for the log
                self.tbBox=Text(master,width=60,height=18)
                self.tbBox.place(x=750,y=70)
                self.tbBox.insert(END,"ID has reached up to:"+str(id))

                self.master.bind('<Return>', self.get_items)
                self.master.bind('<Up>', self.clear_all)

            def dest(self, *args, **kwargs):
              db.destroy()
              root.deiconify()


            def get_items(self, *args, **kwargs):
            # get from entries
              self.name = self.name_e.get()
              self.stock = self.stock_e.get()
              self.cp = self.cp_e.get()

              # dynamic entries
              if self.name == '' or self.stock == '' or self.cp == '':
                  tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
              else:
                  mycursor.execute("INSERT INTO inventory (name, stock, price) VALUES(%s,%s,%s)",[self.name,self.stock,self.cp])
                  conn.commit()
                  # textbox insert
                  self.tbBox.insert(END, "\n\nInseted " + str(self.name) + " into the database with the quantity of " + str(self.stock))
                  tkinter.messagebox.showinfo("Success", "Successfully added to the database")


            def clear_all(self, *args, **kwargs):
              num = id + 1
              self.name_e.delete(0, END)
              self.stock_e.delete(0, END)
              self.cp_e.delete(0, END)
        b = Database(db)
             

      

    def update_db(self,*args,**kwargs):
        root.withdraw()
        up=Tk()
        
        up.geometry("1366x768+0+0")
        up.title("update database")
        conn=mysql.connector.connect(host='localhost',
                                       database='inventory_system',
                                       user='root',
                                       password='')
        mycursor = conn.cursor()
        mycursor.execute("SELECT Max(id) from inventory")
        result = mycursor.fetchall()
        for r in result:
            id=r[0]

        class Database:
            def __init__(self,master,*args,**kwargs):
                self.master=master
                self.heading=Label(master,text="Update to the databse",font=('arial 40 bold'),fg='steelblue')
                self.heading.place(x=400,y=0)

                #label and entry for id
                self.id_le=Label(master,text="Enter ID",font=('arial 18 bold'))
                self.id_le.place(x=0,y=70)

                self.id_leb=Entry(master,font=('arial 18 bold'),width=10)
                self.id_leb.place(x=380,y=70)

                self.btn_search=Button(master,text="search",width=15,height=2,bg='orange',command=self.search)
                self.btn_search.place(x=550,y=70)

                #lables  for the window
                self.name_l=Label(master,text="Enter Product Name",font=('arial 18 bold'))
                self.name_l.place(x=0,y=120)

                self.stock_l=Label(master,text="Enter Stocks",font=('arial 18 bold'))
                self.stock_l.place(x=0,y=170)

                self.cp_l = Label(master, text="Enter Cost Price ", font=('arial 18 bold'))
                self.cp_l.place(x=0, y=220)


                #enteries for window

                self.name_e=Entry(master,width=25,font=('arial 18 bold'))
                self.name_e.place(x=380,y=120)

                self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
                self.stock_e.place(x=380, y=170)

                self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
                self.cp_e.place(x=380, y=220)


                #button to add to the database
                self.btn_add=Button(master,text='Update Database',width=25,height=2,bg='steelblue',fg='white',command=self.update)
                self.btn_add.place(x=520,y=300)

                self.btn_exit = Button(
                    master, text="EXIT", width=18, height=2, bg='red', fg='white', command=self.destr)
                self.btn_exit.place(x=520, y=340)



                #text box for the log
                self.tbBox=Text(master,width=60,height=18)
                self.tbBox.place(x=750,y=70)
                self.tbBox.insert(END,"ID has reached up to:"+str(id))

            def destr(self, *args, **kwargs):
              up.destroy()
              root.deiconify()

            def search(self, *args, **kwargs):
                mycursor.execute("SELECT * FROM inventory WHERE id=%s",[self.id_leb.get()])
                result = mycursor.fetchall()
                for r in result:
                    self.n1 = r[1]  # name
                    self.n2 = r[2]  # stock
                    self.n3 = r[3]  # cp
                conn.commit()

                #inster into the enteries to update
                self.name_e.delete(0,END)
                self.name_e.insert(0, str(self.n1))

                self.stock_e.delete(0, END)
                self.stock_e.insert(0, str(self.n2))

                self.cp_e.delete(0, END)
                self.cp_e.insert(0, str(self.n3))

            def update(self,*args,**kwargs):
                self.u1=self.name_e.get()
                self.u2 = self.stock_e.get()
                self.u3 = self.cp_e.get()


                mycursor.execute("UPDATE  inventory SET name=%s,stock=%s,price=%s WHERE id=%s",[self.u1,self.u2,self.u3,self.id_leb.get()])
                conn.commit()
                tkinter.messagebox.showinfo("Success","Update Database successfully")
        b = Database(up)
        

    def add_to_cart(self,*args,**kwargs):
        self.quantity_value=int(self.quantity_e.get())

        if  self .quantity_value >int(self.get_stock):
            tkinter.messagebox.showinfo("Error","Not that any products in our stock.")
        else:
            #calculate the price first
            self.final_price=(float(self.quantity_value) * float(self.get_price))-(float(self.discount_e.get()))
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            self.x_index=0
            self.y_index=100
            self.counter=0
            for self.p in products_list:
                self.tempname=Label(self.right,text=str(products_list[self.counter]),font=('arial 18 bold'),bg='gray',fg='white')
                self.tempname.place(x=0,y=self.y_index)
                self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 18 bold'), bg='gray', fg='white')
                self.tempqt.place(x=300, y=self.y_index)
                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 18 bold'), bg='gray', fg='white')
                self.tempprice.place(x=500, y=self.y_index)

                self.y_index+=40
                self.counter+=1


                #total confugure
                self.total_l.configure(text="Total : Rs. "+str(sum(product_price)),bg='gray',fg='white')
                #delete
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.add_to_cart_btn.destroy()
                #autofocus to the enter id
                self.enteride.focus()
                self.quantityl.focus()
                self.enteride.delete(0,END)

    def change_func(self,*args,**kwargs):
        self.amount_given=float(self.change_e.get())
        self.our_total=float(sum(product_price))

        self.to_give=self.amount_given-self.our_total

        #label change
        self.c_amount=Label(self.left,text="Change: Rs. "+str(self.to_give),font=('arial 18 bold'),fg='red',bg='black')
        self.c_amount.place(x=0 ,y=600)

    def query(self,*args,**kwargs):
      root.withdraw()
      show=Tk()
      show.title('Show A Record')

      # show.geometry("500x800")

      conn = mysql.connector.connect(host='localhost',
                                     database='inventory_system',
                                     user='root',
                                     password='')


      c = conn.cursor()
      c.execute("SELECT *, id FROM inventory")
      i = 0
      for data in c:
        for j in range(len(data)-1):
            e = Label(show, width=20, text=data[j],
                      borderwidth=2, relief='ridge', anchor="w", font=('arial 15'), fg='white', bg='black')
            e.grid(row=i, column=j)
            #e.insert(END, data[j])
        i = i+1
        
      c.close()
      def dest():  
        show.destroy()
        root.deiconify()

      back = Button(show, text="EXIT", width=22,
                         height=2, bg='orange', command=dest)
      back.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
	   

            
                           
        

    def generate_bill(self,*args,**kwargs):
        self.mycursor.execute("SELECT * FROM inventory WHERE id=%s",[self.get_id])
        self.pc = self.mycursor.fetchall()
        for r in self.pc:
            self.old_stock=r[2]
        for i in products_list:
            for r in self.pc:
                self.old_stock = r[2]
            self.new_stock=int(self.old_stock) - int(self.quantity_value)
            #updating the stock
            self.mycursor.execute("UPDATE inventory SET stock=%s WHERE id=%s",[self.new_stock,self.get_id])
            self.conn.commit()

            #inster into transcation
            self.mycursor.execute("INSERT INTO transaction (product_name,quantity,amount,date) VALUES(%s,%s,%s,%s)",[self.get_name,self.quantity_value,self.get_price,date])
            self.conn.commit()
            print("Decreased")

        tkinter.messagebox.showinfo("success","Done everything smoothly")

     

            



root=Tk()
Application(root)
root.geometry("1366x768+0+0")
root.title("Inventory Management System(oil company)")
root.mainloop()
