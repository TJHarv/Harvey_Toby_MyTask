
###THarvey_Final Assignment
##IMPLICIT BIAS TEST: Gender & Science



#Importing all required modules and functions
from psychopy import core, event, gui
from psychopy.visual import Window, TextStim, Rect#!!!maybe use cross? but how?
from psychopy.core import wait, Clock
from psychopy.event import waitKeys, getKeys 
import random as rd



#Defining global key combination for quitting
event.globalKeys.add(key="q", modifiers=["ctrl"], func=core.quit)




##Preliminary Code
#Creating a file for the respective participant 
data_out=open("/Users/Toby/Desktop/UNI WIEN/2000xx - Programming with Python/Final Assignment/Results/Data.txt","w", encoding="utf-8")
data_out.write( '\t'.join( [ "subject_id", "age", "gender", "occupation","country of residence"] ) + "\n" ) #!!!Wrong and missing variables!!!GUI variables missing!!!
 
#Assigning all object instances
#Window
my_win=Window([1000,600], color="white")#!!!Create template windows for experimental conditions - But how?
#Categories and their words 
male_words=["Man", "Son", "Father", "Boy", "Uncle", "Grandpa", "Husband", "Male"]
female_words=["Woman", "Daughter", "Mother", "Girl", "Aunt", "Grandma", "Wife", "Female"]
science_words=["Astronomy", "Math", "Chemistry", "Physics", "Biology", "Geology", "Engineering"]
arts_words=["History", "Arts", "Humanities", "English", "Philosophy", "Music", "Literature"]
#Categories grouped into two factors, necessary for functions 
gender_words=["Man", "Son", "Father", "Boy", "Uncle", "Grandpa", "Husband", "Male","Woman", "Daughter", "Mother", "Girl", "Aunt", "Grandma", "Wife", "Female"]
fields_words=["Astronomy", "Math", "Chemistry", "Physics", "Biology", "Geology", "Engineering","History", "Arts", "Humanities", "English", "Philosophy", "Music", "Literature"]
fieldbygender_words=["Man", "Son", "Father", "Boy", "Uncle", "Grandpa", "Husband", "Male","Astronomy", "Math", "Chemistry", "Physics", "Biology", "Geology", "Engineering","Woman", "Daughter", "Mother", "Girl", "Aunt", "Grandma", "Wife", "Female","History", "Arts", "Humanities", "English", "Philosophy", "Music", "Literature"]
#fieldbygender_words_incongruent=["Woman", "Daughter", "Mother", "Girl", "Aunt", "Grandma", "Wife", "Female",]

#Empty grouped factors lists, necessary for functions 
gender_words_list=[]
fields_words_list=[]
fieldbygender_list_congruent=[]
fieldbygender_list_incongruent=[]
#Visuals - displaying categories as orientation for PPs - Work in Progress
male_cat=TextStim(my_win,text="Male",height=0.08,color="green")#!!!pos is missing
female_cat=TextStim(my_win,height=0.08,color="green")
science_cat=TextStim(my_win,height=0.08,color="blue")
arts_cat=TextStim(my_win,height=0.08,color="blue")
#Error Rectangle - displayed when error is made - Work in Progress
error_rect=Rect(my_win, fillColor="red", width=0.2, height=0.2)#Used to display error when commited!!!Turn into cross instead, but how?
#Response time lists containing RTs and key presses
resptimelist_congruent=[]
resptimelist_incongruent=[]

##Defining all functions 
#Instruction Screens
instruction_page=TextStim(my_win, wrapWidth=1.5, height=0.06, color="black")
def instruction(instruction_text, min_wait=0.1):
    instruction_page.setText(instruction_text)
    instruction_page.draw()
    my_win.flip()
    wait(min_wait)
    waitKeys(keyList=["space"])
    
#GUI 
def open_gui():
    myDlg = gui.Dlg(title="Implicit Bias Test")
    myDlg.addText('Subject info')
    myDlg.addField('Subject ID (filled out by reseacher):')
    myDlg.addField('Age:')
    myDlg.addField('Gender:')
    myDlg.addField('Occupation:')
    myDlg.addField('Country of Residence:')
    ok_data = myDlg.show()  # show dialog and wait for OK or Cancel
    if myDlg.OK:  # or if ok_data is not None
        print(ok_data)
        data_out.write( '\t'.join(ok_data)  + "\n" )#!!!Add date and time - + str(strftime("%Y%m%d%H%M%S", gmtime())
    else:
        print('user cancelled')

#Function for PP to sort gender 
text_to_show=TextStim(my_win, text="", height=0.08,color="black")


def gender_sort():#!!!display errors 
        rd.shuffle(gender_words)#Randomises list so that it is different for every PP
        timer=Clock()
        while len(gender_words_list) < 8:
            for word in gender_words:
                if word in male_words:
                    text_to_show.text=word
                    text_to_show.draw()
                    my_win.callOnFlip(timer.reset)
                    my_win.flip()
                    pressed_key=waitKeys(keyList="f", timeStamped=timer)#!!!Not so important here, but reset timer to zero after every key press
                    print(pressed_key)
                    gender_words_list.append(word)
                elif word in female_words:
                    text_to_show.text=word
                    text_to_show.draw()
                    my_win.callOnFlip(timer.reset)
                    my_win.flip()
                    pressed_key=waitKeys(keyList="j", timeStamped=timer)
                    print(pressed_key)
                    gender_words_list.append(word)
                    
#Function for PP to sort fields - see above 
def field_sort():
        rd.shuffle(fields_words)
        timer=Clock()
        while len(fields_words_list) < 8:
            for word in fields_words:
                if word in science_words:
                    text_to_show.text=word
                    text_to_show.draw()
                    my_win.callOnFlip(timer.reset)
                    my_win.flip()
                    pressed_key=waitKeys(keyList="f", timeStamped=timer)
                    print(pressed_key)
                    fields_words_list.append(word)
                elif word in arts_words:
                    text_to_show.text=word
                    text_to_show.draw()
                    my_win.callOnFlip(timer.reset)
                    my_win.flip()
                    pressed_key=waitKeys(keyList="j", timeStamped=timer)
                    print(pressed_key)
                    fields_words_list.append(word)

#Function for PP to sort fields - but keys switched 
def field_sort2():
        rd.shuffle(fields_words)
        timer=Clock()
        while len(fields_words_list) < 8:
            for word in fields_words:
                if word in science_words:
                    text_to_show.text=word
                    text_to_show.draw()
                    my_win.callOnFlip(timer.reset)
                    my_win.flip()
                    pressed_key=waitKeys(keyList="f", timeStamped=timer)
                    print(pressed_key)
                    fields_words_list.append(word)
                elif word in arts_words:
                    text_to_show.text=word
                    text_to_show.draw()
                    my_win.callOnFlip(timer.reset)
                    my_win.flip()
                    pressed_key=waitKeys(keyList="j", timeStamped=timer)
                    print(pressed_key)
                    fields_words_list.append(word)


#Functions for PP to sort field by gender - congruent
def fieldbygender_sort_congruent():
        rd.shuffle(fieldbygender_words)
        timer=Clock()
        while len(fieldbygender_list_congruent) < 16:
            for word in fieldbygender_words:
                if word in science_words or word in male_words:
                    text_to_show.text=word
                    text_to_show.draw()
                    my_win.callOnFlip(timer.reset)#callOnFlip to achieve most accurate response time
                    my_win.flip()
                    pressed_key=waitKeys(keyList="f", timeStamped=timer)
                    print(pressed_key)
                    fieldbygender_list_congruent.append(word)
                    resptimelist_congruent.append(pressed_key[0][1])#Appends only RTs
                elif word in arts_words or word in female_words:
                    text_to_show.text=word
                    text_to_show.draw()
                    my_win.callOnFlip(timer.reset)
                    my_win.flip()
                    pressed_key=waitKeys(keyList="j", timeStamped=timer)
                    print(pressed_key)
                    fieldbygender_list_congruent.append(word)
                    resptimelist_congruent.append(pressed_key[0][1])
                    
                        
            
#Function for PP to sort field by gender - incongruent

def fieldbygender_sort_incongruent():
        rd.shuffle(fieldbygender_words)
        timer=Clock()
        while len(fieldbygender_list_incongruent) < 16:
            for word in fieldbygender_words:
                if word in arts_words or word in male_words:
                    text_to_show.text=word
                    text_to_show.draw()
                    my_win.callOnFlip(timer.reset)
                    my_win.flip()
                    pressed_key=waitKeys(keyList="f", timeStamped=timer)
                    print(pressed_key)
                    fieldbygender_list_congruent.append(word)
                    resptimelist_incongruent.append(pressed_key)
                elif word in science_words or word in female_words:
                    text_to_show.text=word
                    text_to_show.draw()
                    my_win.callOnFlip(timer.reset)
                    my_win.flip()
                    pressed_key=waitKeys(keyList="j", timeStamped=timer)
                    print(pressed_key)
                    fieldbygender_list_congruent.append(word)
                    resptimelist_incongruent.append(pressed_key)#How to only append RTs??




##Executing functions - Introductory Screens
#Welcome Screen 
instruction("Welcome and thank you for taking part in this Implicit Bias Test\n\n\nPlease press 'space' to continue ")#!!!change color and boldness of certain words

#Instructions Screen
instruction("Your task will be to sort words into groups as fast as you can\n\nThis study should take about 5 minutes to complete\n\nAt the end, you will receive your result along with information about what it means")#!!!change color and boldness of certain words

#PsychoPy Prompt GUI - Collecting important biographical data
instruction("First, please answer some demographic questions")#!!!change color and boldness of certain words
open_gui()


##Executing functions - Main Experiment
#Varying the conditions
#The experiment always follows the same basic structure: Science Sort - Gender Sort -> Gender and Fields Sort -> Science Sort switched -> Gender and Fields Sort switched 
#!!!Create balanced design order!!!

#instruction("Put a left finger on the F key for items that belong to the category Science.\nPut a right finger on the J key for items that belong to the category Liberal Arts.\nItems will appear one at a time.\n\n\nIf you make a mistake a red square will apear. Press the other key to continue.\n Go as fast as you can while being accurate.\n\nPress 'space' to start")#!!!change color and boldness of certain words
#field_sort()
"""
instruction("Put a left finger on the F key for items that belong to the category Male.\nPut a right finger on the J key for items that belong to the category Female.\nItems will appear one at a time.\n\n\nIf you make a mistake a red square will apear. Press the other key to continue.\n Go as fast as you can while being accurate.\n\nPress 'space' to start")#!!!change color and boldness of certain words
gender_sort()
"""
"""
fieldbygender_sort_congruent()
instruction("Put a left finger on the F key for items that belong to the category Science.\nPut a right finger on the J key for items that belong to the category Liberal Arts.\nItems will appear one at a time.\n\n\nIf you make a mistake a red square will apear. Press the other key to continue.\n Go as fast as you can while being accurate.\n\nPress 'space' to start")#!!!change color and boldness of certain words
field_sort2()
"""
fieldbygender_sort_congruent()
data_out.write("Congruent Condition RTs: "+ str(resptimelist_congruent) + "\n" )
data_out.write("Congruent Condition Average RT: " + str(sum(resptimelist_congruent) / len(resptimelist_congruent)) + "\n")
#Saving experimental data 
data_out.close()

##End of the Experiment 
#Thank You Screen
instruction("This is the end of the experiment.\n\n\nThank you for your participation!\n\n\nPress 'space' to view your results") 

#Immediate Feedback Screen
    #insert function to analyse PPs data and display result. Does bias exist? Preliminary measure by t-test


#Debriefing and Disclaimer Screen
instruction("Disclaimer: These results are provided for educational purposes only. These results may fluctuate and are influenced by variables related to the test")
instruction("What is this test all about?\n\n\nThis test measures associations between concepts (here, Liberal Arts and Science) and evaluations (here, Female and Male)\n\nPeople are quicker to respond when items are closely related in their mind share the same button")

#Final End Screen

