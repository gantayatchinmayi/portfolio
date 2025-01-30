from tkinter import*
from tkinter import messagebox 

from pymysql import * 
conobj = connect (host = "localhost", user = 'root', password = '', port = 3306)
curobj = conobj . cursor ()
curobj . execute ('use project;')

win1=Tk ()
#=======================================================
def Reset () :
	SRegno.delete(0,END)
	SName.delete(0,END)
	Dept.set("---Select Dept Name : ---")
	Accyear.set("---Select Acc Year : ---")
	SPwd.delete(0,END)	

#-------------
def Exit () :
	win1.destroy()
#-------------------
def Login() :
	p1=SRegno.get()
	p2=SPwd.get()
	p3=Accyear.get()
	#print(SRegno.get(),Accyear.get(),Dept.get(),SPwd.get())
	r= 'select * from Student where Regno ={} and Accyear="{}" and Department ="{}" and Password ="{}";'.format (SRegno.get(),Accyear.get(),Dept.get(),SPwd.get())
	curobj . execute (r)
	record = curobj.fetchall()
	if len (record):
		win1.destroy()
		win2=Tk()
		#========================
		def Update ():
			#print(URegno.get(),UName.get(),UPName.get(),UGender.get(),UAccyear.get(),UDept.get(),UCno.get(),UPwd.get())
			
		
			r='update Student set Name = "{}",Gender="{}",ParentName="{}",Contact="{}",Department ="{}",Password="{}" where Regno={} and Password="{}";'.format(UName.get(),UGender.get(),UPName.get(),UCno.get(),UDept.get(),UPwd.get(),p1,p2)
			print(r)
			
			curobj . execute (r)
			conobj.commit()
			win2.destroy()
			
			
		def Exit() :
			win2.destroy()
		def Reset() :
			URegno.delete(0,END)
			UName.delete(0,END)
			UPName.delete(0,END)
			UGender.set(None)
			UDept.set("---Select Dept Name : ---")
			UAccyear.set("---Select Acc Year : ---")
			UCno.delete(0,END)
			UPwd.delete(0,END)
		#========================
		win2.maxsize(1000,600)
		win2.minsize(1000,600)
		win2.title("Student_Login_Page")
		win2.configure(bg="#ccfb5d")
		Label(win2,text="Student RegNo  ",font=('Ebrima',13),bg="#fbe7a1",fg="blue",width=20,relief="groove").place(x=30,y=100)
		v1=StringVar(win2,value=p1)
		URegno=Entry (win2,textvariable=v1,font=('Ebrima',15),bg="white",fg="blue",width=20)
		URegno.place(x=250,y=100)
		
		Label(win2,text="Student Name   ",font=('Ebrima',13),bg="#fbe7a1",fg="blue",width=20,relief="groove").place(x=530,y=100)
		UName=Entry (win2,font=('Ebrima',15),bg="white",fg="blue",width=20)
		UName.place(x=750,y=100)
		
		Label(win2,text="Student Parent Name ",font=('Ebrima',13),bg="#fbe7a1",fg="blue",width=20,relief="groove").place(x=30,y=150)
		UPName=Entry (win2,font=('Ebrima',15),bg="white",fg="blue",width=20)
		UPName.place(x=250,y=150)
		
		Label(win2,text="Select Gender   ",font=('Ebrima',13),bg="#fbe7a1",fg="blue",width=20,relief="groove").place(x=530,y=150)
		UGender=StringVar()
		r1= Radiobutton(win2,text="Male",font=('Ebrima',13),variable =UGender,value ="M")
		r1.place(x=750,y=150)
		r2= Radiobutton(win2,text="Female",font=('Ebrima',13),variable= UGender ,value="F")
		r2.place(x=850,y=150)

		Label(win2,text="Select Academic Year ",font=('Ebrima',13),bg="#fbe7a1",fg="blue",width=20,relief="groove").place(x=30,y=200)
		UAccyear=StringVar()
		
		UAccyear.set(p3)
		menu1=OptionMenu(win2 ,UAccyear,"2019-2023","2020-2024","2021-2025","2022-2026","2023-2027","2024-2028")

		menu1.place(x=250,y=200)
		
		Label(win2,text="Select Dept Name ",font=('Ebrima',13),bg="#fbe7a1",fg="blue",width=20,relief="groove").place(x=530,y=200)
		UDept=StringVar()

		UDept.set("-----Select Dept Name :---- ")
		menu2=OptionMenu(win2 ,UDept,"EEE","CSE","CSEIT","ME","ECE","CIVIL")

		menu2.place(x=750,y=200)
		
		Label(win2,text="Student Contact Number",font=('Ebrima',13),bg="#fbe7a1",fg="blue",width=20,relief="groove").place(x=30,y=250)
		UCno=Entry (win2,font=('Ebrima',15),bg="white",fg="blue",width=20)
		UCno.place(x=250,y=250)
		
		Label(win2,text="Enter Password   ",font=('Ebrima',13),bg="#fbe7a1",fg="blue",width=20,relief="groove").place(x=530,y=250)
		v2=StringVar(win2,value=p2)

		UPwd=Entry (win2,textvariable=v2,font=('Ebrima',15),bg="white",fg="blue",width=20)
		UPwd.place(x=750,y=250)

		

		Button(win2,text="RESET",font=('Ebrima',15),width=8,height=1,bg="#daee01",fg="red",activebackground="#ccfb5d",relief="raised",command= Reset).place(x=90,y=400)

		Button(win2,text="UPDATE",font=('Ebrima',15),width=8,height=1,bg="#daee01",fg="red",activebackground="#ccfb5d",relief="raised",command= Update).place(x=450,y=400)

		Button(win2,text="EXIT",font=('Ebrima',15),width=8,height=1,bg="#7d0552",fg="white",activebackground="#ccfb5d",relief="raised",command= Exit).place(x=800,y=400)





		
	
		win2.mainloop()
	else: 
		
		messagebox.showinfo("Invalid Login ","Try again another time ")
		win1.destroy()
		
#=================================================================
#win1.geometry('500x500')
win1.maxsize(600,500)
win1.minsize(600,500)
win1.title("Student_Login_Page")
win1.configure(bg="#ccfb5d")


Label(win1,text="Student Login Here ",font=('Ebrima',20),bg="#fbe7a1",fg="blue",width=40,relief="raised").place(x=0,y=0)

Label(win1,text="Student RegNo  ",font=('Ebrima',13),bg="#fbe7a1",fg="blue",width=25,relief="groove").place(x=30,y=100)
SRegno=Entry (win1,font=('Ebrima',15),bg="#fbe7a1",fg="blue",width=20)
SRegno.place(x=300,y=100)

Label(win1,text="Select Accademic Year  ",font=('Ebrima',13),bg="#fbe7a1",fg="blue",width=25,relief="groove").place(x=30,y=150)
Accyear=StringVar()
Accyear.set("---Select Any Acc Year :--- ")
menu1=OptionMenu(win1 ,Accyear,"2019-2023","2020-2024","2021-2025","2022-2026","2023-2027","2024-2028")
menu1.place(x=300,y=150)



Label(win1,text="Select Department Name   ",font=('Ebrima',13),bg="#fbe7a1",fg="blue",width=25,relief="groove").place(x=30,y=200)
Dept=StringVar()
Dept.set("-----Select Dept Name :---- ")
menu2=OptionMenu(win1 ,Dept,"EEE","CSE","CSEIT","ME","ECE","CIVIL")
menu2.place(x=300,y=200)

Label(win1,text="Enter Password  ",font=('Ebrima',13),bg="#fbe7a1",fg="blue",width=25,relief="groove").place(x=30,y=250)
SPwd=Entry (win1,font=('Ebrima',15),bg="#fbe7a1",fg="blue",width=20,show="*")
SPwd.place(x=300,y=250)



Button(win1,text="RESET",font=('Ebrima',15),width=8,height=1,bg="#daee01",fg="red",activebackground="#ccfb5d",relief="raised",command=Reset).place(x=30,y=400)

Button(win1,text="LOGIN",font=('Ebrima',15),width=8,height=1,bg="#daee01",fg="red",activebackground="#ccfb5d",relief="raised",command=Login).place(x=190,y=400)

Button(win1,text="EXIT",font=('Ebrima',15),width=8,height=1,bg="#7d0552",fg="white",activebackground="#ccfb5d",relief="raised",command=Exit).place(x=360,y=400)




win1.mainloop()