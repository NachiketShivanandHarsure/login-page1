from tkinter import*
from PIL import ImageTk
def login_page():
    signup_window.destroy()
    import signinpage

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)

background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold')
              ,bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25)

emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,stick='w',padx=25)


usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,stick='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,stick='w',padx=25)


confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmpasswordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
confirmpasswordEntry.grid(row=8,column=0,stick='w',padx=25)


termsandconditions=Checkbutton(frame,text='I agree to the Terms & Condition',font=('Microsoft Yahei UI Light',9,'bold'),
                               fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2')
termsandconditions.grid(row=9,column=0,pady=10,padx=15)



signupButton=Button(frame,text='Signup',font=('open sans',16,'bold'),
                   fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=17)
signupButton.grid(row=10,column=0,pady=10)


alreadyaccount=Label(frame,text="Dont have an account?",font=('Open Sans','9','bold'),fg='firebrick1',bg='white')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)


loginButton=Button(frame,text='Log in',font=('open sans',9,'bold underline')
                   ,bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=156,y=405)

signup_window.mainloop()