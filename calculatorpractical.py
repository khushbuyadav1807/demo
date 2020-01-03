from tkinter import*

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator= total
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=int(eval(operator))
    operator= total
    text_Input.set(sumup)
    
    

cal = Tk()
cal.title("calculator")
operator=""
text_Input =IntVar()

txtDisplay =Entry(cal,font=('arial',20,'bold'),textvariable=text_Input, bd=30, insertwidth=5,bg="powder blue",justify='right').grid(columnspan=6)

btn7=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=1,column=2)

Addition=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="+",bg="powder blue",command=lambda:btnClick("+")).grid(row=1,column=3)
#=====================================================================================================================================================
btn6=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=2,column=0)

btn5=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=2,column=1)

btn4=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=2,column=2)

Substraction=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="-",bg="powder blue",command=lambda:btnClick("-")).grid(row=2,column=3)
#=====================================================================================================================================================

btn3=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=3,column=0)

btn2=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=3,column=1)

btn1=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=3,column=2)

multiplication=Button(cal,padx=16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="*",bg="powder blue",command=lambda:btnClick("*")).grid(row=3,column=3)
#======================================================================================================================================================


btn0=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=4,column=0)

btnClear=Button(cal,padx= 16,bd=8,pady=16,fg="black",font=('arial',20,'bold'), text="C",bg="powder blue",command=btnClearDisplay).grid(row=4,column=1)

btnDot=Button(cal,padx= 16,bd=8,pady=16 ,fg="black",font=('arial',20,'bold'), text=".",bg="powder blue",command=lambda:btnClick(".")).grid(row=4,column=2)

Division=Button(cal,padx= 16,bd=8,pady=16, fg="black",font=('arial',20,'bold'), text="/",bg="powder blue",command=lambda:btnClick("/")).grid(row=4,column=3)

btnEquals=Button(cal,padx=150,bd=8,pady=16 ,fg="black",font=('ariel',20,'bold'),text="=",bg="powder blue",command=btnEqualsInput).place(x=9,y=480)

cal.mainloop()

