'''
Creator - Anurag Thakur, gui frontpage (recreating from a screenshot)
Thursday,17-2-22
Workflow : 
1. make frames
2. make changes frame wise
'''
#importing libraries

from tkinter import *
from tkinter import ttk


#basic main structure

root = Tk()
root_width = root.winfo_screenwidth()
root_height = root.winfo_screenheight()
root.geometry("%dx%d" % (root_width,root_height))
root.title("First Page GUI")
icon = PhotoImage(file = 'icon.png')
root.iconphoto(False,icon)



'''
frame structure :-
1-2
 3
456
  7
'''
#making frame width and frame height for all 7 frames
frm1_width = (2*root_width/3)
frm1_height = (root_height/15)
frm2_width = (root_width/3)
frm2_height = (root_height/15)
frm3_width = (root_width)
frm3_height = (10*root_height/15)
frm4_width = (root_width/3)
frm4_height = (4*root_height/15)
frm5_width = (root_width/3)
frm5_height = (4*root_height/15)
frm6_width = (root_width/3)
frm6_height = (2.7*root_height/15)
frm7_width = (root_width/3)
frm7_height = (1.3*root_height/15)


#making frames (all 7)
frm1 = Frame(root,width=frm1_width,height=frm1_height)
frm2 = Frame(root,width=frm2_width,height=frm2_height)
frm3 = Frame(root,width=frm3_width,height=frm3_height)
frm4 = Frame(root,width=frm4_width,height=frm4_height,borderwidth=2,relief='raised')
frm5 = Frame(root,width=frm5_width,height=frm5_height,borderwidth=2,relief='raised')
frm6 = Frame(root,width=frm6_width,height=frm6_height,borderwidth=2,relief='raised')
frm7 = Frame(root,width=frm7_width,height=frm7_height)


#getting frames on screen
#even if we remove column and column span the code still works the same, don't know why
#it has around 3 rows and 3 columns as per my understanding
frm1.grid(row=0,column=0,columnspan=4,sticky=W)
frm2.grid(row=0,column=2,columnspan=2,sticky=E)
frm3.grid(row=1,column=0,columnspan=4)
frm4.grid(row=3,column=0,columnspan=2,sticky=W)
frm5.grid(row=3,column=1,columnspan=2)
frm6.grid(row=3,column=2,columnspan=2,sticky=NE)
frm7.grid(row=3,column=2,columnspan=2,sticky=SE)

#turning off propagation so the frame size doesn't change with labels
frm1.propagate(0) #0 or False is used to turn off propation
frm2.propagate(0)
frm3.propagate(0)
frm4.propagate(0)
frm5.propagate(0)
frm6.propagate(0)
frm7.propagate(0)

#additionally turning off grid_propagate
frm1.grid_propagate(0) #0 or False is used to turn off propation
frm2.grid_propagate(0)
frm3.grid_propagate(0)
frm4.grid_propagate(0)
frm5.grid_propagate(0)
frm6.grid_propagate(0)
frm7.grid_propagate(0)


#-------Editing Frame-1--------
sensor_label = Label(frm1,text="Radio Altimeter", font=15)
sensor_label.grid(row=0,column=0,padx=20,pady=8)
s_entry_var = StringVar()
sensor_entry = Entry(frm1,textvariable=s_entry_var,width=55,font=15,borderwidth=4,relief='sunken')
sensor_entry.insert(0,'hcft-5gps143')
sensor_entry.grid(row=0,column=1,columnspan=2,padx=20,pady=7)


#-------Editing Frame-2-------
f2_label1 = Label(frm2,text="28:01:11:10",width=10,bg='#7B7B7C',fg='white')
f2_label1.grid(row=0,column=0,padx=30,pady=14)

#making radio buttons
rvariable = IntVar()
rvariable.set("1") #setting default to 1
r1 = Radiobutton(frm2,text="RS-422",variable=rvariable,value=1,width=10,bg='#7B7B7C',fg='white',selectcolor="#7B7B7C",activebackground='black',activeforeground='green')
r2 = Radiobutton(frm2,text="MIL-STD-1553",variable=rvariable,value=2,width=10,bg='#7B7B7C',fg='white',selectcolor="#7B7B7C",activebackground='black',activeforeground='green')
r1.grid(row=0,column=1,padx=(30,0),pady=9)
r2.grid(row=0,column=2)


#--------Editing Frame-3--------
#we have to use tabs
#firstly creating tabs
'''
Process of tab creation:-
1. making tab control inside desired frame/root
2. creating tabs with it
3. add text to the tabs
4. display the tabs on screen
'''
#Create Tab Control, the Notebook method manages collections of windows and displays one at a time
#creating it inside frame-3
TAB_CONTROL = ttk.Notebook(frm3)

#creating tabs, ttk.Frame can also be used
Data_tab = Frame(TAB_CONTROL)
Graph_tab = Frame(TAB_CONTROL,bg='brown')

#adding tabs
TAB_CONTROL.add(Data_tab,text="Data")
TAB_CONTROL.add(Graph_tab,text="Graph")

#packing tabs to screen
TAB_CONTROL.pack(expand=1,fill='both')


#making 11 frames for different data for putting listbox in all of them
dataframe1 = Frame(Data_tab,height=frm3_height,width=(frm3_width/11))
dataframe2 = Frame(Data_tab,height=frm3_height,width=(frm3_width/11))
dataframe3 = Frame(Data_tab,height=frm3_height,width=(frm3_width/11))
dataframe4 = Frame(Data_tab,height=frm3_height,width=(frm3_width/11))
dataframe5 = Frame(Data_tab,height=frm3_height,width=(frm3_width/11))
dataframe6 = Frame(Data_tab,height=frm3_height,width=(frm3_width/11))
dataframe7 = Frame(Data_tab,height=frm3_height,width=(frm3_width/11))
dataframe8 = Frame(Data_tab,height=frm3_height,width=(frm3_width/11))
dataframe9 = Frame(Data_tab,height=frm3_height,width=(frm3_width/11))
dataframe10 = Frame(Data_tab,height=frm3_height,width=(frm3_width/11))
dataframe11 = Frame(Data_tab,height=frm3_height,width=(frm3_width/11))

#Turning off grid_propagate
dataframe1.grid_propagate(0)
dataframe2.grid_propagate(0)
dataframe3.grid_propagate(0)
dataframe4.grid_propagate(0)
dataframe5.grid_propagate(0)
dataframe6.grid_propagate(0)
dataframe7.grid_propagate(0)
dataframe8.grid_propagate(0)
dataframe9.grid_propagate(0)
dataframe10.grid_propagate(0)
dataframe11.grid_propagate(0)

#Turning off pack_propagate
dataframe1.propagate(0)
dataframe2.propagate(0)
dataframe3.propagate(0)
dataframe4.propagate(0)
dataframe5.propagate(0)
dataframe6.propagate(0)
dataframe7.propagate(0)
dataframe8.propagate(0)
dataframe9.propagate(0)
dataframe10.propagate(0)
dataframe11.propagate(0)

#putting dataframes on screen
dataframe1.grid(row=0,column=0)
dataframe2.grid(row=0,column=1)
dataframe3.grid(row=0,column=2)
dataframe4.grid(row=0,column=3)
dataframe5.grid(row=0,column=4)
dataframe6.grid(row=0,column=5)
dataframe7.grid(row=0,column=6)
dataframe8.grid(row=0,column=7)
dataframe9.grid(row=0,column=8)
dataframe10.grid(row=0,column=9)
dataframe11.grid(row=0,column=10)

#making top labels of each frame
datalabel1 = Label(dataframe1,text="SEQ NO")
datalabel2 = Label(dataframe2,text="VAL")
datalabel3 = Label(dataframe3,text="ALT(m)")
datalabel4 = Label(dataframe4,text="GPS(m)")
datalabel5 = Label(dataframe5,text="FD(KHz)")
datalabel6 = Label(dataframe6,text="SNR-U")
datalabel7 = Label(dataframe7,text="SNR-D")
datalabel8 = Label(dataframe8,text="FB-U(Khz)")
datalabel9 = Label(dataframe9,text="FB-D(KHz)")
datalabel10 = Label(dataframe10,text="FR(KHz)")
datalabel11 = Label(dataframe11,text="TIME(s)")

#putting labels into respective frames, using pack to get centered labels
datalabel1.pack()
datalabel2.pack()
datalabel3.pack()
datalabel4.pack()
datalabel5.pack()
datalabel6.pack()
datalabel7.pack()
datalabel8.pack()
datalabel9.pack()
datalabel10.pack()
datalabel11.pack()

'''
Procedure of making scrollable listboxes (used here) :-
1.Create Scrollbar
2.Display it on the screen
3.Create Listboxes
4.Display it on the screen
5.Atach listbox to scrollbar
6.setting up scrollbar to get the desired view on scrolling
'''

#Creating Scrollbars
scrollbar1 = Scrollbar(dataframe1,cursor="dotbox")
scrollbar2 = Scrollbar(dataframe2,cursor="dotbox")
scrollbar3 = Scrollbar(dataframe3,cursor="dotbox")
scrollbar4 = Scrollbar(dataframe4,cursor="dotbox")
scrollbar5 = Scrollbar(dataframe5,cursor="dotbox")
scrollbar6 = Scrollbar(dataframe6,cursor="dotbox")
scrollbar7 = Scrollbar(dataframe7,cursor="dotbox")
scrollbar8 = Scrollbar(dataframe8,cursor="dotbox")
scrollbar9 = Scrollbar(dataframe9,cursor="dotbox")
scrollbar10 = Scrollbar(dataframe10,cursor="dotbox")
scrollbar11 = Scrollbar(dataframe11,cursor="dotbox")


#packing to screen
scrollbar1.pack(side=RIGHT,fill='both')
scrollbar2.pack(side=RIGHT,fill='both')
scrollbar3.pack(side=RIGHT,fill='both')
scrollbar4.pack(side=RIGHT,fill='both')
scrollbar5.pack(side=RIGHT,fill='both')
scrollbar6.pack(side=RIGHT,fill='both')
scrollbar7.pack(side=RIGHT,fill='both')
scrollbar8.pack(side=RIGHT,fill='both')
scrollbar9.pack(side=RIGHT,fill='both')
scrollbar10.pack(side=RIGHT,fill='both')
scrollbar11.pack(side=RIGHT,fill='both')

#creating listboxes
listbox1 = Listbox(dataframe1,bg="#7B7B7C",fg='white')
listbox2 = Listbox(dataframe2,bg="#7B7B7C",fg='white')
listbox3 = Listbox(dataframe3,bg="#7B7B7C",fg='white')
listbox4 = Listbox(dataframe4,bg="#7B7B7C",fg='white')
listbox5 = Listbox(dataframe5,bg="#7B7B7C",fg='white')
listbox6 = Listbox(dataframe6,bg="#7B7B7C",fg='white')
listbox7 = Listbox(dataframe7,bg="#7B7B7C",fg='white')
listbox8 = Listbox(dataframe8,bg="#7B7B7C",fg='white')
listbox9 = Listbox(dataframe9,bg="#7B7B7C",fg='white')
listbox10 = Listbox(dataframe10,bg="#7B7B7C",fg='white')
listbox11 = Listbox(dataframe11,bg="#7B7B7C",fg='white')

#displaying using pack
listbox1.pack(side=LEFT,fill='both')
listbox2.pack(side=LEFT,fill='both')
listbox3.pack(side=LEFT,fill='both')
listbox4.pack(side=LEFT,fill='both')
listbox5.pack(side=LEFT,fill='both')
listbox6.pack(side=LEFT,fill='both')
listbox7.pack(side=LEFT,fill='both')
listbox8.pack(side=LEFT,fill='both')
listbox9.pack(side=LEFT,fill='both')
listbox10.pack(side=LEFT,fill='both')
listbox11.pack(side=LEFT,fill='both')

#configuring and attaching scrollbar to listbox
listbox1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=listbox1.yview)
listbox2.config(yscrollcommand=scrollbar2.set)
scrollbar2.config(command=listbox2.yview)
listbox3.config(yscrollcommand=scrollbar3.set)
scrollbar3.config(command=listbox3.yview)
listbox4.config(yscrollcommand=scrollbar4.set)
scrollbar4.config(command=listbox4.yview)
listbox5.config(yscrollcommand=scrollbar5.set)
scrollbar5.config(command=listbox5.yview)
listbox6.config(yscrollcommand=scrollbar6.set)
scrollbar6.config(command=listbox6.yview)
listbox7.config(yscrollcommand=scrollbar7.set)
scrollbar7.config(command=listbox7.yview)
listbox8.config(yscrollcommand=scrollbar8.set)
scrollbar8.config(command=listbox8.yview)
listbox9.config(yscrollcommand=scrollbar9.set)
scrollbar9.config(command=listbox9.yview)
listbox10.config(yscrollcommand=scrollbar10.set)
scrollbar10.config(command=listbox10.yview)
listbox11.config(yscrollcommand=scrollbar11.set)
scrollbar11.config(command=listbox11.yview)

#garbage code to fill the listboxes
"""for values in range(100):
    listbox1.insert(END, values)
for values in range(100):
    listbox2.insert(END, values)"""


#---------Editing Frame-4----------
#making tabs Health and Transmit
TAB_CONTROL2 = ttk.Notebook(frm4)

#creating tabs
Health_tab = Frame(TAB_CONTROL2)
Transmit_tab = Frame(TAB_CONTROL2,bg="green")

#adding the tabs
TAB_CONTROL2.add(Health_tab,text="Health")
TAB_CONTROL2.add(Transmit_tab,text="Transmit")

#packing the tabs to the screen
TAB_CONTROL2.pack(expand=1,fill='both')

#we will use grid system inside,4 rows 3 columns

#creating labels
expected_label = Label(Health_tab,text="Expected")
read_label = Label(Health_tab,text="READ")
pwr_label = Label(Health_tab,text="PWR ON ACK")
version_label = Label(Health_tab,text="VERSION")
txstatus_label = Label(Health_tab,text="Tx STATUS")

#creating entry widgets (for textboxes)
Expected_textbox1 = Entry(Health_tab)
Expected_textbox2 = Entry(Health_tab)
Expected_textbox3 = Entry(Health_tab)
read_textbox1 = Entry(Health_tab)
read_textbox2 = Entry(Health_tab)
read_textbox3 = Entry(Health_tab)

#placing on screen
expected_label.grid(row=0,column=1,padx=10,pady=10,sticky="nsew")
read_label.grid(row=0,column=2,padx=10,pady=10,sticky="nsew")
pwr_label.grid(row=1,column=0,padx=10,pady=5,sticky="nsew")
version_label.grid(row=2,column=0,padx=10,pady=5,sticky="nsew")
txstatus_label.grid(row=3,column=0,padx=10,pady=5,sticky="nsew")
Expected_textbox1.grid(row=1,column=1,padx=10,pady=5,sticky="nsew")
Expected_textbox2.grid(row=2,column=1,padx=10,pady=5,sticky="nsew")
Expected_textbox3.grid(row=3,column=1,padx=10,pady=5,sticky="nsew")
read_textbox1.grid(row=1,column=2,padx=10,pady=5,sticky="nsew")
read_textbox2.grid(row=2,column=2,padx=10,pady=5,sticky="nsew")
read_textbox3.grid(row=3,column=2,padx=10,pady=5,sticky="nsew")

#inserting default values
Expected_textbox1.insert(0,"0x00")
Expected_textbox2.insert(0,"dd/mm/yy Vx.x")
Expected_textbox3.insert(0,"ON/OFF:AA/55")
read_textbox1.insert(0,"-")
read_textbox2.insert(0,"-")
read_textbox3.insert(0,"-")

#disabling all the boxes as we don't want the user to alter it
Expected_textbox1.configure(state='disabled')
Expected_textbox2.configure(state='disabled')
Expected_textbox3.configure(state='disabled')
read_textbox1.configure(state='disabled')
read_textbox2.configure(state='disabled')
read_textbox3.configure(state='disabled')


#--------Editing Frame-5---------
#making label 
interface_control_label = Label(frm5,text="Interface Controls",width=25)

#making buttons
pwron_button = Button(frm5,text="PWR ON",bg="lightgreen")
txon_button = Button(frm5,text="Tx-ON",bg="lightgreen")
hltchk_button = Button(frm5,text="HLT CHK",bg="lightgreen")
pwroff_buttton = Button(frm5,text="PWR OFF",bg="#8B0000")
txoff_button = Button(frm5,text="Tx-OFF",bg="#8B0000")
quit_button = Button(frm5,text="Quit",bg="#EE4B2B",command=root.destroy)

#placing using pack, wasn't able to align them on top of each other, therefore used grid
"""interface_control_label.pack()
pwron_button.pack(side=LEFT,fill='x')
txon_button.pack(side=LEFT,fill='x')
hltchk_button.pack(side=LEFT,fill='x')
pwroff_buttton.pack(side=RIGHT,fill='x')
txoff_button.pack(side=RIGHT,fill='x')
quit_button.pack(side=RIGHT,fill='x')"""


#placing on screen using grid
interface_control_label.grid(row=0,column=1,sticky="nsew",padx=0,pady=7)
pwron_button.grid(row=1,column=0,sticky="nsew",padx=(45,20),pady=7)
txon_button.grid(row=2,column=0,sticky="nsew",padx=(45,20),pady=7)
hltchk_button.grid(row=3,column=0,sticky="nsew",padx=(45,20),pady=7)
pwroff_buttton.grid(row=1,column=2,sticky="nsew",padx=(20,45),pady=7)
txoff_button.grid(row=2,column=2,sticky="nsew",padx=(20,45),pady=7)
quit_button.grid(row=3,column=2,sticky="nsew",padx=(20,45),pady=7)


#--------Editing Frame-6-----------
#creating top label
hob_label = Label(frm6,text="Enter HOB")

#creating variable for entry widget, a default value of 0 is shown in the entry widget(if IntVar)
hob_var = StringVar()
#print(type(hob_var))

#creating entry widget
hob_entry = Entry(frm6,textvariable=hob_var,fg='red')
#print(type(hob_entry.get()))

#creating label to show result
result_label = Label(frm6,text="RESULT")

#showing on screen
hob_label.grid(row=0,column=0,sticky=W,padx=50,pady=7)
hob_entry.grid(row=1,column=0,sticky="nsew",padx=50,pady=30)
result_label.grid(row=1,column=1,sticky="nsew",padx=50,pady=30)

#as of now, just using bind with enter to change the result label(as functionality has not been told)
#defining handler fuction, it requires an attribute by default
def handler(self):
  if hob_entry.get()=="20":
    result_label.config(text="PASS",fg='green')
  else:  
    try:
      if type(int(hob_entry.get()))==int:
        result_label.config(text="FAIL",fg='red')
    except:
      result_label.config(text="INVALID",fg='red')
#binding 
hob_entry.bind('<Return>',handler) #handler is a funtion that we define above,Return means enter key


#---------Editing Frame-7-----------
#making scrollbar
frm7_scrollbar = Scrollbar(frm7)

#making listbox
frm7_listbox = Listbox(frm7,fg='green',width=int(frm7_width))

#attaching scrollbar and listbox
frm7_listbox.configure(yscrollcommand=frm7_scrollbar.set)
frm7_scrollbar.configure(command=frm7_listbox.yview)

#packing on screen
frm7_scrollbar.pack(side=RIGHT,fill='both')
frm7_listbox.pack(side=LEFT,fill='x')

#putting text as shown in screen shot
frm7_listbox.insert(0,"TX-on response received sent")



#running the program
root.mainloop()