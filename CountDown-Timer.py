#CountDown Timer

#Importing Modules

import tkinter as tk
from datetime import datetime

#Taking input from user

seconds=int(input("Enter time in seconds for countdown:"))
print('''A CountDown Timer Window is created in background.
Minimize the tabs to use Countdown timer.^_^''')
timer=66600+seconds
run=False

#Defing function for CountDown Timer

def label_timer(label):

    def running():

        
        global timer
        global run

        if run:

            
            if timer>=66600:

                
                tt = datetime.fromtimestamp(timer)
                string = tt.strftime("%H:%M:%S")
                display=string

                
            else:

                
                display="Time Up.."
                run=False 

            label['text']=display  

            label.after(1000, running)  

            timer -= 1 

    running()

#Start Button function

    
def Start(label):

    global run 

    run=True
    
    label_timer(label)
    
    start['state']='disabled'

    stop['state']='normal'

    resume['state']='disabled'

    reset['state']='normal'

    
#Stop Button function

    
def Stop(label):
    
    global run 

    run=False

    start['state']='disabled'

    stop['state']='disabled'

    resume['state']='normal'

    reset['state']='normal'

    
    
#Resume Button function


def Resume(label):

    global run 

    run=True

    label_timer(label)

    start['state']='disabled'

    stop['state']='normal'

    resume['state']='disabled'

    reset['state']='normal'

# Reset Button function 


def Reset(label):
    
    global timer
    
    timer=66600+seconds

    tt1 = datetime.fromtimestamp(timer)
    
    string1= tt1.strftime("%H:%M:%S")
    
    display1=string1

    label['text']=display1

    global run 

    run=False

    label_timer(label)

    start['state']='normal'
    
    stop['state']='disabled'

    resume['state']='disabled'

    reset['state']='disabled'



#Title of the Window
    
root = tk.Tk()

root.title("Stopwatch")


# Fixing the size of Window. 


root.minsize(width=650, height=300) 

label = tk.Label(root, text="CountDown..!", fg="red",bg="white", font="Verdana 30 bold") 

label.pack() 

f = tk.Frame(root)


#Attributes of Buttons which are created inside Window


start = tk.Button(f, text='Start', width=20, fg="red",bg="white" ,bd=10,
                  activeforeground="Orange",activebackground="white",
                  highlightcolor="purple",justify="right",padx=10,
                  pady=10,relief="groove",command=lambda:Start(label)) 

stop = tk.Button(f, text='Stop/Pause',width=20,fg="red",bg="white" ,bd=10,
                 activeforeground="Orange",activebackground="white",
                 highlightcolor="purple",justify="right",padx=10,pady=10,
                 relief="groove",state='disabled', command=lambda:Stop(label)) 

resume = tk.Button(f, text='Resume', width=20, fg="red",bg="white",bd=10,
                   activeforeground="Orange",activebackground="white",
                   highlightcolor="purple",justify="right",padx=10,pady=10,
                   relief="groove",state='disabled',
                   command=lambda:Resume(label) )

reset = tk.Button(f, text='Reset',width=20, fg="red",bg="white",bd=10,
                  activeforeground="Orange",activebackground="white",
                  highlightcolor="purple",justify="right",padx=10,pady=10,
                  relief="groove",state='disabled',command=lambda:Reset(label))

f.pack(anchor = 'center',pady=20)

start.pack(side="left") 

stop.pack(side ="left") 

resume.pack(side="left")

reset.pack(side="left")

label1 = tk.Label(root, text="Timer",fg="white", bg="blue" ,
                  font="Verdana 30 bold")

label1.pack()

root.mainloop()

