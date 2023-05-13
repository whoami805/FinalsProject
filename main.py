import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk
from PIL import ImageTk,Image
import mysql.connector


def window():
    root = tk.Tk()
    root.geometry("400x420")
    root.title("Goblin Slayer RPG Login")
    root.config(bg="#444444")
    root.resizable(0,0)
    conn = mysql.connector.connect(host="localhost",user="root",password="",db="final")
    cur = conn.cursor()

    def modpage():
        root1 = tk.Toplevel()
        root1.geometry("1000x580")
        root1.title("MODERATOR")
        root1.config(bg="#444444")
        root1.resizable(0, 0)

        frame = tk.Frame(root1, bg="#222222", height=420, width=960)
        frame.place(x=20, y=130)

        frame2 = tk.Frame(root1, bg="#333333", height=380, width=920)
        frame2.place(x=40, y=150)

        frame3 = tk.Frame(root1, bg="#222222", height=105, width=380)
        frame3.place(x=600, y=10)

        frame5 = tk.Frame(root1, bg="#333333", height=85, width=360)
        frame5.place(x=610, y=20)

        label = tk.Label(frame2, text="Total User:", font=("Arial", 14), bg="#333333", foreground="white")
        label.place(x=700, y=20)
        label2 = tk.Label(frame2, text="", font=("Arial", 14), bg="#333333", foreground="white")
        label2.place(x=800, y=20)

        cur.execute("select count(*) from user_data")
        result = (list(cur))
        label2.config(text=result)

        my_tree = ttk.Treeview(frame2, height=13)

        def updBtn():
            username = usernameEntry.get()
            name = newnameEntry.get()
            lastname = newlastnameEntry.get()

            query = "UPDATE user_data SET name='"+name+"',lastname='"+lastname+"' WHERE username='"+username+"'"
            cur.execute(query)
            conn.commit()

            refresh()


        def refresh():
            query = "SELECT * FROM user_data"
            cur.execute(query)

            row = cur.fetchall()

            display(row)

        def select_row(e):
            usernameEntry.delete(0,END)
            newlastnameEntry.delete(0,END)
            newnameEntry.delete(0,END)

            select = my_tree.focus()
            item = my_tree.item(select, "values")

            usernameEntry.insert(0, item[2])
            newnameEntry.insert(0,item[0])
            newlastnameEntry.insert(0,item[1])

        def display(row):
            my_tree.delete(*my_tree.get_children())
            for i in row:
                my_tree.insert("", "end", values=(i[0], i[1], i[2], i[4]))

        logoutBtn = tk.Button(root1, text="LOGOUT", font=("Arial", 11, "bold"), bg="#393535", fg="white",cursor="hand2", width=8, command=lambda: [root1.withdraw(), window()])
        logoutBtn.place(x=870, y=45)

        statusLabel = tk.Label(root1, text="STATUS: MODERATOR", font=("Arial", 13), bg="#333333",foreground="white")
        statusLabel.place(x=620, y=70)

        username = tk.Label(frame2, text="Username:", bg="#333333")
        username.place(x=10, y=10)

        usernameEntry = tk.Entry(frame2,text="",width=14)
        usernameEntry.place(x=80, y=10)

        newname = tk.Label(frame2, text="Update Name:", bg="#333333")
        newname.place(x=190,y=10)

        newnameEntry = tk.Entry(frame2)
        newnameEntry.place(x=300, y=10)

        newlastname = tk.Label(frame2, text="Update LastName:", bg="#333333")
        newlastname.place(x=190,y=35)

        newlastnameEntry = tk.Entry(frame2)
        newlastnameEntry.place(x=300, y=35)

        user = tk.Label(root1, text=": MOD", font=("Arial", 14), bg="#333333", foreground="white")
        user.place(x=660, y=30)

        statusLabel = tk.Label(root1, text="STATUS: MODERATOR", font=("Arial", 13), bg="#333333",foreground="white")
        statusLabel.place(x=620, y=70)

        updateBtn = tk.Button(frame2, text="UPDATE", font=("Arial", 11, "bold"), bg="#393535", fg="white",cursor="hand2", width=15, command=updBtn)
        updateBtn.place(x=500, y=20)

        icon = Image.open(r"C:\Users\John Lester\Desktop\img\profile icon.png")

        icon = icon.resize((40, 40))

        my_icon = ImageTk.PhotoImage(icon)

        label3 = tk.Label(root1, image=my_icon, bg="#333333")
        label3.image = my_icon
        label3.place(x=615, y=23)

        image = Image.open(r"C:\Users\John Lester\Desktop\img\Goblin slayer title.png")

        img = image.resize((300, 80))

        my_img = ImageTk.PhotoImage(img)

        label = tk.Label(root1, image=my_img, bg="#444444")
        label.image = my_img
        label.place(x=30, y=20)

        my_tree["column"] = ("name", "lastname", "username","email")
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("name", width=250, anchor=CENTER)
        my_tree.column("lastname", width=250, anchor=CENTER)
        my_tree.column("username", width=200, anchor=CENTER)
        my_tree.column("email", width=190, anchor=CENTER)
        my_tree.heading("name", text="Name", anchor=CENTER)
        my_tree.heading("lastname", text="Last Name", anchor=CENTER)
        my_tree.heading("username", text="Username", anchor=CENTER)
        my_tree.heading("email", text="email", anchor=CENTER)

        my_tree.place(x=15, y=70)

        my_tree.bind("<ButtonRelease-1>", select_row)

        query = "SELECT * FROM user_data"
        cur.execute(query)
        row = cur.fetchall()

        display(row)

    def adminpage():
        root1 = tk.Toplevel()
        root1.geometry("1000x580")
        root1.title("ADMIN")
        root1.config(bg="#444444")
        root1.resizable(0, 0)


        frame = tk.Frame(root1, bg="#222222", height=420, width=960)
        frame.place(x=20, y=130)

        frame2 = tk.Frame(root1, bg="#333333", height=380, width=920)
        frame2.place(x=40, y=150)

        frame3 = tk.Frame(root1, bg="#222222", height=105, width=380)
        frame3.place(x=600, y=10)

        frame5 = tk.Frame(root1, bg="#333333", height=85, width=360)
        frame5.place(x=610, y=20)

        label = tk.Label(frame2, text="Total User:",font=("Arial", 14), bg="#333333", foreground="white")
        label.place(x=700,y=20)
        label2 = tk.Label(frame2, text="",font=("Arial", 14), bg="#333333", foreground="white")
        label2.place(x=800,y=20)

        cur.execute("select count(*) from user_data")
        result = (list(cur))
        label2.config(text=result)

        my_tree = ttk.Treeview(frame2, height=13)

        def refresh():
            query = "SELECT * FROM user_data"
            cur.execute(query)

            row = cur.fetchall()

            cur.execute("select count(*) from user_data")
            result = (list(cur))
            label2.config(text=result)

            display(row)

        def delBtn():
            user = usernameEntry.get()

            query = "DELETE FROM user_data WHERE username='"+user+"'"
            cur.execute(query)
            conn.commit()

            refresh()

        def select_row(e):
            usernameEntry.delete(0,END)
            passwordEntry.delete(0,END)

            select = my_tree.focus()
            item = my_tree.item(select, "values")

            usernameEntry.insert(0, item[2])
            passwordEntry.insert(0, item[3])

        def display(row):
            my_tree.delete(*my_tree.get_children())
            for i in row:
                my_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5]))

        logoutBtn = tk.Button(root1, text="LOGOUT", font=("Arial", 11, "bold"), bg="#393535", fg="white",cursor="hand2", width=8,command=lambda:[root1.withdraw(),window()])
        logoutBtn.place(x=870, y=45)

        statusLabel = tk.Label(root1, text="STATUS: ADMINISTRATOR", font=("Arial", 13), bg="#333333", foreground="white")
        statusLabel.place(x=620, y=70)

        deleteBtn = tk.Button(frame2, text="DELETE", font=("Arial", 11, "bold"), bg="#393535", fg="white",cursor="hand2", width=15,command=delBtn)
        deleteBtn.place(x=230, y=20)

        username = tk.Label(frame2,text="Username:", bg="#333333")
        username.place(x=10,y=10)

        password = tk.Label(frame2,text="Password:", bg="#333333")
        password.place(x=10,y=35)

        usernameEntry = tk.Entry(frame2)
        usernameEntry.place(x=80,y=10)

        passwordEntry = tk.Entry(frame2)
        passwordEntry.place(x=80,y=35)

        user = tk.Label(root1,text=": ADMIN",font=("Arial", 14), bg="#333333", foreground="white")
        user.place(x=660,y=30)

        statusLabel = tk.Label(root1, text="STATUS: ADMINISTRATOR", font=("Arial", 13), bg="#333333", foreground="white")
        statusLabel.place(x=620, y=70)


        icon = Image.open(r"C:\Users\John Lester\Desktop\img\profile icon.png")

        icon = icon.resize((40, 40))

        my_icon = ImageTk.PhotoImage(icon)

        label3 = tk.Label(root1, image=my_icon, bg="#333333")
        label3.image = my_icon
        label3.place(x=615, y=23)

        image = Image.open(r"C:\Users\John Lester\Desktop\img\Goblin slayer title.png")

        img = image.resize((300, 80))

        my_img = ImageTk.PhotoImage(img)

        label = tk.Label(root1, image=my_img, bg="#444444")
        label.image = my_img
        label.place(x=30, y=20)

        my_tree["column"]=("name","lastname","username","password","email","date",)
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("name", width=150, anchor=CENTER)
        my_tree.column("lastname", width=150, anchor=CENTER)
        my_tree.column("username", width=130, anchor=CENTER)
        my_tree.column("password", width=130, anchor=CENTER)
        my_tree.column("email", width=150, anchor=CENTER)
        my_tree.column("date", width=175, anchor=CENTER)
        my_tree.heading("name", text="Name", anchor=CENTER)
        my_tree.heading("lastname", text="Last Name", anchor=CENTER)
        my_tree.heading("username", text="Username", anchor=CENTER)
        my_tree.heading("password", text="Password", anchor=CENTER)
        my_tree.heading("email", text="Email", anchor=CENTER)
        my_tree.heading("date", text="Date Created", anchor=CENTER)

        my_tree.place(x=15,y=70)

        my_tree.bind("<ButtonRelease-1>", select_row)

        query = "SELECT * FROM user_data"
        cur.execute(query)
        row = cur.fetchall()

        display(row)

    def homepage():
        root1 = tk.Toplevel()
        root1.geometry("1000x580")
        root1.title("Home Page")
        root1.config(bg="#444444")
        root1.resizable(0, 0)

        def prereg():
            messagebox.showinfo("Info", "Pre-Register Successfully!")

        frame = tk.Frame(root1, bg="#222222", height=420, width=960)
        frame.place(x=20, y=130)

        frame2 = tk.Frame(root1, bg="#333333", height=380, width=920)
        frame2.place(x=40, y=150)

        frame3 = tk.Frame(root1, bg="#222222", height=105, width=380)
        frame3.place(x=600, y=10)

        frame4 = tk.Frame(root1, bg="#222222", height=220, width=430)
        frame4.place(x=520, y=180)

        frame5 = tk.Frame(root1, bg="#333333", height=85, width=360)
        frame5.place(x=610, y=20)

        disLabel = tk.Label(root1, text="GOBLIN SLAYER RPG", font=("Arial", 24, "bold"), bg="#222222",foreground="white")
        disLabel.place(x=530, y=200)

        disLabel2 = tk.Label(root1, text="GREAT WAR BATTLES", font=("Arial", 14), bg="#222222", foreground="white")
        disLabel2.place(x=530, y=250)

        disLabel3 = tk.Label(root1, text="ARE WAITING FOR YOU TO EXPERIENCE", font=("Arial", 14), bg="#222222",foreground="white")
        disLabel3.place(x=530, y=280)

        disLabel4 = tk.Label(root1, text="COMING SOON...", font=("Arial", 33, "bold"), bg="#222222",foreground="white")
        disLabel4.place(x=530, y=320)

        preregBtn = tk.Button(root1, text="PRE-REGISTER", font=("Arial", 30, "bold"), bg="#393535", fg="white",cursor="hand2", width=16,command=prereg)
        preregBtn.place(x=540, y=420)

        statusLabel = tk.Label(root1, text="STATUS: User", font=("Arial", 14), bg="#333333", foreground="white")
        statusLabel.place(x=620, y=70)

        logoutBtn = tk.Button(root1, text="LOGOUT", font=("Arial", 11, "bold"), bg="#393535", fg="white",cursor="hand2", width=8,command=lambda:[root1.withdraw(),window()])
        logoutBtn.place(x=870, y=45)

        user = tk.Label(root1,text=":",font=("Arial", 14), bg="#333333", foreground="white")
        user.place(x=660,y=30)

        username = tk.Label(root1,text="",font=("Arial", 14), bg="#333333", foreground="white")
        username.place(x=670,y=32)

        result = userEntry.get()
        username.config(text=result)

        image = Image.open(r"C:\Users\John Lester\Desktop\img\Goblin slayer title.png")

        img = image.resize((300, 80))

        my_img = ImageTk.PhotoImage(img)

        label = tk.Label(root1, image=my_img, bg="#444444")
        label.image = my_img
        label.place(x=30, y=20)

        image2 = Image.open(r"C:\Users\John Lester\Desktop\img\Goblin slayer2 img2.png")

        img2 = image2.resize((460, 340))

        my_img2 = ImageTk.PhotoImage(img2)

        label2 = tk.Label(root1, image=my_img2)
        label2.image = my_img2
        label2.place(x=50, y=170)

        icon = Image.open(r"C:\Users\John Lester\Desktop\img\profile icon.png")

        icon = icon.resize((40, 40))

        my_icon = ImageTk.PhotoImage(icon)

        label3 = tk.Label(root1, image=my_icon, bg="#333333")
        label3.image = my_icon
        label3.place(x=615, y=23)

    def login():
        if userEntry.get()=="admin" or passEntry.get()=="admin":
            messagebox.showinfo("Success", "Successfully login")
            root.withdraw()
            adminpage()
        elif userEntry.get()=="mod" or passEntry.get()=="mod":
            messagebox.showinfo("Success", "Successfully login")
            root.withdraw()
            modpage()
        elif userEntry.get()=="" or passEntry.get()=="":
            messagebox.showerror("Error","Enter Username and Password")
        else:
            user = userEntry.get()
            passw = passEntry.get()

            query = "SELECT * FROM user_data WHERE username=%s AND password=%s"
            val = (user,passw)

            cur.execute(query,val)

            row = cur.fetchone()

            if row == None:
                messagebox.showerror("ERROR","Invalid Username and Password")
            else:
                messagebox.showinfo("Success","Successfully login")
                root.withdraw()
                homepage()

    def forgot(e):
        root1 = Toplevel(root)
        root1.geometry("500x300")
        root1.config(bg="#444444")
        root1.resizable(0,0)
        root1.title("FORGOT PASSWORD")
        root.withdraw()

        frame = tk.Frame(root1, bg="#222222", height=210,width=460)
        frame.place(x=20,y=70)

        frame2= tk.Frame(root1, bg="#333333", height=170,width=420)
        frame2.place(x=40,y=90)

        label = tk.Label(root1, text="Find your account", font=("Arial",25,"bold"), bg="#444444", foreground="white")
        label.place(x=15,y=15)

        label2 = tk.Label(frame2,text="Please enter your email to search for your",font=("Arial",14),bg="#333333", foreground="white")
        label2.place(x=10,y=10)
        label3 = tk.Label(frame2,text="account.",font=("Arial",14),bg="#333333", foreground="white")
        label3.place(x=10,y=35)

        def enter_forgot():
            cur.execute("SELECT * FROM user_data WHERE email='" + emailEntry.get() + "'")
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("No Search Result",
                                     "Your search did not return any results. Please try again with other information.")
            else:
                messagebox.showinfo("Success", "We sent the link in your email to reset your password!")

        emailEntry = tk.Entry(frame2,font=("Arial",14),width=24)
        emailEntry.place(x=80,y=75)

        enterBtn = tk.Button(frame2,text="ENTER",font=("Arial",15,"bold"),bg="#393535",fg="white",cursor="hand2",command=enter_forgot)
        enterBtn.place(x=175,y=120)

        backBtn = tk.Button(root1,text="←",font=("Arial",15,"bold"),bg="#393535",fg="white",cursor="hand2",width=4,command=lambda:[root1.withdraw(),window()])
        backBtn.place(x=420,y=15)

    def signup():
        root1 = Toplevel(root)
        root1.geometry("500x450")
        root1.title("Signup")
        root1.resizable(0,0)
        root1.config(bg="#444444")
        root.withdraw()

        frame = tk.Frame(root1,bg="#222222",width=440,height=350)
        frame.place(x=30,y=70)
        frame2 = tk.Frame(root1,bg="#333333", width=400,height=310)
        frame2.place(x=50,y=90)

        def reg():
            name = nameEntry.get()
            lname = lnameEntry.get()
            user = userEntry.get()
            passw = passEntry.get()
            email = emailEntry.get()
            if nameEntry.get() == "" or lnameEntry.get() == "" or userEntry.get() == "" or passEntry.get() == "" or conpassEntry.get() =="" or emailEntry.get() == "":
                messagebox.showerror("Error", "Enter Valid Entry")
            elif passEntry.get() != conpassEntry.get():
                messagebox.showerror("Error", "Password Not Match")
                nameEntry.delete(0,END)
                lnameEntry.delete(0, END)
                userEntry.delete(0, END)
                passEntry.delete(0, END)
                conpassEntry.delete(0, END)
                emailEntry.delete(0, END)

            else:
                query = "INSERT INTO user_data(name,lastname,username,password,email) VALUES (%s,%s,%s,%s,%s)"
                val = (name, lname, user, passw, email)
                nameEntry.delete(0,END)
                lnameEntry.delete(0, END)
                userEntry.delete(0, END)
                passEntry.delete(0, END)
                conpassEntry.delete(0, END)
                emailEntry.delete(0, END)

                cur.execute(query, val)
                conn.commit()
                messagebox.showinfo("Message", "SignUp Success")

        backBtn = tk.Button(root1,text="←",font=("Arial",15,"bold"),bg="#393535",fg="white",cursor="hand2",width=4,command=lambda:[root1.withdraw(),window()])
        backBtn.place(x=400,y=15)

        label = tk.Label(root1,text="Sign Up",font=("Arial",23,"bold"),bg="#444444",foreground="white")
        label.place(x=30,y=20)

        nameLabel = tk.Label(root1,text="Name",font=("Arial",14),bg="#333333",fg="white")
        nameLabel.place(x=120,y=110)
        nameEntry = tk.Entry(root1,font=10,width=15)
        nameEntry.place(x=80,y=140)

        lnameLabel = tk.Label(root1,text="Last Name",font=("Arial",14),bg="#333333",fg="white")
        lnameLabel.place(x=300,y=110)
        lnameEntry = tk.Entry(root1,font=10,width=15)
        lnameEntry.place(x=280,y=140)

        userLabel = tk.Label(root1,text="Username:",font=("Arial",14),bg="#333333",fg="white")
        userLabel.place(x=80,y=180)
        userEntry = tk.Entry(root1,font=10,width=24)
        userEntry.place(x=200,y=185)

        passLabel = tk.Label(root1,text="Password:",font=("Arial",14),bg="#333333",fg="white")
        passLabel.place(x=80,y=220)
        passEntry = tk.Entry(root1,show="*",font=10,width=24)
        passEntry.place(x=200,y=222)

        conpassLabel = tk.Label(root1,text="Confirm Pass:",font=("Arial",13),bg="#333333",fg="white")
        conpassLabel.place(x=80,y=260)
        conpassEntry = tk.Entry(root1,show="*",font=10,width=24)
        conpassEntry.place(x=200,y=262)

        emailLabel = tk.Label(root1,text="Email:",font=("Arial",14),bg="#333333",fg="white")
        emailLabel.place(x=80,y=300)
        emailEntry = tk.Entry(root1,font=10,width=24)
        emailEntry.place(x=200,y=302)

        signupBtn = tk.Button(root1,text="Sign Up",font=("Arial",15,"bold"),bg="#393535",fg="white",cursor="hand2",width=16,command=reg)
        signupBtn.place(x=160,y=340)

    label = tk.Label(root,text="WELCOME", font=("Arial",23,"bold"),bg="#444444",foreground="white")
    label.place(x=130,y=20)

    frame2 = tk.Frame(root,bg="#222222",height=310,width=340)
    frame2.place(x=30,y=80)
    frame = tk.Frame(root,bg="#444444",height=270,width=300)
    frame.place(x=50,y=100)

    userLabel = tk.Label(root,text="Username:",font=("Arial",14),bg="#444444",fg="white")
    userLabel.place(x=70,y=130)

    userEntry = tk.Entry(root,font=10,width=15)
    userEntry.place(x=180,y=132)

    passLabel = tk.Label(root,text="Password:",font=("Arial",14),bg="#444444",fg="white")
    passLabel.place(x=70,y=170)

    passEntry = tk.Entry(root,show="•",font=10,width=15)
    passEntry.place(x=180,y=170)

    loginBtn = tk.Button(root,text="Log in",font=("Arial",15,"bold"),bg="#393535",fg="white",cursor="hand2",command=login)
    loginBtn.place(x=210,y=203)

    label2 = tk.Label(root,text="Forgot Password?",cursor="hand2",font=("Times",9),fg="blue",bg="#444444")
    label2.place(x=80,y=215)
    label2.bind("<Button-1>", forgot)

    frame3 = tk.Frame(root,width=280,height=2,bg="#333333")
    frame3.place(x=60,y=260)
    signupBtn = tk.Button(root,text="Create new account",font=("Arial",15,"bold"),bg="#393535",fg="white",cursor="hand2",command=signup)
    signupBtn.place(x=97,y=285)

    root.mainloop()

window()