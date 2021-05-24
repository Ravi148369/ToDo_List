from tkinter import *
from tkinter.messagebox import showerror, showinfo, showwarning 
root=Tk()
root.title("ToDo List")
root.configure(background="#00001a")

# Add task on text widget
i=0
def addTask():
    global i
    task=value.get()
    if(task==""):
        showinfo("Alert","Please enter the task")
        return 0
    i=i+1
    text.insert(END,f"{i}. {task}\n")
    value.delete(0,END)
    root.update()
    status_text.set(f"{i} pending task")
    root.update()

# to show previous task
def show_task():
    global i
    i=0
    showwarning("Warning","It'll destroy your present content")
    with open("C:\\Python32\\task.txt") as show:
        task_count=show.read()
        if(len(task_count)==1):
            showerror("Info","Your previous task list is empty")
            return 0
        text.insert(1.0,task_count)        
        for j in range(len(task_count)):
            if(task_count[j]=="\n"):
                i=i+1
        i=i-1
        status_text.set(f"{i} pending task")
        text.delete(f"{int(i)}.end")
        root.update()   
        
# delete task on text widget
def deleteTask():
    global i
    n=float(input("enter a task you want to delete :"))
    text.delete(n,f"{int(n)}.end")
    text.delete(n)
    for n in range(i):
        j=float(n)
        text.delete(j)
        text.insert(j,f"{n}") 
    i=i-1
    status_text.set(f"{i} pending task")
    root.update()

# clear the screen
def clear():
    global i
    text.delete(1.0,END)
    i=0
    status_text.set(f"{i} pending task")
    root.update()

# to save the file
def save():
    with open("task.txt","w") as save_file:
        save_file.write(text.get(1.0,END))
    exit()

# creating main label
f1=Frame(root)
sc=Scrollbar(f1)
sc.pack(side=RIGHT,fill=Y)
Label(root,text=" Your ToDo List",font="lucida 20 bold").pack(pady=20)
text=Text(f1,font="helvetica 10 bold",yscrollcommand=sc.set)
text.pack()
sc.config(command=text.yview)
f1.pack()

# creating label
Label(root,text="Enter your task here",font="lucida 15 bold").pack(pady=15)
scvalue=StringVar()
value=Entry(root,textvariable=scvalue,font="lucida 15 bold")
value.pack()

# buttons with frame
f=Frame(root,background="#00001a")
b1=Button(f,text="Add",background="green",command=addTask,font="lucida 15 bold",padx=10)
b1.pack(side=LEFT,padx=5)
b2=Button(f,text="Delete",background="red",command=deleteTask,font="lucida 15 bold")
b2.pack(side=RIGHT)
b3=Button(f,text="Clear",background="red",command=clear,font="lucida 15 bold")
b3.pack(padx=5,side=RIGHT)
b4=Button(f,text="Save & Exit",background="red",command=save,font="lucida 15 bold")
b4.pack(padx=5,side=RIGHT)
b5=Button(f,text="Show task",background="red",command=show_task,font="lucida 15 bold")
b5.pack(padx=5,side=RIGHT)
f.pack(pady=15)
# creating status bar
status_text=StringVar()
status_bar=Label(root,textvariable=status_text,anchor="w",relief=SUNKEN,font="lucida 12 bold",background="#00001a",fg="white")
status_bar.pack(side=BOTTOM,fill=X)

root.mainloop()