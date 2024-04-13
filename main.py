import tkinter as tk
from tkinter import *
from tkinter import messagebox
from backend import *
#-------------------------------------------------------------------------


def window_main():
    root=tk.Tk()
    root.geometry("1000x600")
    root.title('DBMS_PROJECT')
    
    
    def table1_page():
        table1_frame = tk.Frame(main_frame)
        data = table1()
        total_rows = len(data)
        total_columns = len(data[0])
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(table1_frame, width=20, fg='blue', font=('Arial',16,'bold'))
                e.grid(row=i, column=j)
                e.insert(END, data[i][j])
        table1_frame.pack(pady=20)
        
 
    def table2_page():
        table2_frame = tk.Frame(main_frame)
        data = table2()
        total_rows = len(data)
        total_columns = len(data[0])
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(table2_frame, width=20, fg='blue', font=('Arial',16,'bold'))
                e.grid(row=i, column=j)
                e.insert(END, data[i][j])
        table2_frame.pack(pady=20) 
 
 
    def table3_page():
        table3_frame = tk.Frame(main_frame)
        data = table3()
        total_rows = len(data)
        total_columns = len(data[0])
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(table3_frame, width=20, fg='blue', font=('Arial',16,'bold'))
                e.grid(row=i, column=j)
                e.insert(END, data[i][j])
        table3_frame.pack(pady=20) 
        
        
    def table4_page():
        table4_frame = tk.Frame(main_frame)
        lb =tk.Label(table4_frame , text='table 4 page \n \n page:4',font=("Bold",30))
        lb.pack()
        table4_frame.pack(pady=20) 
        
    
    def table5_page():
        table5_frame = tk.Frame(main_frame)
        lb =tk.Label(table5_frame , text='table 5 page \n \n page:5',font=("Bold",30))
        lb.pack()
        table5_frame.pack(pady=20) 
        
        
    def table6_page():
        table6_frame = tk.Frame(main_frame)
        lb =tk.Label(table6_frame , text='table 6 page \n \n page:6',font=("Bold",30))
        lb.pack()
        table6_frame.pack(pady=20)
    
        
    def hide_indicators():
        table1_indicate.config(bg="#c3c3c3")
        table2_indicate.config(bg="#c3c3c3")
        table3_indicate.config(bg="#c3c3c3")
        table4_indicate.config(bg="#c3c3c3")
        table5_indicate.config(bg="#c3c3c3")
        table6_indicate.config(bg="#c3c3c3")
        
        
    def delete_pages():
        for frame in main_frame.winfo_children():
            frame.destroy()
            
            
    def indicate(lb, page):
        hide_indicators()   #hiding indicaot before new touch
        lb.config(bg='#158aff')
        delete_pages()
        page()
        
        
#-------------------------------------------------------------------------   


    options_frame = tk.Frame(root,bg="#c3c3c3")#option vala frame 
    
    
    table1_btn = tk.Button(options_frame,text="ITEM_LIST",font=('Bold',15),fg='#158aff',bd=0
                        ,bg='#c3c3c3',command=lambda: indicate(table1_indicate , table1_page) )
    table1_btn.place(x=10,y=50)
    table1_indicate = tk.Label(options_frame, text = '' , bg='#c3c3c3')
    table1_indicate.place(x=3 , y=50 , width=5 , height=40)    
    
    
    table2_btn = tk.Button(options_frame,text="IN_STOCK",font=('Bold',15),fg='#158aff',bd=0
                        ,bg='#c3c3c3',command=lambda: indicate(table2_indicate , table2_page) )
    table2_btn.place(x=10,y=100)
    table2_indicate = tk.Label(options_frame, text = '' , bg='#c3c3c3')
    table2_indicate.place(x=3 , y=100 , width=5 , height=40)   


    table3_btn = tk.Button(options_frame,text="OUT_STOCK",font=('Bold',15),fg='#158aff',bd=0
                        ,bg='#c3c3c3',command=lambda: indicate(table3_indicate , table3_page) )
    table3_btn.place(x=10,y=150)
    table3_indicate = tk.Label(options_frame, text = '' , bg='#c3c3c3')
    table3_indicate.place(x=3 , y=150 , width=5 , height=40) 
    
    
    table4_btn = tk.Button(options_frame,text="ADD_ITEM",font=('Bold',15),fg='#158aff',bd=0
                        ,bg='#c3c3c3',command=lambda: indicate(table4_indicate , table4_page) )
    table4_btn.place(x=10,y=200)
    table4_indicate = tk.Label(options_frame, text = '' , bg='#c3c3c3')
    table4_indicate.place(x=3 , y=200 , width=5 , height=40) 

    
    table5_btn = tk.Button(options_frame,text="DELETE_ITEM",font=('Bold',15),fg='#158aff',bd=0
                        ,bg='#c3c3c3',command=lambda: indicate(table5_indicate , table5_page) )
    table5_btn.place(x=10,y=250)
    table5_indicate = tk.Label(options_frame, text = '' , bg='#c3c3c3')
    table5_indicate.place(x=3 , y=250 , width=5 , height=40) 
    
    
    table6_btn = tk.Button(options_frame,text="EDIT_ITEM",font=('Bold',15),fg='#158aff',bd=0
                        ,bg='#c3c3c3',command=lambda: indicate(table6_indicate , table6_page) )
    table6_btn.place(x=10,y=300)
    table6_indicate = tk.Label(options_frame, text = '' , bg='#c3c3c3')
    table6_indicate.place(x=3 , y=300 , width=5 , height=40)
    
    
    options_frame.pack(side=tk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=150,height=600) 
    
    
#-------------------------------------------------------------------------

    main_frame = tk.Frame(root,highlightbackground="black",highlightthickness=2)

    main_frame.pack(side=tk.LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(width=850,height=600)

    root.mainloop()
    
#-------------------------------------------------------------------------


def window_login():
    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Check if username and password are correct
        if username == "a" and password == "a":
            messagebox.showinfo("Login Successful", "Welcome, Admin!" )
            
            window_main() 
            #code to close previous window will come here
            
            # You can add code here to open a new window or perform any action after successful login
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

    # Create the main window
    root = tk.Tk()
    root.title("Login Page")
    root.geometry("300x200")

    # Create username label and entry
    username_label = tk.Label(root, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    # Create password label and entry
    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    # Create login button
    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack()

    # Run the main event loop
    root.mainloop()


#-------------------------------------------------------------------------

window_main()
# window_login()

