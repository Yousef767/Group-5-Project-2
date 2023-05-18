from tkinter import *
import random
import tkinter.messagebox as mb
root = Tk()
root.title("Tile Matching Game")
root.geometry ("500x550")

# Create matches
matches = [1,1,2,2,3,3,4,4,5,5,6,6]

# Shuffle matches
random.shuffle(matches)

# Define variables
count = 0
answer_list=[]
answer_dict={}

# Set win counter
global win_counter
win_counter = 0

# Define reset function
def reset():
    global win_counter,matches
    matches = [1,1,2,2,3,3,4,4,5,5,6,6]
    random.shuffle(matches)
    win_counter=0
    label.config(text='')
    btn_list = [btn0,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11]
    for btn in btn_list:
        btn.config(bg='SystemButtonFace',state='normal',text=' ')



# Define click button function
def click_event(btn,num):
    global count,answer_list,answer_dict,win_counter
    if btn["text"] == ' ' and count < 2:
        btn["text"] = matches[num]
        # Add number to answer list
        answer_list.append(num)
        # Add button and number to answer dictionary
        answer_dict[btn]=matches[num]
        # Increase counter
        count += 1
    #Check if the answer is correct
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            label.config(text='Correct Match !')
            for key in answer_dict:
                key["state"] = "disabled"
            # Reset variables to default
            count =0
            answer_list=[]
            answer_dict={}
            # Increase winner counter
            win_counter += 1
            # When user win 
            if win_counter == 6:
                btn_list = [btn0,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11]
                label.config(text='You Won !')
                for btn in btn_list:
                    btn.config(bg='lightblue')
        else :
            #if the match is wrong
            label.config(text='Wrong Match !')
            mb.showinfo('INFO','Wrong Match !')
            count =0
            answer_list=[]
            # Reset the buttons
            for key in answer_dict:
              key["text"] = " "
            answer_dict={}


# Create the frame
frame = Frame(root)
frame.pack(pady=10)

# Create info label
label = Label(root,font=('Giddyup Std',15),fg='blue')
label.pack(pady=10)

# Create reset btn
reset_btn = Button(root,text='Rest',padx=20,pady=7,borderwidth=1, relief="solid",command=reset,font=('Giddyup Std',15))
reset_btn.pack()

# Define our buttons
btn0 = Button(frame,text=' ',font=('Giddyup Std',20),width=6,height=3,command=lambda:click_event(btn0,0))
btn1 = Button(frame,text=' ',font=('Giddyup Std',20),width=6,height=3,command=lambda:click_event(btn1,1))
btn2 = Button(frame,text=' ',font=('Giddyup Std',20),width=6,height=3,command=lambda:click_event(btn2,2))
btn3 = Button(frame,text=' ',font=('Giddyup Std',20),width=6,height=3,command=lambda:click_event(btn3,3))
btn4 = Button(frame,text=' ',font=('Giddyup Std',20),width=6,height=3,command=lambda:click_event(btn4,4))
btn5 = Button(frame,text=' ',font=('Giddyup Std',20),width=6,height=3,command=lambda:click_event(btn5,5))
btn6 = Button(frame,text=' ',font=('Giddyup Std',20),width=6,height=3,command=lambda:click_event(btn6,6))
btn7 = Button(frame,text=' ',font=('Giddyup Std',20),width=6,height=3,command=lambda:click_event(btn7,7))
btn8 = Button(frame,text=' ',font=('Giddyup Std',20),width=6,height=3,command=lambda:click_event(btn8,8))
btn9 = Button(frame,text=' ',font=('Giddyup Std',20),width=6,height=3,command=lambda:click_event(btn9,9))
btn10 = Button(frame,text=' ',font=('Giddyup Std',20),width=6,height=3,command=lambda:click_event(btn10,10))
btn11 = Button(frame,text=' ',font=('Giddyup Std',20),width=6,height=3,command=lambda:click_event(btn11,11))

# Grid our Buttons
btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=1, column=3)
btn8.grid(row=2, column=0)
btn9.grid(row=2, column=1)
btn10.grid(row=2, column=2)
btn11.grid(row=2, column=3)

root.mainloop()