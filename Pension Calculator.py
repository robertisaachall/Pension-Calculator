from tkinter import * #Import whole module since we are using multiple widgets and functions.
from tkinter import messagebox as mb #Import this to use the messagebox function.



 
'''
Function that when called, tests all of the avaliable fields to ensure the user entered the correct formatted input.
i.e: 
-Must be numeric (no strings or characters)
-Must be non-negative (cannot be below 0)
-Must not be blank (cannot have no input for field)
-All three salaries cannot be zero (would have error down the line due to division, implementation in the function prevents this.)
-Both Years and age cannot be both zero(similar error as above but implemented to avoid weird output from the calculate_pension program).
Age, Years, and Months input can only be integers and this function checks to make sure of that.
Whenever it finds an illegal input, it uses the messagebox library to pop a window up to inform the user
of the field they got incorrect. 
If the function finds illegal input it returns a sentinel of -1 to denote this.
'''
def test_user_input():
    
   
    
     #First salary input validation section
    if first_entry.get() == "":
        mb.showerror("FIRST HIGHEST INPUT","Your frist salary input was invalid because it \nwas blank. Positive decimals and Numbers only!")
        return -1
    else:
        try:
            float(first_entry.get())
        except:
            mb.showerror("FIRST HIGHEST INPUT","Your frist salary input was invalid because it \ncontained illegal characters. Positive decimals and Numbers only!")
            return -1
        
        if(float(first_entry.get()) < 0):
            mb.showerror("FIRST HIGHEST INPUT","Your frist salary input was invalid because it \ncannot be below zero!. Positive decimals and Numbers only!")
            return -1
        else:
            pass
        
        
        
        
        
        
        
      #Second salary input validation section  
    if second_entry.get() == "":
        mb.showerror("SECOND HIGHEST INPUT","Your second salary input was invalid because it \nwas blank. Positive decimals and Numbers only!")
        return -1
    else:
        try:
            float(second_entry.get())
        except:
            mb.showerror("SECOND HIGHEST INPUT","Your second salary input was invalid because it \ncontained illegal characters. Positive decimals and Numbers only!")
            return -1
        
        if(float(second_entry.get()) < 0):
            mb.showerror("SECOND HIGHEST INPUT","Your second salary input was invalid because it \ncannot be below zero!. Positive decimals and Numbers only!")
            return -1
        else:
            pass
        
        
        
        
        
        
     #Third salary input validation section
    if third_entry.get() == "":   
        mb.showerror("THIRD HIGHEST INPUT","Your third salary input was invalid because it \nwas blank. Positive decimals and Numbers only!")
        return -1
    else:
        try:
            float(third_entry.get())
        except:
            mb.showerror("THIRD HIGHEST INPUT","Your third salary input was invalid because it \ncontained illegal characters. Positive decimals and Numbers only!")
            return -1
        
        
        if(float(third_entry.get()) < 0):
            mb.showerror("THIRD HIGHEST INPUT","Your third salary input was invalid because it \ncannot be below zero!. Positive decimals and Numbers only!")
            return -1
        else:
            pass
    
    
    
    
    
    
     #Checking to see if all three salary input are not zero validation section
    if(float(first_entry.get()) == 0 and float(second_entry.get()) == 0 and float(third_entry.get()) == 0):
        mb.showerror("NO ALL ZERO SALARIES","Your input was invalid because all salaries \ncannot be 0! Positive decimals and Numbers only!")
        return -1
    else:
        pass
    
    
    
    
     #Years input validation section
    if years_entry.get() == "":
        mb.showerror("","Your years of service input was invalid because it \nwas blank. Positive Integers and Numbers only!")
        return -1
    else:
        try:
            int(years_entry.get())
        except:
            mb.showerror("YEARS INPUT","Your years of service input was invalid because it \ncontained illegal characters. Positive Integers and Numbers only!")
            return -1
        if(int(years_entry.get()) < 0):
            mb.showerror("YEARS ENTRY INPUT","Your years input was invalid because it \ncannot be below zero! Positive Integers only!")
            return -1
        else:
            pass
        
        
    
    
    #Age input validation section
    if age_entry.get() == "":
        mb.showerror("AGE ENTRY EMPTY","Your age input was invalid because \n it was blank. Positive Integers and Numbers only!")
        return -1
    else:
        try:
            int(age_entry.get())
        except:
            mb.showerror("AGE INPUT","Your age input was invalid because it \ncontained illegal characters. Positive Integers and Numbers only!")
            return -1
        
        if(int(age_entry.get()) == 0):
            mb.showerror("AGE ENTRY INPUT","Your age input was invalid because it cannot be zero! Positive Integers and Numbers only!")
            return -1
        else:
            pass
        if(int(age_entry.get()) < 0):
            mb.showerror("AGE ENTRY INPUT","Your age input was invalid because it \ncannot be below zero! Positive Integers and Numbers only!")
            return -1
        else:
            pass
   
    
     #Months input validation section
    if months_entry.get() == "":
        mb.showerror("","Your months of service input was invalid because it \nwas blank. Positive Integers and Numbers only!")
        return -1
    else:
        try:
            int(months_entry.get())
        except:
            mb.showerror("MONTHS INPUT","Your months of service input was invalid because it \ncontained illegal characters. Positive Integers and Numbers only!")
            return -1
        if(int(months_entry.get()) < 0):
            mb.showerror("MONTHS ENTRY INPUT","Your months input was invalid because it \ncannot be below zero! Positive Integers and Numbers only!")
            return -1
        else:
            pass
        
        
        
    #Checking to see if both months and years are not zero validation section
    if (int(months_entry.get()) == 0 and int(years_entry.get()) == 0):
        mb.showerror("YEARLY AND MONTH","Your input was invalid because both years \nand months cannot both be zero!")
        return -1
    else:
        pass
    
    
'''
Function that when called, uses similar calculations to the previous example.
This function uses all the information the user entered and calcculates the pension.
First checks to ensure the user input is correct and formatted correctly. It uses the test_user_input() function
that if the function returns the sentinel -1, then it is flagged as illegal and the function does not do
anything. This function is called by the "Calculate Pension" button.
'''
def calculate_pension():
   
    
    if test_user_input() != -1:
        
        yearly_avg = round((((float(first_entry.get()) + float(second_entry.get()) + float(third_entry.get())) / 3)),2)
        years = (int(years_entry.get()) + (int(months_entry.get()) / 12))
        
        first_five_years = (yearly_avg * 5) * 0.015
        second_five_years = (yearly_avg * 5) * 0.0175
        rest_of_years = ((years - 10) * yearly_avg) * 0.02
        total_over_course = (first_five_years + second_five_years + rest_of_years)
        perRate = total_over_course / yearly_avg
        
        p = min(perRate, 0.8)
    
        
        pension = (p * yearly_avg)
        
        format_pension = "${pension:,.2f}" #Format to have $ , ',' , and 2 decimal places.
        formatted_pension = format_pension.format(pension=pension)
        pension_output.config(text=str(formatted_pension))
    else:
        return
    

'''
Function that when called, clears all field entries in the GUI to blank. Used to clear out inputs.
This method accesses all the entries and starting from the beginning index, clears the entries.
This function is called via the "Clear Entries" button. When the button is pressed this function is called and used.
'''
def clear_entries():
    first_entry.delete(0, 'end')
    second_entry.delete(0, 'end')
    third_entry.delete(0, 'end')
    age_entry.delete(0, 'end')
    years_entry.delete(0, 'end')
    months_entry.delete(0, 'end')
    pension_output.config(text="")
    return



'''
All of the widgets, panels, and grid systems in implemented and marked in their own sections,
i.e: Top frame, salary labels, etc. all have their own labeled sections for easy viewing
and future reference.
'''


#Creation of the window, and setting the title.
window = Tk()

window.title("Pension")




############# TOP FRAME AND BUTTON FRAME CREATION ##########################
top_frame = Frame(window)
top_frame.grid(row=0,column=0)

salaries_frame = Frame(top_frame)
salaries_frame.grid(row=0,column=0)


service_frame = Frame(top_frame)
service_frame.grid(row=0,column=1,padx=20)

button_frame_1 = Frame(window)
button_frame_1.grid(row=1,column=0)

button_frame_2 = Frame(window)
button_frame_2.grid(row=2,column=0)
#####################################################







############# SALARY LABELS ##########################
first_label = Label(salaries_frame,text="First Highest Salary: ")
second_label = Label(salaries_frame,text="Second Highest Salary: ")
third_label = Label(salaries_frame,text="Third Highest Salary: ")
age_label = Label(salaries_frame,text="Age: ")

first_label.grid(row=0,column=0,sticky=E)
second_label.grid(row=1,column=0,sticky=E)
third_label.grid(row=2,column=0,sticky=E)
age_label.grid(row=3,column=0,sticky=E)

#####################################################







############# SALARY ENTRIES ##########################

first_entry = Entry(salaries_frame,width=10)
second_entry = Entry(salaries_frame,width=10)
third_entry = Entry(salaries_frame,width=10)
age_entry = Entry(salaries_frame,width=3)


first_entry.grid(row=0,column=1,pady=1)
second_entry.grid(row=1,column=1,pady=1)
third_entry.grid(row=2,column=1,pady=1)
age_entry.grid(row=3,column=1,sticky=W,pady=1)


#####################################################









############# SERVICE LABELS ##########################
service_label = Label(service_frame,text="Service ")
service_label.grid(row=0,column=0,sticky=N)


years_label = Label(service_frame,text="Years: ")
months_label = Label(service_frame,text="Months: ")
blank = Label(service_frame,text=" ")


years_label.grid(row=1,column=0,sticky=E)
months_label.grid(row=2,column=0,sticky=E)
blank.grid(row=4,column=1)

######################################################









############# SERVICE ENTRIES ##########################

years_entry = Entry(service_frame,width=3)
months_entry = Entry(service_frame,width=3)

years_entry.grid(row=1,column=1,pady=1)
months_entry.grid(row=2,column=1,pady=1)

######################################################









############# FUNCTIONAL BUTTONS ###################################

calculate_button = Button(button_frame_1,text="Calculate Pension",command=calculate_pension)
calculate_button.grid(row=0,column=2,pady=3)
blank_1 = Label(button_frame_1,text="                       ")
blank_1.grid(row=0,column=1)

clear_entries_button = Button(button_frame_2,text="Clear Entries",command=clear_entries)
clear_entries_button.grid(row=1,column=1,pady=3)
blank_entries_control = Label(button_frame_2,text="                       ")
blank_entries_control.grid(row=1,column=0)


close_form_button = Button(button_frame_2,text="Close Form ",command=window.destroy)
close_form_button.grid(row=2,column=1,pady=3)
blank_form_control = Label(button_frame_2,text="                       ")
blank_form_control.grid(row=2,column=0)

##########################################################








############# BOTTOM FRAME PENSION LABEL AND OUTPUT ###################################

bottom_frame = Frame(window)
bottom_frame.grid(row=3,column=0)


pension_control = Label(bottom_frame,text="                   ")
pension_control.grid(row=0,column=0,pady=5)

pension_label = Label(bottom_frame,text="Pension: ")
pension_label.grid(row=0,column=1,sticky=W)

pension_output = Label(bottom_frame,text="",relief=SUNKEN,width=13,anchor=W)
pension_output.grid(row=0,column=2,sticky=W)

##################################################################################




window.mainloop() #Use this to start the GUI run process.