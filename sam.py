from tkinter import *  #importing evrything from tkinter library
from tkinter.filedialog import askopenfilename #importing filedialog in order to select the files dynamically
import pandas as pd #importing pandas in order to perform statistical operations on the given data
import numpy as np
import time #imported time as a module 
import csv #imported csv library in order to perform operations such as opening,editing,appending
import matplotlib.pyplot as plt #in order to develop beautiful analytical graphs
from tkinter import messagebox
localtime=time.asctime(time.localtime(time.time())) #it is giving us the right now time on the standard indian time
#--------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------#

def import_csv_data():
    global v
    global data
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    df = pd.read_csv(csv_file_path,na_values=["not available","n.a."])
    data.set(df)
#--------------------------------------------------------------------------------#
def dup(): #it is a fucntion which checks the for two duplicates in the data base 
	#print(file_name)
	file_name = v.get() #naming the file and getting the file name from v string variable
	df = pd.read_csv(file_name, sep="\t or ,")
	# Notes:
	# - the `subset=None` means that every column is used 
	#    to determine if two rows are different; to change that specify
	#    the columns as an array
	# - the `inplace=True` means that the data structure is changed and
	#   the duplicate rows are gone  
	df.drop_duplicates(subset=None, inplace=True)
	# Write the results to a different file
	df.to_csv(file_name,index=False,sep="\t")
	var = messagebox.showinfo("Congratulations Your Data is Now Unique!!!" ,"Hence All Duplicates are removed from the file")#invokes a new window for giving the indication that duplicates are removed


 #--------------------------------------------------------------------------------#
def sdm():


	window=Tk()
	window.geometry("1600x900+0+0")
	window.title("Data")
	window.configure(background="tan1")


	Top = Frame(window,bg="steel blue",width = 1600,height=1000)
	Top.pack(side=TOP)
	f1 = Frame(window,bg="light grey",width = 600,height=850)
	f1.pack(anchor=CENTER,pady=100)
	Label(Top, font=( 'Helvetica' ,38,'bold' ),text="Student Data Manager 2.0 ",bg="black",fg="white").grid(row=0,column=0,sticky=W)
#--------------------------------------------------------------------------------------------------------

	Label(f1, font=( 'Helvetica',20),text=" Name :  ",fg="steel blue").grid(row=0,column=0)
	na=StringVar()
	Entry(f1,textvariable=na,font=('Helvetica',20),bg="powder blue" ,justify='center').grid(row=0,column=1)
	
	
	Label(f1, font=( 'Helvetica',20 ),text=" Roll No :  ",fg="steel blue").grid(row=1,column=0)
	ro=IntVar()
	Entry(f1,textvariable=ro,font=('Helvetica',20),bg="powder blue" ,justify='center').grid(row=1,column=1)
	
	Label(f1, font=( 'Helvetica',20 ),text=" Branch :  ",fg="steel blue").grid(row=2,column=0)
	br=StringVar()
	Entry(f1,textvariable=br,font=('Helvetica',20),bg="powder blue" ,justify='center').grid(row=2,column=1)
	
	Label(f1, font=( 'Helvetica',20 ),text=" Year :  ",fg="steel blue").grid(row=3,column=0)
	ye=IntVar()
	Entry(f1,textvariable=ye,font=('Helvetica',20),bg="powder blue" ,justify='center').grid(row=3,column=1)
	
	Label(f1, font=( 'Helvetica',20 ),text=" Section :  ",fg="steel blue").grid(row=4,column=0)
	se=StringVar()
	Entry(f1,textvariable=se,font=('Helvetica',20),bg="powder blue" ,justify='center').grid(row=4,column=1)
	

	Label(f1, font=( 'Helvetica',20 ),text=" Subjects ",fg="steel blue").grid(row=5,column=0)
	Label(f1, font=( 'Helvetica',20 ),text=" Marks ",fg="steel blue").grid(row=5,column=1)

	Label(f1, font=( 'Helvetica',20 ),text=" Python : ",fg="steel blue").grid(row=6,column=0)
	py=DoubleVar()
	Entry(f1,textvariable=py,font=('Helvetica',20),bg="powder blue" ,justify='center').grid(row=6,column=1)
	
	Label(f1, font=( 'Helvetica',20 ),text=" ADBMS : ",fg="steel blue").grid(row=7,column=0)
	ad=DoubleVar()
	Entry(f1,textvariable=ad,font=('Helvetica',20),bg="powder blue" ,justify='center').grid(row=7,column=1)
	

	Label(f1, font=( 'Helvetica',20 ),text=" Data Structure : ",fg="steel blue").grid(row=8,column=0)
	dss=DoubleVar()	
	Entry(f1,textvariable=dss,font=('Helvetica',20),bg="powder blue" ,justify='center').grid(row=8,column=1)
	
	def line1():
		#graph between Roll No and Python Marks
		x=[]
		y=[]
		with open('database.csv','r+') as f:
			has_header=csv.Sniffer().has_header(f.read(16384))
			f.seek(0)
			p=csv.reader(f,delimiter=',')
			if has_header:
				next(p)
			for row in p:
				x.append(int(row[0]))
				y.append(int(row[5]))

		plt.plot(x,y,marker='o')
		plt.title('Students marks Vs Roll no')
		plt.xlabel('roll no')
		plt.ylabel('Python marks')
		plt.show()

	def line2():
		#graph between Roll No and Data Structure Marks
		x=[]
		y=[]
		with open('database.csv','r+') as f:
			has_header=csv.Sniffer().has_header(f.read(16384))
			f.seek(0)
			p=csv.reader(f,delimiter=',')
			if has_header:
				next(p)
			for row in p:
				x.append(int(row[0]))
				y.append(int(row[6]))

		plt.plot(x,y,marker='o')
		plt.title('Students marks Vs Roll no')
		plt.xlabel('roll no')
		plt.ylabel('Data Structure marks')
		plt.show()	
	
	def line3():
		#graph between Roll No and Python Marks
		x=[]
		y=[]
		with open('database.csv','r+') as f:
			has_header=csv.Sniffer().has_header(f.read(16384))
			f.seek(0)
			p=csv.reader(f,delimiter=',')
			if has_header:
				next(p)
			for row in p:
				x.append(int(row[0]))
				y.append(int(row[6]))

		plt.plot(x,y,marker='o')
		plt.title('Students marks Vs Roll no')
		plt.xlabel('roll no')
		plt.ylabel('ADBMS marks')
		plt.show()
	
	def pie():
		size_of_groups=["2","3","2","3","1","2"]
		# Create a pieplot
		labels=["DA","UCA","FUll Stack 8","Java","Pega","UX"]
		explode=(0.1,0.1,0.1,0.1,0.1,0.1)
		fig1,ax1=plt.subplots()
		ax1.pie(size_of_groups,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
		ax1.axis('equal')
		plt.title("Sections Present in database")
		my_circle=plt.Circle( (0,0), 0.2, color='grey')
		p=plt.gcf()
		p.gca().add_artist(my_circle)
		plt.tight_layout()
		plt.show()

	def bar():
		x=[]
		y=[]
		z=[]
		c=[]
		a=0
		#extract data from csv
		with open('database.csv','r') as csvfile:
			plots=csv.reader(csvfile,delimiter=',')
			next(plots,None)
			for row in plots:
				x.append(int((row[0])))
				y.append(int((row[5])))
				z.append(int((row[6])))
				c.append(int((row[7])))
			a=np.arange(len(y))
			#sorting the roll no in order
		#plot data
		#use border to put bars in front of grid
		bar_width=0.3
		plt.bar(a,y,width=bar_width,label="PYTHON",color="red",zorder=2)
		plt.bar(a+bar_width,z,width=bar_width,label="Data Structure",color="green",zorder=2)
		plt.bar(a+bar_width+bar_width,c,width=bar_width,label="ADBMS",color="blue",zorder=2)

		#labels
		plt.xticks(a+bar_width/2,x)
		plt.xlabel("Roll No")
		plt.title("Marks in Data Structure,Python and ADBMS ")
		plt.legend(["PYTHON","Data Structure","ADBMS"])
		
		#axis
		plt.grid(axis="y")
		plt.show()
	def learn_graph():
		pass	
	def stats():
		win=Tk()
		win.geometry("500x300")
		win.title("Graphical Analysis")
		win.configure(background='steel blue')
		#Label(win,font=('Helvetica',20),bg="powder blue" ,justify='center',text=localtime).pack()

		def python():
			file_path=v.get()
			df = pd.read_csv(file_path,na_values=["not available","n.a."])
			Label(win,text="Summary of Python",font=('Times New Roman',20,'bold'),justify='center',bg="powder blue").grid(row=0,column=0)
			mean1 = df['Python'].mean() # calculates the average of all values 
			sum1 = df['Python'].sum() # calculates the sum of all values 
			max1 = df['Python'].max() # calculates the max of all values
			min1 = df['Python'].min() # calculates the min of all values 
			count1 = df['Python'].count() # calculates the count of all values 
			median1 = df['Python'].median () # calculates the median of all values
			mode1 = df['Python'].mode () # calculates the mode of all values
			struct="The average of marks in Python is: "+str(mean1)+"\nThe sum of marks in Python is: "+str(sum1)+"\nThe max of marks in Python is: " + str(max1)+"\nThe min of marks in Python is: " + str(min1)+"\nThe count of students in Python is: " + str(count1)+"\nThe median of marks in Python is:" + str(median1)
			Label(win,text=struct,font=('comic sans ms',8,'bold'),bg="powder blue").grid(row=1,column=0)
	
		def data_struc():
			file_path=v.get()
			df = pd.read_csv(file_path,na_values=["not available","n.a."])
			Label(win,text="Summary of Data Structure",font=('Times New Roman',20,'bold'),justify='center',bg="powder blue").grid(row=0,column=0)
			mean1 = df['Data Structure'].mean() # calculates the average of all values 
			sum1 = df['Data Structure'].sum() # calculates the sum of all values 
			max1 = df['Data Structure'].max() # calculates the max of all na_values
			min1 = df['Data Structure'].min() # calculates the min of all values 
			count1 = df['Data Structure'].count() # calculates the count of all values 
			median1 = df['Data Structure'].median () # calculates the median of all values
			mode1 = df['Data Structure'].mode () # calculates the mode of all values
			struct="The average of marks in DS is: "+str(mean1)+"\nThe sum of marks in DS is: "+str(sum1)+"\nThe max of marks in DS is: " + str(max1)+"\nThe min of marks in DS is: " + str(min1)+"\nThe count of students in DS is: " + str(count1)+"\nThe median of marks in DS is:" + str(median1)
			Label(win,text=struct,font=('comic sans ms',8,'bold'),bg="powder blue").grid(row=1,column=0)
		
		def dbms():
			file_path=v.get()
			df = pd.read_csv(file_path,na_values=["not available","n.a."])
			Label(win,text="Summary of ADBMS",font=('Times New Roman',20,'bold'),justify='center',bg="powder blue").grid(row=0,column=0)
			mean1 = df['ADBMS'].mean() # calculates the average of all values 
			sum1 = df['ADBMS'].sum() # calculates the sum of all values 
			max1 = df['ADBMS'].max() # calculates the max of all na_values
			min1 = df['ADBMS'].min() # calculates the min of all values 
			count1 = df['ADBMS'].count() # calculates the count of all values 
			median1 = df['ADBMS'].median () # calculates the median of all values
			mode1 = df['ADBMS'].mode () # calculates the mode of all values
			struct="The average of marks in ADMS is: "+str(mean1)+"\nThe sum of marks in ADBMS is: "+str(sum1)+"\nThe max of marks in ADBMS is: " + str(max1)+"\nThe min of marks in ADBMS is: " + str(min1)+"\nThe count of students in ADBMS is: " + str(count1)+"\nThe median of marks in ADBMS is:" + str(median1)
			Label(win,text=struct,font=('comic sans ms',8,'bold'),bg="powder blue").grid(row=1,column=0)

		def learn():
			#getting dataset ready for the predication using multi value linear regression
			file_path=v.get()
			df = pd.read_csv(file_path,na_values=["not available","n.a."])
			x=df[['Python','Data Structure']]
			y=df['ADBMS']
			from sklearn.model_selection import train_test_split
			X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.8, random_state=0)

			#training the machine 
			from sklearn.linear_model import LinearRegression
			regressor = LinearRegression()
			regressor.fit(X_train, y_train)

			#now prediction starts and it is stored in y_pred

			y_pred = regressor.predict(X_test)
			df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
			Label(win,text="Prediction of ADBMS Marks",font=('Times New Roman',20,'bold'),justify='center',bg="powder blue").grid(row=0,column=0)
			Label(win,text=pd.DataFrame({'Actual': y_test, 'Predicted': y_pred}),font=('comic sans ms',8,'bold'),bg="powder blue").grid(row=1,column=0)
			
			






		menubar = Menu(win)
		linegraph=Menu(menubar,tearoff=0)
		linegraph.add_command(label="Python Analysis", command=line1)
		linegraph.add_separator()
		linegraph.add_command(label="Data Structure Analysis", command=line2)
		linegraph.add_separator()
		linegraph.add_command(label="ADBMS Analysis", command=line3)
		linegraph.add_separator()
		linegraph.add_command(label="Exit", command=win.destroy)
		menubar.add_cascade(label="LINE GRAPH", menu=linegraph)

		# create more pulldown menus
		piechart = Menu(menubar, tearoff=0)
		piechart.add_command(label="Contribution of Section", command=pie)
		menubar.add_cascade(label="PIE GRAPH", menu=piechart)

		barr=Menu(menubar,tearoff=0)
		barr.add_command(label="Marks of Each Student",command=bar)
		menubar.add_cascade(label="BAR CHART",menu=barr)

		analy = Menu(menubar, tearoff=0)
		analy.add_command(label="Python Analysis", command=python)
		analy.add_separator()
		analy.add_command(label="Data Structure Analysis", command=data_struc)
		analy.add_separator()
		analy.add_command(label="ADBMS Analysis", command=dbms)
		menubar.add_cascade(label="DATA ANALYSIS", menu=analy)

		pred=Menu(menubar,tearoff=0)
		pred.add_command(label="Prediction of ADBMS Marks",command=learn)
		menubar.add_cascade(label="PREDICATION",menu=pred)

		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label="About")
		menubar.add_cascade(label="Help", menu=helpmenu)
		# display the menu
		win.config(menu=menubar)
		win.mainloop()


	def submit():
		var1 = messagebox.showwarning("Maintenance Going On" ,"Please refer to the CLI Mode.\nSorry for Inconvenience")	
		name=na.get()
		Roll=ro.get()
		branch=br.get()
		year=ye.get()
		section=se.get()
		python=py.get()
		adbms=ad.get()
		ds=dss.get()
		a=list()
		name=input("Enter Your Name : ")
		Roll=int(input("Enter Your Roll No : "))
		branch=input("Enter Your Branch : ")
		year=int(input("Enter your year : "))
		section=input("Enter your Section : ")
		print("********************************Enter Your Marks************************************** \n")
		python=int(input("Enter Your Python Marks : "))
		adbms=int(input("Enter Your ADBMS Marks : "))
		ds=int(input("Enter Your Data Structure Marks : "))
		a.append(Roll)
		a.append(name)
		a.append(branch)
		a.append(year)
		a.append(section)
		a.append(python)
		a.append(ds)
		a.append(adbms)
	
		with open('database.csv', 'a', newline='') as csvfile:
			fieldnames = ['Roll_No','Name','Branch','Year','Section','Python','Data_Structure','ADBMS']
			spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
			spamwriter.writerow({'Roll_No':a[0],'Name':a[1],'Branch':a[2],'Year':a[3],'Section':a[4],'Python':a[5],'Data_Structure':a[6],'ADBMS':a[7]})
			var = messagebox.showinfo("Data Added !!!" ,"Your Record has been updated to the database.")	

	Button(f1,font=('Helvetica',20),bg="powder blue" ,justify='center',text="Statistcal Representation",command=stats).grid(row=9,column=0)
	Button(f1,font=('Helvetica',20),bg="powder blue" ,justify='center',text="SUBMIT",command=submit).grid(row=9,column=1)
	window.mainloop()	

def search():
	rol=Tk()
	rol.geometry("900x500")
	rol.configure(background="steel blue")
	rol.title("Searching Data........")
	def searching():
		#a=text_search.get()
		var1 = messagebox.showwarning("Maintenance Going On" ,"Please refer to the CLI Mode.\nSorry for Inconvenience")	
		a=int(input("***********************************Enter The Roll Number To View The Record********************************************\n"))
		var = messagebox.showinfo("**Information**" ,"For Records Please See the Search Data Window")
		with open('database.csv','r') as searchfile:
			searchit=csv.reader(searchfile)
			for row in searchit:
				for field in row:
					if(field==str(a)):
						form=row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6]+" "+row[7]
						Label(rol,text=form,font=('Helvetica',20),bg="steel blue").grid(row=4,column=0)
						return 
		var = messagebox.showerror("Soryy!!!!" ,"Your Record Does not Exist, Please check your Roll No")

	text_search=IntVar()
	Label(rol,text="Enter Your Roll Number",font=('Helvetica',20),bg="light blue").grid(row=0,column=0)
	Entry(rol,textvariable=text_search,font=('Helvetica',20),bg="light blue" ,width=10).grid(row=1,column=0)
	Button(rol,font=('Helvetica',20),bg="light blue" ,text="SEARCH",command=searching).grid(row=2,column=0)
	Label(rol,text="   Roll Name Branch Year Section Python Data Structure ADBMS",font=('Helvetica',20),bg="light blue").grid(row=3,column=0)



	rol.mainloop()


def delete():
	rol=Tk()
	rol.geometry("430x130")
	rol.configure(background="misty rose")
	rol.title("Deleting Data........")
	def searching():
		a=int(input("***********************************Enter The Index Number from DATA To Delete The Record********************************************"))
		df = pd.read_csv('data.csv',na_values=["not available","n.a."])
		df.drop([a],axis=0,inplace=True)					
	text_search=IntVar()
	Label(rol,text="Enter Roll Number To Delete Data",font=('Helvetica',20),bg="light blue").grid(row=0,column=0)
	Entry(rol,textvariable=text_search,font=('Helvetica',20),bg="light blue" ,width=10).grid(row=1,column=0)
	Button(rol,font=('Helvetica',20),bg="light blue" ,text="Delete",command=searching).grid(row=2,column=0)


	rol.mainloop()






def syn():
	doodle = Tk()
	doodle.title("Synopsis")
	text = Text(doodle,font=('Helvetica',18),bg="powder blue",width=500,height=600,)
	text.insert(INSERT, "Project Name:Py-Drawer\n")
	text.insert(INSERT, "Product Name:Student Data Manager 2.0\n")
	text.insert(INSERT,"Instuctions:\n")
	text.insert(INSERT,"1. Firstly Just click on the browse button and load the file database.csv\n")
	text.insert(INSERT,"2. We have given a  tool for Duplicacy Checking so click on the button checkk duplicate \n")
	text.insert(INSERT,"3. We have given you a button to close the software\n")
	text.insert(INSERT,"4. There is a field on the home page which shows you the data in the csv file.\n")
	text.insert(INSERT,"5. Now to get the data of a specific roll number click on the menubar button and enter the Roll No to get the record\n")
	text.insert(INSERT,"6. Now if you want to delete the specific data of a student so you can click on the delete and enter the roll number but it is a beta function\n")
	text.insert(INSERT,"7. Now click on insert data button to get the form in which enter the data and click on submit\n")
	text.insert(INSERT,"8. Now click on the statistcal Representation button to get the data Analysis option window\n")
	text.insert(INSERT,"9. Here you will get a lot of visualizations :- \n")
	text.insert(INSERT,"10. You can get line graph by click on LINE GRAPH button at menubar.\n")
	text.insert(INSERT,"11. You can get Bar graph by click on BAR GRAPH button at menubar.\n")
	text.insert(INSERT,"12. You can get Pie graph by clicking on the PIE GRAPH button at menubar\n")
	text.insert(INSERT,"13. You can Analysis the marks of students in python,data structures and ADBMS\n")
	text.insert(INSERT,"14. You can see the predicted marks on the basis of two suubject marks.\n")
	text.insert(INSERT,"Team:-\n")
	text.insert(INSERT,"Py-Doodlers\n")
	text.insert(INSERT,"Akanksha Singh 1610991059\n")
	text.insert(INSERT,"Anirudh Mishra 1610991110\n")
	text.pack()
	doodle.mainloop()


def team():
	doodle = Tk()
	doodle.title("Py-Doodlers")
	text = Text(doodle,font=('Helvetica',18),bg="powder blue",width=500,height=600,)
	text.insert(INSERT, "Project Name:Py-Drawer\n")
	text.insert(INSERT, "Product Name:Student Data Manager 2.0\n")
	text.insert(INSERT,"Description:\n")
	text.insert(INSERT,"Our product will have following keyfeatures which will make it unique and classic:-\n")
	text.insert(INSERT,"1. A tool for Duplicacy Checking\n")
	text.insert(INSERT,"2. A tool for selecting any kind of csv file dynamically\n")
	text.insert(INSERT,"3. writing and reading the csv file\n")
	text.insert(INSERT,"Now main features :-\n")
	text.insert(INSERT,"1. Our app can analyze the data from csv file and can give you some statistcal results to you.\n")
	text.insert(INSERT,"2. You can get graphical view of data selected by you\n")
	text.insert(INSERT,"3. You can get Prediction of third subject marks from combination of other two subject marks.\n")
	text.insert(INSERT,"4. We have used A tool from machine learning which is known as Linear Regression\n")
	text.insert(INSERT,"Future Developments:-\n")
	text.insert(INSERT,"1. Using Django making it fit for any size of screen.\n")
	text.insert(INSERT,"2. Using Some Ml tools some basic predication can be shown.\n")
	text.insert(INSERT,"Technical Description:\n")
	text.insert(INSERT,"		-tkinter module\n")
	text.insert(INSERT,"		-csv\n")
	text.insert(INSERT,"		-pandas\n")
	text.insert(INSERT,"		-numpy\n")
	text.insert(INSERT,"		-skitlearn\n")
	text.insert(INSERT,"		-matplot.lib\n")
	text.insert(INSERT,"		-django(In future version of our product)\n")
	text.insert(INSERT,"Team:-\n")
	text.insert(INSERT,"Py-Doodlers\n")
	text.insert(INSERT,"Akanksha Singh 1610991059\n")
	text.insert(INSERT,"Anirudh Mishra 1610991110\n")
	text.grid(row=0,column=0)
	doodle.mainloop()


#--------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("1260x1200")
filename = PhotoImage(file = "image.gif")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
var = messagebox.showinfo("Welcome to the Student Data Manager 2.0" ,"Please Read the Instuctions Before Using the Product")


Top = Frame(root,bg="steel blue",width = 1600,height=1000)
Top.pack(side=TOP)
Label(Top, font=( 'Helvetica' ,38,'bold' ),text="Student Data Manager 2.0",bg="black",fg="white").grid(row=0,column=0,sticky=W)



f3 = Frame(root,bg="misty rose",width =100,height=400)
f3.pack(pady=150,anchor=CENTER)

f2 = Frame(root,bg="powder blue",width =900,height=150)
f2.pack(anchor=CENTER)

data=StringVar()
Label(f2,text="DATA",font=('Times New Roman',20,'bold'),justify='center',bg="powder blue").grid(row=0,column=0)
Label(f2,textvariable=data,font=('comic sans ms',8,'bold'),bg="powder blue").grid(row=1,column=0)

Label(f3,font=('Helvetica',12),bg="powder blue" ,justify='center',text='File Path').grid(row=1, column=0)
v = StringVar()
entry = Entry(f3,font=('Helvetica',12),bg="powder blue" ,justify='center',textvariable=v,width=40).grid(row=1, column=1)
Button(f3,font=('Helvetica',12),bg="powder blue" ,justify='center',text='Browse Data Set',command=import_csv_data).grid(row=2, column=0)
Button(f3,font=('Helvetica',12),bg="powder blue" ,justify='center',text='Close',command=root.destroy).grid(row=2, column=1)#it closes the application
Button(f3,font=('Helvetica',12),bg="powder blue" ,justify='center',text='Check For Duplicates',command=dup).grid(row=2,column=2,)# this calls the function to check the data for the duplicates 
Button(f3,font=('Helvetica',12),bg="powder blue" ,justify='center',text='Insert Data',command=sdm).grid(row=2,column=3,padx=20)#this calls the function to get the data from the user in order to append the data in the csv file
root.title("Student Data Manager 2.0")#this gives the title to our main window 
#menu bar at main page
men=Menu(root)
sear=Menu(men,tearoff=0)
sear.add_command(label="Search For Record",command=search)
sear.add_separator()
sear.add_command(label="Delete Data(Beta)",command=delete)
men.add_cascade(label="File Explorer",menu=sear)

mai=Menu(men, tearoff=0)
mai.add_command(label="Synopsis", command=syn)
mai.add_separator()
mai.add_command(label="Py-Doodlers", command=team)
men.add_cascade(label="About", menu=mai)

root.config(menu=men)
root.mainloop()

'''
-----------------------------------------------------------------------------------------------------------------------------------------------------
Developed By :- ANICODEV Co. Inc.
-----------------------------------------------------------------------------------------------------------------------------------------------------
'''