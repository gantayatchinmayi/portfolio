from tkinter import*
from tkinter import messagebox 
import csv
from pymysql import * 
conobj = connect (host = "localhost", user = 'root', password = '', port = 3306)
curobj = conobj . cursor ()
curobj . execute ('use project;')

win1=Tk ()
#=======================================================

def Reset () :
	AUid.delete(0,END)
	APwd.delete(0,END)
#-------------
def Exit () :
	win1.destroy()
#-------------------
def Login() :
	x=AUid.get())
	y=Apwd.get())
	r='select * from admin where Auser="{}" and Apwd ="{}" ;'.format (x,y)
	curobj.execute(r)
	record=curobj.fetchall()
	if len (record):
		win1.destroy()
		messagebox.showinfo("Login Successfully ","Welcome To Admin Home Page")
		win2=Tk()

#=====================================================
		def AddStudent() :
			win2.destroy()
			win3=Tk()
			#===============================
			def Submit() :
				#print(SRegNo.get(),SName.get(),Accyear.get(),Dept.get(),SPwd.get())
				r = 'insert into Student (Regno,Name, Accyear, Department, Password)values  ({}, "{}", "{}", "{}", "{}");' . format (SRegNo.get(),SName.get(),Accyear.get(),Dept.get(),SPwd.get())
				curobj . execute (r)
				conobj . commit ()

			def Reset() :
				SRegNo.delete(0,END)
				SName.delete(0,END)
				Dept.set("---Select Dept Name : ---")
				Accyear.set("---Select Acc Year : ---")
				SPwd.delete(0,END)

			def Exit() :
				win3.destroy() 
			#===============================
			win3.maxsize(600,600)
			win3.minsize(600,600)
			win3.configure(bg="#ccfb5d")
			win3.title("Add New Student ")
			Label(win3,text="Student Regstration Number",font=('Ebrima',15),bg="#fbe7a1",fg="blue",width=25,height=1,relief="groove").place(x=20,y=50)
			SRegNo=Entry (win3,font=('Ebrima',14),bg="white",fg="blue",width=20)
			SRegNo.place(x=320,y=50)
			
			Label(win3,text="Student Name",font=('Ebrima',15),bg="#fbe7a1",fg="blue",width=25,height=1,relief="groove").place(x=20,y=150)
			
			SName=Entry (win3,font=('Ebrima',14),bg="white",fg="blue",width=20)
			SName.place(x=320,y=150)


			Label(win3,text="Student Acc Year ",font=('Ebrima',15),bg="#fbe7a1",fg="blue",width=25,height=1 ,relief="groove").place(x=20,y=250)
			Accyear=StringVar()
			Accyear.set("---Select Any Acc Year :--- ")
			menu1=OptionMenu(win3 ,Accyear,"2019-2023","2020-2024","2021-2025","2022-2026","2023-2027","2024-2028")
			
			menu1.place(x=320,y=250)
			
			Label(win3,text="Student Dept Name ",font=('Ebrima',15),bg="#fbe7a1",fg="blue",width=25,height=1 ,relief="groove").place(x=20,y=350)
			
			Dept=StringVar()
			Dept.set("-----Select Dept Name :---- ")
			menu2=OptionMenu(win3 ,Dept,"EEE","CSE","CSEIT","ME","ECE","CIVIL")
			menu2.place(x=320,y=350)
			Label(win3,text="Enter Password",font=('Ebrima',15),bg="#fbe7a1",fg="blue",width=25,height=1 ,relief="groove").place(x=20,y=450)
			SPwd=Entry (win3,font=('Ebrima',14),bg="white",fg="blue",width=20,relief="groove",show="*")
			SPwd.place(x=320,y=450)
		
			Button(win3,text="RESET",font=('Ebrima',15),width=8,height=1,bg="#daee01",fg="red",activebackground="#ccfb5d",relief="raised",command=Reset).place(x=50,y=510)


			Button(win3,text="SUBMIT",font=('Ebrima',15),width=8,height=1,bg="#daee01",fg="red",activebackground="#ccfb5d",relief="raised",command=Submit).place(x=210,y=510)

			Button(win3,text="EXIT",font=('Ebrima',15),width=8,height=1,bg="#7d0552",fg="white",activebackground="#ccfb5d",relief="raised",command=Exit).place(x=380,y=510)


			


			win3.mainloop()
		#=======================
		def DownloadStudent() :
			curobj . execute("select * from Student ;")
			record = curobj.fetchall()
			fobj=open("Studentdentails.txt","w")
			fobj1=open("Student.csv","w",newline="\n")
			cobj=csv.writer(fobj1)
			cobj.writerow(["Regno","Name","ParentName","Gender","Accyear "," Department","Contact", "Password"])
			for row in record :
				fobj.write(str(row))
				cobj.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])

				fobj.write("\n")
			
			fobj.close()
			messagebox.showinfo("Download complete","Thank you ")
			win2.destroy()
		#=======================
		def Exit () :
			win2.destroy()
#=============================================
		win2.maxsize(500,400)
		win2.minsize(500,400)
		win2.configure(bg="#ccfb5d")
		win2.title("Admin Home Page ")
		Button(win2,text="Add New Student",font=('Ebrima',15),width=25,height=2,bg="#800080",fg="white",activebackground="#ccfb5d",relief="raised",command=AddStudent).place(x=50,y=50)


		Button(win2,text="Download Student Details",font=('Ebrima',15),width=25,height=2,bg="#800080",fg="white",activebackground="#ccfb5d",relief="raised",command=DownloadStudent).place(x=50,y=150)

		Button(win2,text="Exit",font=('Ebrima',15),width=15,height=2,bg="red",fg="white",activebackground="#ccfb5d",relief="raised",command=Exit).place(x=100,y=250)
		win2.mainloop()
	else : 
		print("Invalid Login")
		win1.destroy()




#=================================================================
#win1.geometry('500x500')
win1.maxsize(500,500)
win1.minsize(500,500)
win1.title("Admin_Login_Page")
win1.configure(bg="#ccfb5d")


Label(win1,text="Admin Login Here ",font=('Ebrima',20),bg="#fbe7a1",fg="blue",width=33,relief="raised").place(x=0,y=100)

Label(win1,text="Admin User Id ",font=('Ebrima',15),bg="#fbe7a1",fg="blue",width=15,relief="groove").place(x=30,y=200)
AUid=Entry (win1,font=('Ebrima',15),bg="#fbe7a1",fg="blue",width=20)
AUid.place(x=250,y=200)

Label(win1,text="Admin Password ",font=('Ebrima',15),bg="#fbe7a1",fg="blue",width=15,relief="groove").place(x=30,y=300)
APwd=Entry (win1,font=('Ebrima',15),bg="#fbe7a1",fg="blue",width=20,show="*")
APwd.place(x=250,y=300)

# Button on Admin page
Button(win1,text="RESET",font=('Ebrima',15),width=8,height=1,bg="#daee01",fg="red",activebackground="#ccfb5d",relief="raised",command=Reset).place(x=30,y=400)


Button(win1,text="LOGIN",font=('Ebrima',15),width=8,height=1,bg="#daee01",fg="red",activebackground="#ccfb5d",relief="raised",command=Login).place(x=190,y=400)

Button(win1,text="EXIT",font=('Ebrima',15),width=8,height=1,bg="#7d0552",fg="white",activebackground="#ccfb5d",relief="raised",command=Exit).place(x=360,y=400)




win1.mainloop()