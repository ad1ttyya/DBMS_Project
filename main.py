import tkinter as tk

root=tk.Tk()

root.geometry("1000x600")
root.title('DBMS_PROJECT')

def table1_page():
    table1_frame = tk.Frame(main_frame)
    
    lb =tk.Label(table1_frame , text='table 1 page \n \n page:1',font=("Bold",30))
    lb.pack()
    
    table1_frame.pack(pady=20)


def table2_page():
    table2_frame = tk.Frame(main_frame)
    
    lb =tk.Label(table2_frame , text='table 2 page \n \n page:1',font=("Bold",30))
    lb.pack()
    
    table2_frame.pack(pady=20)
    
    
def table3_page():
    table3_frame = tk.Frame(main_frame)
    
    lb =tk.Label(table3_frame , text='table 3 page \n \n page:1',font=("Bold",30))
    lb.pack()
    
    table3_frame.pack(pady=20)


def hide_indicators():
    table1_indicate.config(bg="#c3c3c3")
    table2_indicate.config(bg="#c3c3c3")
    table3_indicate.config(bg="#c3c3c3")
    

#for deleteing previos page data bfor enew load  
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
    
    
def indicate(lb, page):
    hide_indicators()   #hiding indicaot before new touch
    lb.config(bg='#158aff')
    delete_pages()
    page()


#----------------------------------------option _frame _work _here-----------------------------------------
options_frame = tk.Frame(root,bg="#c3c3c3")#option vala frame 

table1_btn = tk.Button(options_frame,text="TABLE_1",font=('Bold',15),fg='#158aff',bd=0
                       ,bg='#c3c3c3',command=lambda: indicate(table1_indicate , table1_page) )
table1_btn.place(x=10,y=50)# next button 50 then 100 for buttondistance

table1_indicate = tk.Label(options_frame, text = '' , bg='#c3c3c3')
table1_indicate.place(x=3 , y=50 , width=5 , height=40) 

table2_btn = tk.Button(options_frame,text="TABLE_2",font=('Bold',15),fg='#158aff',bd=0
                       ,bg='#c3c3c3',command=lambda: indicate(table2_indicate , table2_page) )
table2_btn.place(x=10,y=100)

table2_indicate = tk.Label(options_frame, text = '' , bg='#c3c3c3')
table2_indicate.place(x=3 , y=100 , width=5 , height=40) 

table3_btn = tk.Button(options_frame,text="TABLE_3",font=('Bold',15),fg='#158aff',bd=0
                       ,bg='#c3c3c3',command=lambda: indicate(table3_indicate , table1_page) )
table3_btn.place(x=10,y=150)

table3_indicate = tk.Label(options_frame, text = '' , bg='#c3c3c3')
table3_indicate.place(x=3 , y=150 , width=5 , height=40) 

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=150,height=600)

#-------------------------------------main_frame_work_here------------------------------------------------

main_frame = tk.Frame(root,highlightbackground="black",highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=850,height=600)


root.mainloop()
