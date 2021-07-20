###THarvey_Final Assignment_Implicit Bias Test

# -*- coding: utf-8 -*-

##Importing all required modules 
from psychopy import visual, core, event, gui
from psychopy.visual import Window, TextStim, Rect
from psychopy.core import wait, Clock
from psychopy.event import waitKeys, getKeys
import random as rd

##Defining global key combination for quitting
event.globalKeys.add(key="q", modifiers=["ctrl"], func=core.quit)

#Creating two files for the respective participant - one with raw data, the other with processed data 
raw_data_out=open("Raw_Experimental_Data.txt","a", encoding="utf-8")
print("raw data file was created")
raw_data_out.write("\t".join(["subject_id", "condition","age", "gender", "occupation","country of residence","congruent task"])\
    + "\t" + "\t".join([str(i) for i in range(1,33)]) + "\t" + "incongruent task" +  "\t" +"\t".join([str(i) for i in range(1,33)]) + "\n")
data_out=open("Experimental_Data.txt","a", encoding="utf-8")
print("processed data file was created")
data_out.write( '\t'.join(["subject_id", "condition","age", "gender", "occupation","country of residence","congruent average rt","incongruent average rt", "difference score rt"]) + "\t" + "\n" ) 


##Assigning object instances
#Window
my_win=Window([1000,600], color="black")

##Assigning global variables
#Categories and their words 
concept1=["Astronomy", "Math", "Chemistry", "Physics", "Biology", "Geology", "Engineering","Technology"]
concept2=["History", "Arts", "Humanities", "English", "Philosophy", "Music", "Literature","Sociology"]
evaluation1=["Man", "Son", "Father", "Boy", "Uncle", "Grandpa", "Husband", "Male"]
evaluation2=["Woman", "Daughter", "Mother", "Girl", "Aunt", "Grandma", "Wife", "Female"]
#Categories grouped into two factors, necessary for functions 
evaluation=["Man", "Son", "Father", "Boy", "Uncle", "Grandpa", "Husband", "Male",\
    "Woman", "Daughter", "Mother", "Girl", "Aunt", "Grandma", "Wife", "Female"]
concept=["Astronomy", "Math", "Chemistry", "Physics", "Biology", "Geology", "Engineering","Technology",\
    "History", "Arts", "Humanities", "English", "Philosophy", "Music", "Literature","Sociology"]
concept_by_evaluation=["Man", "Son", "Father", "Boy", "Uncle", "Grandpa", "Husband", "Male",\
    "Astronomy", "Math", "Chemistry", "Physics", "Biology", "Geology", "Engineering","Technology",\
    "Woman", "Daughter", "Mother", "Girl", "Aunt", "Grandma", "Wife", "Female",\
    "History", "Arts", "Humanities", "English", "Philosophy", "Music", "Literature","Sociology"]
#Response time lists containing RTs and key presses
resp_time_list_congruent=[]
resp_time_list_incongruent=[]


##Defining all functions 
#Instruction Screens
def instruction(instruction_text, min_wait=0.1,Continue=True):
    instruction_page=TextStim(my_win, wrapWidth=2, height=0.07, color="white")
    instruction_page.setText(instruction_text)
    instruction_page.draw()
    if Continue==True:
        continue_key=TextStim(my_win,text="Presse the 'space bar' to continue",height=0.05,pos=(0,-0.8))
        continue_key.draw()
    my_win.flip()
    wait(min_wait)
    waitKeys(keyList=["space"])
#Sorting Instruction Function
def sorting_instruction(task,left_category, right_category,left_category_2="foo",right_category_2="bar"):
    if task==concept or task==evaluation:
        instruction("Put a left finger on the 'F' key for items that belong to the category " + left_category + ".\nPut a right finger on the 'J' key for items that belong to the category " + right_category \
            + ".\n\n\nItems will appear one at a time.\n\nIf you make a mistake a red cross will flash.\n\n Go as fast as you can while being accurate.")
    elif task==concept_by_evaluation:
        instruction("Put a left finger on the 'F' key for items that belong to the category " + left_category + " or " + left_category_2 + ".\nPut a right finger on the 'J' key for items that belong to the category " + right_category + " or " + right_category_2 +".\
        \n\n\nItems will appear one at a time.\n\nIf you make a mistake a red cross will flash.\n\n Go as fast as you can while being accurate.")
#Creating the GUI window
def create_gui():
    myDlg = gui.Dlg(title="Implicit Bias Test")
    myDlg.addText('Subject Info')
    myDlg.addField('Subject ID (filled out by reseacher):')
    myDlg.addField('Condition (filled out by researcher)',choices=["1","2"])
    myDlg.addField('Age:')
    myDlg.addField('Gender:')
    myDlg.addField('Occupation:')
    myDlg.addField('Country of Residence:')
    print("GUI was created")
    open_gui(myDlg)
#Opening the GUI window, including compulsory fields 
def open_gui(myDlg):
     global cancel
     ok_data = myDlg.show()
     if myDlg.OK:
         if ok_data[1] == '' or ok_data[2] == '': # check if fulfilled
              open_gui(myDlg)    # start (show) Dlg again if not
         if ok_data != None:
             cancel=False
             global condition
         condition=ok_data[1]
         raw_data_out.write( '\t'.join(ok_data) + "\t")
         data_out.write( '\t'.join(ok_data) + "\t")
         print("user filled out gui with following data: ", ok_data)
         print("gui data was saved to both data files")
     else:
         cancel=True
         print('user cancelled')
#Templates for Experimental Screen
def exp_screen(task, switched):
    upper_left=TextStim(my_win, text="", height=0.07, color="green", pos=(-0.8, 0.85))
    upper_right=TextStim(my_win, text="", height=0.07, color="green", pos=(0.8,0.85))
    bottom_left=TextStim(my_win, text="", height=0.07, color="green",pos=(-0.8,0.65))
    bottom_right=TextStim(my_win, text="", height=0.07, color="green",pos=(0.8,0.65))
    key_left=TextStim(my_win, text="'F'", height=0.07, color="blue", pos=(-0.8, 0.75))
    key_right=TextStim(my_win, text="'J'", height=0.07, color="blue", pos=(0.8, 0.75))
    upper_left.text=""
    upper_right.text=""
    bottom_left.text=""
    bottom_right.text= ""
    if task==concept:
        if switched==False:
            upper_left.text="Science"
            upper_right.text="Liberal Arts"
        else:
            upper_left.text="Liberal Arts"
            upper_right.text="Science"
    elif task==evaluation:
        if switched==False:
            upper_left.text="Male"
            upper_right.text="Female"
        else:
            upper_left.text="Female"
            upper_right.text="Male"
    elif task==concept_by_evaluation:
        if switched==False:
            upper_left.text="Male"
            upper_right.text="Female"
            bottom_left.text="Science"
            bottom_right.text="Liberal Arts"
        else:
            upper_left.text="Male"
            upper_right.text="Female"
            bottom_left.text="Liberal Arts"
            bottom_right.text="Science"
    upper_left.draw()
    bottom_left.draw()
    upper_right.draw()
    bottom_right.draw()
    key_left.draw()
    key_right.draw()
#Presentation of Stimuli
def show_stimuli(task,word,correct_key,wrong_key,switched):
    timer=Clock()
    while timer.getTime() < 10:
        text_to_show=TextStim(my_win, text="", height=0.07,color="white")
        text_to_show.text=word
        text_to_show.draw()
        exp_screen(task, switched)
        my_win.flip()
        correct=getKeys(keyList=correct_key)
        wrong=getKeys(keyList=wrong_key)
        if correct:
            reaction_time=timer.getTime()
            if task==concept_by_evaluation:
                if switched==False:
                    reaction_time_data=resp_time_list_congruent
                    reaction_time_data.append(reaction_time)
                else:
                    reaction_time_data=resp_time_list_incongruent
                    reaction_time_data.append(reaction_time)
            break
        elif wrong:
            error_cross=TextStim(my_win, text="X", height=0.2,color="red",pos=(0,-0.2))
            error_cross.draw()
#Sorting Function
def sorting(task,switched,list1,list2,list3="foo",list4="bar"):
    rd.shuffle(task)
    if task==concept or task==evaluation:
        for word in task[0:5]:
            if word in list1:
                show_stimuli(task,word,"f","j",switched)
            elif word in list2:
                show_stimuli(task,word,"j","f",switched)
    elif task==concept_by_evaluation:
        for word in task[0:5]:
            if word in list1 or word in list2:
                show_stimuli(task,word,"f","j",switched)
            elif word in list3 or word in list4:
                show_stimuli(task,word,"j","f",switched)
#Experimental Function, includes aforementioned functions 
def exp_function(task,switched=False):
    if task==concept:
        if switched==False:
           left_category="Science"
           right_category="Liberal Arts"
           list1=concept1
           list2=concept2
           sorting_instruction(task,left_category, right_category,left_category_2="foo",right_category_2="bar")
           sorting(task,switched,list1,list2)
        else:
           left_category="Liberal Arts"
           right_category="Science"
           list1=concept2
           list2=concept1 
           sorting_instruction(task,left_category, right_category,left_category_2="foo",right_category_2="bar")
           sorting(task,switched,list1,list2)
        print("concept sorting was presented to PP")
    elif task==evaluation:
        left_category="Male"
        right_category="Female"
        list1=evaluation1 
        list2=evaluation2
        sorting_instruction(task,left_category, right_category,left_category_2="foo",right_category_2="bar")
        sorting(task,switched,list1,list2)
        print("evaluation sorting was presented to PP")
    elif task==concept_by_evaluation:
        if switched==False:
            left_category="Male"
            right_category="Female"
            left_category_2="Science"
            right_category_2="Liberal Arts"
            list1=evaluation1 
            list2=concept1
            list3=evaluation2
            list4=concept2
            sorting_instruction(task,left_category, right_category,left_category_2,right_category_2)
            sorting(task,switched,list1,list2,list3,list4)
        else:
            left_category="Male"
            right_category="Female"
            left_category_2="Liberal Arts"
            right_category_2="Science"
            list1=evaluation1
            list2=concept2
            list3=evaluation2
            list4=concept1
            sorting_instruction(task,left_category, right_category,left_category_2,right_category_2)
            sorting(task,switched,list1,list2,list3,list4)
        print("concept by evaluation sorting was presented to PP")
#Data Write and Save Function 
def write_and_save():
    raw_data_out.write("\t" + "\t".join([str(i) for i in resp_time_list_congruent]) + "\t")
    raw_data_out.write("\t" + "\t".join([str(i) for i in resp_time_list_incongruent]) + "\t\n")
    raw_data_out.close()
    print("raw data was written to file and saved")
    congruent_average=sum(resp_time_list_congruent) / len(resp_time_list_congruent)
    data_out.write(str(congruent_average) + "\t") 
    incongruent_average=sum(resp_time_list_incongruent) / len(resp_time_list_incongruent)
    data_out.write(str(incongruent_average) + "\t")
    difference_score=incongruent_average-congruent_average
    data_out.write(str(difference_score) + "\t" + "\n")
    data_out.close()
    print("processed data was written to file and saved")
#Main Experimental Function, includes every other function and is used to conduct experiment
def main_function():
    create_gui()
    if cancel==True:
        raw_data_out.write("user cancelled\n")
        data_out.write("user cancelled\n")
        data_out.close()
    else:
        instruction("Welcome and thank you for taking part in this Implicit Bias Test!")
        instruction("Your task will be to sort words into groups as fast as you can.\n\nThis study should take about 10 minutes to complete.")
        instruction("You will use the 'F' and 'J' computer keys to categorize items into groups as fast as you can.\n\n\nThese are the four groups and the items that belong to each:\n\n\
            Male: Man, Son, Father, Boy, Uncle, Grandpa, Husband, Male\n\
            Female: Woman, Daughter, Mother, Girl, Aunt, Grandma, Wife, Female\n\
            Science: Astronomy, Math, Chemistry, Physics, Biology, Geology, Engineering,Technology\n\
            Liberal Arts: History, Arts, Humanities, English, Philosophy, Music, Literature, Sociology\n\n\n\
            There are several parts. The instructions change for each part. Pay attention!")
        if int(condition) %2 != 0:
            exp_function(concept)
            exp_function(evaluation)
            exp_function(concept_by_evaluation)
            exp_function(concept,switched=True)
            exp_function(concept_by_evaluation,switched=True)
        else:
            exp_function(concept,switched=True)
            exp_function(evaluation)
            exp_function(concept_by_evaluation,switched=True)
            exp_function(concept)
            exp_function(concept_by_evaluation)
        write_and_save()
        instruction("This is the end of the experiment.\n\n\nThank you for your participation!") 
        instruction("What is this test all about?\n\nThis test measures associations between concepts (here, Liberal Arts and Science) and evaluations (here, Female and Male).\n\nPeople are quicker to respond when items that are closely related in their mind share the same button.")
    instruction("You can now close this window", Continue=False)
    print("experiment was finished")


##Executing the functions/experiment
main_function()






