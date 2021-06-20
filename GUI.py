from tkinter import *
from tkinter import ttk
import mysql.connector

# Establishing connection to the database
mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="factory")
mycursor = mydb.cursor()

gui = Tk()  # Creating window
gui.title("Factory")
gui.geometry('1920x1080+0+0')

firstframe = Frame(gui)
startframe = Frame(gui)
empsearchframe = Frame(gui)
customersearchframe = Frame(gui)
deleteframe = Frame(gui)
inventoryframe = Frame(gui)
manufactureframe = Frame(gui)
rawframe = Frame(gui)
addframe = Frame(gui)
sellframe = Frame(gui)
sellheadframe = Frame(gui)
checkorderframe = Frame(gui)
avsalframe = Frame(gui)

firstdestroy = 0
startdestroy = 0
empsearchdestroy = 0
customersearchdestroy = 0
deletedestroy = 0
inventorydestroy = 0
manufacturedestroy = 0
rawdestroy = 0
adddestroy = 0
selldestroy = 0
checkorderdestroy = 0
avsaldestroy = 0


def first():
    global firstframe
    firstframe = Frame(gui)

    global firstdestroy
    firstdestroy = 1

    headingframe = Frame(firstframe)

    heading = Label(headingframe, text="FACTORY SIMULATOR", fg="brown", font='Helvetica 40 bold italic', bg="lightblue",
                    relief=RAISED)

    loginframe = Frame(firstframe)

    loginbutton = Button(loginframe, text="Begin", font="time 15", command=startwindow,
                         activebackground="grey")  # Program starts once "Begin" button is clicked

    creator1 = Label(headingframe,
                     text="Project Created by:\n\nRushang Phira (E011)\nTarran Pidugu (E012)\nShaurya Rawat (E018)",
                     font="times 20 italic")

    creator1.grid(row=1)
    heading.grid(row=0, column=0, padx=100, pady=80)
    headingframe.grid()
    loginframe.grid(row=2, column=0)
    loginbutton.grid(row=3, padx=20, pady=50)
    firstframe.grid()
    firstframe.place(relx=0.5, rely=0.3, anchor=CENTER)


def startwindow():  # Home button leads to this page. Contains code to destroy all frames as soon as this page is
    # reached
    # This page then leads to the next page with no input/outputs, making it a sort of a dummy page.

    global startframe
    global firstdestroy
    global startdestroy
    global empsearchdestroy
    global customersearchdestroy
    global deletedestroy
    global inventorydestroy
    global manufacturedestroy
    global rawdestroy
    global adddestroy
    global selldestroy
    global checkorderdestroy
    global avsaldestroy

    startframe = Frame(gui)
    startdestroy = 1

    # Next few lines check which page we are reaching here from. Then the frames corresponding to those pages only
    # are destroyed.

    if firstdestroy == 1:
        firstframe.destroy()
        firstdestroy = 0
    elif empsearchdestroy == 1:
        empsearchframe.destroy()
        empsearchdestroy = 0
    elif customersearchdestroy == 1:
        customersearchframe.destroy()
        customersearchdestroy = 0
    elif deletedestroy == 1:
        deleteframe.destroy()
        deletedestroy = 0
    elif inventorydestroy == 1:
        inventoryframe.destroy()
        inventorydestroy = 0
    elif manufacturedestroy == 1:
        manufactureframe.destroy()
        manufacturedestroy = 0
    elif rawdestroy == 1:
        rawframe.destroy()
        rawdestroy = 0
    elif adddestroy == 1:
        addframe.destroy()
        adddestroy = 0
    elif selldestroy == 1:
        sellframe.destroy()
        sellheadframe.destroy()
        selldestroy = 0
    elif checkorderdestroy == 1:
        checkorderframe.destroy()
        checkorderdestroy = 0
    elif avsaldestroy == 1:
        avsalframe.destroy()
        avsaldestroy = 0

    login()  # Leads to the next page, which presents user with all the choices.


def login():  # Function for begin command, executed once "Begin" button is clicked

    global startdestroy

    if startdestroy == 1:  # Destroying all existing frames before proceeding
        startdestroy = 0
        startframe.destroy()

    def search():  # Function for searching

        def emp():  # Function for Employee search

            global empsearchframe  # Frame within which all widgets are contained in the employee search page.
            global empsearchdestroy

            empsearchframe = Frame(gui)
            empsearchdestroy = 1  # Setting this to 1 means that when we click the home button, this page gets

            # destroyed.

            def detail2():  # Function to display employee

                uid = searchentry.get()  # Stores ID of employee
                label1.destroy()
                searchentry.destroy()
                searchbutton.destroy()

                mycursor.execute("select EmployeeID from employee where EmployeeID = ('{}')".format(uid))
                checking = (str(mycursor.fetchall()))[2:-3]

                if checking.isdigit():  # Checking if record exists
                    detailframe = Frame(empsearchframe)
                    detailframe.grid(row=0, column=0, pady=50)

                    displayframe = Frame(empsearchframe)
                    displayframe.grid(row=0, column=1, pady=50)

                    detaillabel1 = Label(detailframe, text="Employee ID: ", font="times 14")
                    detaillabel1.grid(row=0, sticky=E)

                    detaillabel2 = Label(detailframe, text="Name: ", font="times 14")
                    detaillabel2.grid(row=1, sticky=E)

                    detaillabel3 = Label(detailframe, text="Salary: ", font="times 14")
                    detaillabel3.grid(row=2, sticky=E)

                    detailID = Label(displayframe, text="", font="times 14 ")
                    mycursor.execute(
                        "select EmployeeID from employee where EmployeeID = ('{}')".format(uid))  # Fetching data
                    data1 = mycursor.fetchall()
                    detailID.config(text=data1)
                    detailID.grid(row=0, sticky=W)

                    detailname = Label(displayframe, text="", font="times 14")
                    mycursor.execute(
                        "select EmployeeName from employee where EmployeeID = ('{}')".format(uid))  # Fetching data
                    data2 = (str(mycursor.fetchall()))[3:-4]
                    detailname.config(text=data2)
                    detailname.grid(row=1, sticky=W)

                    detailsal = Label(displayframe, text="", font="times 14")
                    mycursor.execute("select Salary from employee where "
                                     "EmployeeID = ('{}')".format(uid))  # Fetching data
                    data3 = (str(mycursor.fetchall()))[2:-3]
                    detailsal.config(text=data3)
                    detailsal.grid(row=2, sticky=W)
                else:
                    failabel = Label(empsearchframe, text="Entry does not exist", font="times 15")
                    failabel.grid()

                back = Button(empsearchframe, text="Home", command=startwindow)
                back.grid(pady=30, row=2, column=0)

            # Destroying all existing frames before proceeding
            searchframe.destroy()
            search1.destroy()
            search2.destroy()

            empsearchframe.grid(padx=100)
            label1 = Label(empsearchframe, text="Enter unique ID of the Employee", font="times 15")
            label1.grid(padx=100, pady=20)
            searchentry = Entry(empsearchframe)
            searchentry.grid(row=1, column=0)
            searchbutton = Button(empsearchframe, text="Show Details", command=detail2, font="times 10")
            searchbutton.grid(row=2, column=0, pady=50)
            empsearchframe.place(relx=0.5, rely=0.3, anchor=CENTER)

        def cmer():  # Function for Customer search

            global empsearchframe
            global empsearchdestroy
            empsearchframe = Frame(gui)

            empsearchdestroy = 1

            def detail1():
                uid = searchentry.get()
                label1.destroy()
                searchentry.destroy()
                searchbutton.destroy()

                mycursor.execute("select CustomerID from customer where CustomerID = ('{}')".format(uid))
                checking = (str(mycursor.fetchall()))[2:-3]
                if checking.isdigit():  # Checking if record exists
                    detailframe = Frame(empsearchframe)
                    detailframe.grid(row=0, column=0, pady=50)

                    displayframe = Frame(empsearchframe)
                    displayframe.grid(row=0, column=1, pady=50)

                    detaillabel1 = Label(detailframe, text="Customer ID: ", font="times 14")
                    detaillabel1.grid(row=0, sticky=E)

                    detaillabel2 = Label(detailframe, text="Name: ", font="times 14")
                    detaillabel2.grid(row=1, sticky=E)

                    detaillabel3 = Label(detailframe, text="City: ", font="times 14")
                    detaillabel3.grid(row=2, sticky=E)

                    detaillabel4 = Label(detailframe, text="Phone: ", font="times 14")
                    detaillabel4.grid(row=3, sticky=E)

                    detaillabel5 = Label(detailframe, text="Balance: ", font="times 14")
                    detaillabel5.grid(row=4, sticky=E)

                    detailID = Label(displayframe, text="", font="times 14 ")
                    mycursor.execute(
                        "select CustomerID from customer where CustomerID = ('{}')".format(uid))  # Fetching data
                    data1 = mycursor.fetchall()
                    detailID.config(text=data1)
                    detailID.grid(row=0, sticky=W)

                    detailname = Label(displayframe, text="", font="times 14")
                    mycursor.execute(
                        "select CustomerName from customer where CustomerID = ('{}')".format(uid))  # Fetching data
                    data2 = (str(mycursor.fetchall()))[3:-4]
                    detailname.config(text=data2)
                    detailname.grid(row=1, sticky=W)

                    detailcity = Label(displayframe, text="", font="times 14")
                    mycursor.execute("select City from customer where CustomerID = ('{}')".format(uid))  # Fetching data
                    data3 = (str(mycursor.fetchall()))[3:-4]
                    detailcity.config(text=data3)
                    detailcity.grid(row=2, sticky=W)

                    detailphone = Label(displayframe, text="", font="times 14")
                    mycursor.execute("select Phone from customer where "
                                     "CustomerID = ('{}')".format(uid))  # Fetching data
                    data4 = mycursor.fetchall()
                    detailphone.config(text=data4)
                    detailphone.grid(row=3, sticky=W)

                    detailbal = Label(displayframe, text="", font="times 14")
                    mycursor.execute("select Balance from customer where "
                                     "CustomerID = ('{}')".format(uid))  # Fetching data
                    data5 = mycursor.fetchall()
                    detailbal.config(text=data5)
                    detailbal.grid(row=4, sticky=W)

                else:
                    failabel = Label(empsearchframe, text="Entry does not exist", font="times 15")
                    failabel.grid()

                back = Button(empsearchframe, text="Home", command=startwindow)
                back.grid(pady=30, row=2, column=0)

            # Destroying all existing frames before proceeding
            searchframe.destroy()
            search1.destroy()
            search2.destroy()

            label1 = Label(empsearchframe, text="Enter unique ID of the Customer", font="times 15")
            label1.grid(padx=100, pady=20)
            searchentry = Entry(empsearchframe)
            searchentry.grid(row=1, column=0)
            searchbutton = Button(empsearchframe, text="Show Details", command=detail1, font="times 14")
            searchbutton.grid(row=2, column=0, pady=50)
            empsearchframe.grid(padx=100)
            empsearchframe.place(relx=0.5, rely=0.3, anchor=CENTER)

        # Destroying all frames before proceeding
        choiceframe.destroy()
        mainframe.destroy()

        searchframe = Frame(gui)
        searchframe.grid(row=0, column=0)
        searchtable = Label(searchframe, text="Choose a table to search from", font="times 30")
        searchtable.grid(padx=100, pady=50)
        search1 = Button(searchframe, text="Search Employee", command=emp, font="times 15")
        search2 = Button(searchframe, text="Search Customer", command=cmer, font="times 15")
        search1.grid(row=1, column=0)
        search2.grid(row=2, column=0, pady=40)
        searchframe.place(relx=0.5, rely=0.3, anchor=CENTER)

    def delete():
        def cmer():  # Function for Customer delete
            def delete1():
                uid = searchentry.get()
                label1.destroy()
                searchentry.destroy()
                searchbutton.destroy()

                mycursor.execute("select CustomerID from customer where CustomerID = ('{}')".format(uid))
                checking = (str(mycursor.fetchall()))[2:-3]

                if checking.isdigit():  # Checking if record exists
                    mycursor.execute("delete from customer where CustomerID = ('{}')".format(uid))
                    mydb.commit()
                    dellab = Label(deleteframe, text="Entry Deleted", font="times 14")
                    dellab.grid(row=3, pady=20, padx=50)
                else:
                    failabel = Label(deleteframe, text="Entry does not exist", font="times 15")
                    failabel.grid()

            label1 = Label(deleteframe, text="Enter unique ID of the Customer", font="times 15")
            label1.grid(padx=100, pady=20)
            searchentry = Entry(deleteframe)
            searchentry.grid(row=1, column=0)
            searchbutton = Button(deleteframe, text="Delete Details", command=delete1, font="times 15")
            searchbutton.grid(row=2, column=0, pady=50)

            back = Button(deleteframe, text="Home", command=startwindow)
            back.grid(row=4, column=0, pady=30)

        global deleteframe
        global deletedestroy
        deletedestroy = 1

        # Destroying all frames before proceeding
        choiceframe.destroy()
        mainframe.destroy()

        deleteframe = Frame(gui)
        deleteframe.grid(row=0, column=0)
        deleteframe.place(relx=0.5, rely=0.3, anchor=CENTER)

        cmer()

    def inventory():  # Function to display products as well as raw materials in stock.

        global inventoryframe
        inventoryframe = Frame(gui)

        global inventorydestroy
        inventorydestroy = 1  # Set to 1 so when the home button is clicked it goes to startwindow() after destroying
        # this frame.

        choiceframe.destroy()
        mainframe.destroy()

        label1 = Label(inventoryframe, text="Products", font="times 20")
        mycursor.execute("select * from product")
        rows = mycursor.fetchall()

        # Creating TreeViews to display data in the form of tables
        tv1 = ttk.Treeview(inventoryframe, columns=(1, 2, 3, 4, 5), show="headings")
        tv1.heading(1, text="Product ID")
        tv1.heading(2, text="Product Name")
        tv1.heading(3, text="Quantity Available")
        tv1.heading(4, text="Price")
        tv1.heading(5, text="ID of Raw Material Used")
        for i in rows:
            tv1.insert('', 'end', values=i)
        label1.grid(row=0, padx=10, pady=10)
        tv1.grid(row=1)

        label2 = Label(inventoryframe, text="Raw Materials", font="times 20")
        mycursor.execute("select * from rawmaterial")
        rows = mycursor.fetchall()
        tv2 = ttk.Treeview(inventoryframe, columns=(1, 2, 3, 4), show="headings")
        tv2.heading(1, text="Material ID")
        tv2.heading(2, text="Material Name")
        tv2.heading(3, text="Quantity Available")
        tv2.heading(4, text="Price")
        for i in rows:
            tv2.insert('', 'end', values=i)
        label2.grid(row=2, padx=10, pady=10)
        tv2.grid(row=3)

        back = Button(inventoryframe, text="Home", command=startwindow)
        back.grid(row=4, column=0, pady=35)

        inventoryframe.grid()
        inventoryframe.place(relx=0.5, rely=0.4, anchor=CENTER)

    def manufacture():  # Function to manufacture a product

        def manufactured():
            prodid = int(enterprod.get())  # Fetching the product ID entered by the user

            mycursor.execute("select ProductID from product where ProductID = ('{}')".format(prodid))
            checking = (str(mycursor.fetchall()))[2:-3]

            if checking.isdigit():  # Checking if record exists
                # Fetching the quantity of the raw material available
                mycursor.execute("select MaterialID from product where ProductID = ('{}')".format(prodid))
                matid = int((str(mycursor.fetchall())[2:-3]))  # Fetching material ID

                mycursor.execute("select Quantity from rawmaterial where MaterialID = ('{}')".format(matid))
                available = int((str(mycursor.fetchall())[2:-3]))  # Fetching available quantity of raw material

                if available >> 0:  # Checking if quantity available is enough for manufacturing
                    mycursor.execute(
                        "update product set QuantityAvailable = QuantityAvailable+1 where ProductID = ('{}')".format(
                            prodid))
                    mycursor.execute("update rawmaterial set "
                                     "Quantity = Quantity-1 where MaterialID= ('{}')".format(matid))
                    mydb.commit()
                    manlabel = Label(manufactureframe, text="Product Manufactured", font="times 15")
                    manlabel.grid(row=3)
                else:
                    label1.destroy()
                    enterprod.destroy()
                    manbutton.destroy()
                    fail = Label(manufactureframe, text="Not enough raw materials, more stock needed", font="times 14")
                    fail.grid(row=0)
            else:
                label1.destroy()
                enterprod.destroy()
                manbutton.destroy()
                failabel = Label(manufactureframe, text="Entry does not exist", font="times 15")
                failabel.grid()

        choiceframe.destroy()
        mainframe.destroy()

        global manufacturedestroy
        global manufactureframe
        manufactureframe = Frame(gui)
        manufacturedestroy = 1

        label1 = Label(manufactureframe, text="Enter the ID of the product to be manufactured", font="times 15")
        enterprod = Entry(manufactureframe)
        manbutton = Button(manufactureframe, command=manufactured, text="Manufacture")
        back = Button(manufactureframe, text="Home", command=startwindow)

        label1.grid(padx=50, pady=20)
        enterprod.grid(row=1, column=0, padx=50, pady=5)
        manbutton.grid(row=2, column=0, pady=20)
        back.grid(row=5, column=0, pady=20)

        manufactureframe.grid()
        manufactureframe.place(relx=0.5, rely=0.3, anchor=CENTER)

    def raw():  # Function for ordering raw materials

        def order():
            # Next few lines deducts cost of the transaction from factory funds
            rawmat = int(rawentry.get())  # Stores Material ID entered by user
            supid = int(supplierentry.get())

            mycursor.execute("select MaterialID from rawmaterial where MaterialID = ('{}')".format(rawmat))
            checking = (str(mycursor.fetchall()))[2:-3]

            if checking.isdigit():  # Checking if record exists
                mycursor.execute("select SupplierID from supplier where SupplierID = ('{}')".format(supid))
                checking2 = (str(mycursor.fetchall()))[2:-3]
                if checking2.isdigit():
                    mycursor.execute("select DeliveryCharge from supplier where SupplierId = ('{}')".format(supid))
                    deliverycharge = int((str(mycursor.fetchall())[2:-3]))

                    quantity = int(quantenter.get())  # Stores quantity of raw material entered by user
                    mycursor.execute("select Price from rawmaterial where MaterialID = ('{}')".format(rawmat))
                    materialcost = int((str(mycursor.fetchall())[2:-3]))
                    totalcost = (materialcost * quantity) + deliverycharge
                    mycursor.execute("update funds set Amount = Amount - ('{}')".format(totalcost))

                    # Destroying all frames before proceeding.
                    rawlabel.destroy()
                    rawbutton.destroy()
                    rawentry.destroy()
                    supplierentry.destroy()
                    supplierlabel.destroy()
                    quantlabel.destroy()
                    quantenter.destroy()

                    mycursor.execute(
                        "update rawmaterial set Quantity = Quantity + ('{}') where MaterialID = ('{}')".format(quantity,
                                                                                                               rawmat))

                    rawdone = Label(rawframe, text="Order Placed", font="times 20")
                    rawdone.grid(row=0, pady=20)

                    mydb.commit()
                else:
                    rawlabel.destroy()
                    rawentry.destroy()
                    quantlabel.destroy()
                    quantenter.destroy()
                    rawbutton.destroy()
                    supplierlabel.destroy()
                    supplierentry.destroy()
                    failabel = Label(rawframe, text="Entry does not exist", font="times 15")
                    failabel.grid()
            else:
                rawlabel.destroy()
                rawentry.destroy()
                quantlabel.destroy()
                quantenter.destroy()
                rawbutton.destroy()
                supplierlabel.destroy()
                supplierentry.destroy()
                failabel = Label(rawframe, text="Entry does not exist", font="times 15")
                failabel.grid()

        global rawframe
        rawframe = Frame(gui)

        global rawdestroy
        rawdestroy = 1

        choiceframe.destroy()
        mainframe.destroy()

        rawlabel = Label(rawframe, text="Enter the ID of the raw material to order", font="times 15")
        rawentry = Entry(rawframe)

        supplierlabel = Label(rawframe, text="Enter ID of supplier", font="times 15")
        supplierentry = Entry(rawframe)

        quantlabel = Label(rawframe, text="Enter Quantity to be Ordered", font="times 15")
        quantenter = Entry(rawframe)
        rawbutton = Button(rawframe, command=order, text="Place order")
        back = Button(rawframe, text="Home", command=startwindow)

        rawlabel.grid(row=0, column=0, pady=10)
        rawentry.grid(row=0, column=1)
        supplierlabel.grid(row=1, column=0, pady=10)
        supplierentry.grid(row=1, column=1, pady=10)
        quantlabel.grid(row=2, column=0, pady=10)
        quantenter.grid(row=2, column=1, pady=10)
        rawbutton.grid(row=3, pady=20)
        back.grid(pady=20, row=4)
        rawframe.grid(padx=100)
        rawframe.place(relx=0.5, rely=0.3, anchor=CENTER)

    def add():  # Function to add a customer to database

        def added():
            mycursor.execute(
                "insert into customer values(('{}'), ('{}'), ('{}'), ('{}'), ('{}'))".format(int(enterid.get()),
                                                                                             entername.get(),
                                                                                             entercity.get(),
                                                                                             enterph.get(),
                                                                                             int(enterbal.get())))
            done = Label(addframe, text="Customer added")
            done.grid(row=8, pady=30)
            mydb.commit()

        choiceframe.destroy()
        mainframe.destroy()

        global addframe
        addframe = Frame(gui)

        global adddestroy
        adddestroy = 1

        addlabelframe = Frame(addframe)
        addlabel = Label(addlabelframe, text="Enter details of the customer", font="time 15")

        enterframe = Frame(addframe)

        addID = Label(enterframe, text="Enter ID")
        addname = Label(enterframe, text="Enter Name")
        addcity = Label(enterframe, text="Enter City")
        addph = Label(enterframe, text="Enter Phone Number")
        addbal = Label(enterframe, text="Enter Balance")

        enterid = Entry(enterframe)
        entername = Entry(enterframe)
        entercity = Entry(enterframe)
        enterph = Entry(enterframe)
        enterbal = Entry(enterframe)

        addlabel.grid(pady=20)

        addID.grid(row=1, column=0, pady=7, sticky=E)
        addname.grid(row=2, column=0, pady=7, sticky=E)
        addcity.grid(row=3, column=0, pady=7, sticky=E)
        addph.grid(row=4, column=0, pady=7, sticky=E)
        addbal.grid(row=5, column=0, pady=7, sticky=E)

        enterid.grid(row=1, column=1, pady=7)
        entername.grid(row=2, column=1, pady=7)
        entercity.grid(row=3, column=1, pady=7)
        enterph.grid(row=4, column=1, pady=7)
        enterbal.grid(row=5, column=1, pady=7)

        addbutton = Button(enterframe, command=added, text="Add", font="times 15")
        addbutton.grid(column=1)

        back = Button(enterframe, text="Home", font="times 15", command=startwindow)
        back.grid(pady=20, row=7, column=1)

        addframe.grid(padx=100)
        addlabelframe.grid()
        addframe.place(relx=0.5, rely=0.3, anchor=CENTER)
        enterframe.grid()

    def sell():  # Function to sell a product to a customer based on details entered by user
        def sold():
            pid = enterprod.get()
            cid = entercust.get()
            orderno = int(enterorder.get())
            quantity = int(enterquant.get())
            eid = int(enteremp.get())
            incentive = 0
            mycursor.execute("select Price from product where ProductID = ('{}')".format(pid))
            price = int((str(mycursor.fetchall())[2:-3]))
            mycursor.execute("select ProductName from product where ProductID = ('{}')".format(pid))
            pname = (str(mycursor.fetchall())[3:-4])
            mycursor.execute("select CustomerName from customer where CustomerID = ('{}')".format(cid))
            cname = (str(mycursor.fetchall())[3:-4])
            mycursor.execute("select QuantityAvailable from product where ProductID = ('{}')".format(pid))
            quantavailable = int((str(mycursor.fetchall())[2:-3]))

            mycursor.execute("select Balance from customer where CustomerID = ('{}')".format(cid))
            custbal = int((str(mycursor.fetchall())[2:-3]))

            if (quantity * price) > custbal:  # Checks if customer can afford order
                sellheadframe.destroy()
                sellcust.destroy()
                entercust.destroy()
                sellemp.destroy()
                enteremp.destroy()
                sellprod.destroy()
                enterprod.destroy()
                sellbutton.destroy()
                quantlabel.destroy()
                enterquant.destroy()
                enterorder.destroy()
                ordernolabel.destroy()
                back.destroy()
                faillab = Label(sellframe, text="Customer cannot afford this sale.", font="times 14")
                faillab.grid()
                failbutton = Button(sellframe, text="Home", command=startwindow, font="times 14")
                failbutton.grid(row=1)
            else:

                if quantity < quantavailable:

                    mycursor.execute("update funds set Amount = Amount + ('{}')".format((quantity * price)))

                    # The next few lines calculate the incentives to the employees depending on the
                    # amount made during the sale
                    if (price * quantity) < 20000:
                        incentive = 0.25 / 100 * (price * quantity)
                        mycursor.execute("update employee set Salary = Salary + ('{}') "
                                         "where EmployeeID = ('{}')".format(incentive, eid))
                    elif (price * quantity) >= 20000 & price * quantity < 35000:
                        incentive = 1.00 / 100 * (price * quantity)
                        mycursor.execute("update employee set Salary = Salary + ('{}') "
                                         "where EmployeeID = ('{}')".format(incentive, eid))
                    elif (price * quantity) >= 35000 & price * quantity < 60000:
                        incentive = 2.00 / 100 * (price * quantity)
                        mycursor.execute("update employee set Salary = Salary + ('{}') "
                                         "where EmployeeID = ('{}')".format(incentive, eid))
                    elif (price * quantity) >= 60000 & price * quantity < 90000:
                        incentive = 3.50 / 100 * (price * quantity)
                        mycursor.execute("update employee set Salary = Salary + ('{}') "
                                         "where EmployeeID = ('{}')".format(incentive, eid))
                    elif (price * quantity) >= 90000 & price * quantity < 120000:
                        incentive = 5.50 / 100 * (price * quantity)
                        mycursor.execute("update employee set Salary = Salary + ('{}') "
                                         "where EmployeeID = ('{}')".format(incentive, eid))
                    elif (price * quantity) >= 120000:
                        incentive = 7.50 / 100 * (price * quantity)
                        mycursor.execute("update employee set Salary = Salary + ('{}') "
                                         "where EmployeeID = ('{}')".format(incentive, eid))

                    sellheadframe.destroy()
                    sellcust.destroy()
                    entercust.destroy()
                    sellemp.destroy()
                    enteremp.destroy()
                    sellprod.destroy()
                    enterprod.destroy()
                    sellbutton.destroy()
                    quantlabel.destroy()
                    enterquant.destroy()
                    enterorder.destroy()
                    ordernolabel.destroy()

                    mycursor.execute(
                        "update product set QuantityAvailable = QuantityAvailable-('{}') where "
                        "ProductID = ('{}')".format(
                            quantity, pid))
                    mycursor.execute(
                        "update  customer set Balance = Balance - ('{}') where CustomerID = ('{}')".format(
                            (quantity * price),
                            cid))
                    mycursor.execute(
                        "insert into orders values(('{}'),"
                        " ('{}'), ('{}'), ('{}'), ('{}'),"
                        " ('{}'),('{}'),('{}'))".format(orderno, int(cid), cname, int(pid), pname, eid, quantity,
                                                        price * quantity))

                    mydb.commit()
                    soldlabel1 = Label(sellframe, text="Product Sold, and incentive added to "
                                                       "the employee's salary. Incentive amount:", font="times 15")
                    soldlabel1.grid(row=11, padx=100, pady=10)
                    soldlabel2 = Label(sellframe, text="", font="times 14")
                    soldlabel2.config(text=incentive)
                    soldlabel2.grid(row=12)

                else:
                    sellheadframe.destroy()
                    sellcust.destroy()
                    entercust.destroy()
                    sellemp.destroy()
                    enteremp.destroy()
                    sellprod.destroy()
                    enterprod.destroy()
                    sellbutton.destroy()
                    quantlabel.destroy()
                    enterquant.destroy()
                    enterorder.destroy()
                    ordernolabel.destroy()
                    fail = Label(sellframe, text="Product not available, more need to be manufactured", font="times 14")
                    fail.grid()

        choiceframe.destroy()
        mainframe.destroy()

        global sellframe  # This and the next 4 lines sets this frame to be destroyed
        # once the user clicks the Home button
        sellframe = Frame(gui)
        global sellheadframe

        global selldestroy
        selldestroy = 1

        sellheadframe = Frame(gui)
        sellhead = Label(sellheadframe, text="Specify product being sold, employee selling it and the customer it is "
                                             "being sold to",
                         font="times 15")
        sellcust = Label(sellframe, text="Enter Customer ID", font="times 15")
        sellemp = Label(sellframe, text="Enter Employee ID", font="times 15")
        sellprod = Label(sellframe, text="Enter Product ID", font="times 15")
        ordernolabel = Label(sellframe, text="Enter an Order Number", font="times 15")
        quantlabel = Label(sellframe, text="Enter Quantity bought", font="times 15")
        enterorder = Entry(sellframe)
        entercust = Entry(sellframe)
        enteremp = Entry(sellframe)
        enterquant = Entry(sellframe)
        enterprod = Entry(sellframe)
        sellbutton = Button(sellframe, command=sold, text="Sell", font="times 15")

        sellheadframe.grid(pady=20, row=0)
        sellframe.grid(padx=100, row=1, pady=30)
        sellhead.grid()
        ordernolabel.grid(row=4, column=0, sticky=E)
        enterorder.grid(row=4, column=1)
        sellcust.grid(row=1, column=0, sticky=E)
        entercust.grid(row=1, column=1)
        sellemp.grid(row=2, column=0, sticky=E)
        enteremp.grid(row=2, column=1)
        sellprod.grid(row=3, column=0, sticky=E)
        enterprod.grid(row=3, column=1)
        quantlabel.grid(row=5, column=0, sticky=E)
        enterquant.grid(row=5, column=1)
        sellbutton.grid(row=7, column=1, pady=20)
        sellheadframe.place(relx=0.5, rely=0.1, anchor=CENTER)
        sellframe.place(relx=0.5, rely=0.3, anchor=CENTER)
        back = Button(sellframe, text="Home", font="times 15", command=startwindow)
        back.grid(pady=20, row=9, column=0)

    def checkorder():  # Function to display the orders table

        choiceframe.destroy()
        mainframe.destroy()

        global checkorderdestroy
        checkorderdestroy = 1

        global checkorderframe
        checkorderframe = Frame(gui)

        # Creating a TreeView to display data in the form of a table
        mycursor.execute("select * from orders")
        rows = mycursor.fetchall()
        tv = ttk.Treeview(checkorderframe, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings")
        tv.heading(1, text="Order Number")
        tv.heading(2, text="Customer ID")
        tv.heading(3, text="Customer Name")
        tv.heading(4, text="Product ID")
        tv.heading(5, text="Product Name")
        tv.heading(6, text="Employee ID")
        tv.heading(7, text="Quantity Bought")
        tv.heading(8, text="Sale Value")

        for i in rows:
            tv.insert('', 'end', values=i)
        tv.grid()

        checkorderframe.grid(padx=100, pady=100)
        checkorderframe.place(relx=0.5, rely=0.3, anchor=CENTER)

        back = Button(checkorderframe, text="Home", command=startwindow)
        back.grid(pady=40)

    def avsal():
        def maxsal():
            maxsalbutton.destroy()
            avsalbutton.destroy()

            mycursor.execute("select MAX(Salary) from employee")
            uid = int((str(mycursor.fetchall())[2:-3]))

            detailframe = Frame(avsalframe)
            detailframe.grid(row=0, column=0, pady=50)

            displayframe = Frame(avsalframe)
            displayframe.grid(row=0, column=1, pady=50)

            detaillabel1 = Label(detailframe, text="Employee ID: ", font="times 15")
            detaillabel1.grid(row=0, sticky=E)

            detaillabel2 = Label(detailframe, text="Name: ", font="times 15")
            detaillabel2.grid(row=1, sticky=E)

            detaillabel3 = Label(detailframe, text="Salary: ", font="times 15")
            detaillabel3.grid(row=2, sticky=E)

            detailID = Label(displayframe, text="", font="times 15 ")
            mycursor.execute(
                "select EmployeeID from employee where Salary = ('{}')".format(uid))  # Fetching data
            data1 = mycursor.fetchall()
            detailID.config(text=data1)
            detailID.grid(row=0, sticky=W)

            detailname = Label(displayframe, text="", font="times 14")
            mycursor.execute(
                "select EmployeeName from employee where Salary = ('{}')".format(uid))  # Fetching data
            data2 = (str(mycursor.fetchall()))[3:-4]
            detailname.config(text=data2)
            detailname.grid(row=1, sticky=W)

            detailsal = Label(displayframe, text="", font="times 14")
            mycursor.execute("select Salary from employee where Salary = ('{}')".format(uid))  # Fetching data
            data3 = (str(mycursor.fetchall()))[2:-3]
            detailsal.config(text=data3)
            detailsal.grid(row=2, sticky=W)

        def average():
            maxsalbutton.destroy()
            avsalbutton.destroy()

            mycursor.execute("select AVG(Salary) from employee")
            uid = (str(mycursor.fetchall())[11:-5])

            displaylabel1 = Label(avsalframe, text="Average Salary: ", font="times 20")
            displaylabel1.grid(row=0, column=0)

            displaylabel2 = Label(avsalframe, text="", font="times 20")
            displaylabel2.config(text=uid)
            displaylabel2.grid(row=0, column=1)

        choiceframe.destroy()
        mainframe.destroy()

        global avsaldestroy
        avsaldestroy = 1

        global avsalframe
        avsalframe = Frame(gui)

        maxsalbutton = Button(avsalframe, command=maxsal, text="Employee With Maximum Salary", font="times 15")
        avsalbutton = Button(avsalframe, command=average, text="Average Employee Salary", font="times 15")

        back = Button(avsalframe, text="Home", command=startwindow)
        back.grid(row=3, pady=40)
        maxsalbutton.grid(row=0, column=0, pady=15)
        avsalbutton.grid(row=1, column=0, pady=15)
        avsalframe.grid(padx=100, pady=100)
        avsalframe.place(relx=0.5, rely=0.3, anchor=CENTER)

    choiceframe = Frame(gui)
    choiceframe.grid(pady=15)
    choiceframe.place(relx=0.5, rely=0.07, anchor=CENTER)

    mainframe = Frame(gui)
    mainframe.grid(padx=100, pady=50)
    mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Presenting functionalities to the user
    choicetext = Label(choiceframe, text="Choose an Operation", font="times 40")
    choicetext.grid(row=0, column=1, pady=20)

    choice1 = Button(mainframe, command=search, text="Search Record", font="times 20")
    choice1.grid(row=1, column=0, pady=10)

    choice2 = Button(mainframe, command=delete, text="Delete Customer record", font="times 20")
    choice2.grid(row=2, column=0, pady=10)

    choice3 = Button(mainframe, command=inventory, text="Check Inventory", font="times 20")
    choice3.grid(row=3, column=0, pady=10)

    choice4 = Button(mainframe, command=manufacture, text="Manufacture Product", font="times 20")
    choice4.grid(row=4, column=0, pady=10)

    choice5 = Button(mainframe, command=raw, text="Place Order for Raw Material", font="times 20")
    choice5.grid(row=5, column=0, pady=10)

    choice6 = Button(mainframe, command=add, text="Add Customer", font="times 20")
    choice6.grid(row=6, column=0, pady=10)

    choice7 = Button(mainframe, command=sell, text="Sell Product", font="times 20")
    choice7.grid(row=7, column=0, pady=10)

    choice8 = Button(mainframe, command=checkorder, text="Check Orders", font="times 20")
    choice8.grid(row=8, column=0, pady=10)

    choice9 = Button(mainframe, command=avsal, text="Find out Employee Details", font="times 20")
    choice9.grid(row=9, column=0, pady=10)

    # Funds is a table in the database that stores the total funds available to the factory
    fundlabel = Label(mainframe, text="Total available funds: ", font="times 15")
    fundlabel.grid(row=10, column=0, pady=15)
    fundlabel2 = Label(mainframe, text="", font="times 15")
    mycursor.execute("select * from funds")
    funds = int((str(mycursor.fetchall()))[2:-3])
    fundlabel2.config(text=funds)
    fundlabel2.grid(row=10, column=1, pady=15)


first()
# Execute GUI
gui.mainloop()
