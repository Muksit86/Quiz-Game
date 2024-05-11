# Final Project - Quiz Game using Python and json

#                                   -----------------------------Importing packages and creating the main window-----------------------------
# Importing the tkinter and custom tkinter
from tkinter import *
import customtkinter
import json


# creating the first window
win = customtkinter.CTk()
win.geometry("680x400")
win.resizable(0, 0)
win.title("Quiz Game")
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


#                                   -----------------------------All the questions-----------------------------
# get the data from the json file
with open('data.json') as f:
	data = json.load(f)

# set the question, options, and answer
Questions = (data['question'])
Options = (data['options'])
Answers = (data[ 'answer'])


#                                   -----------------------------All the important variables-----------------------------
# creating important variables
score = 0
wrong = 0
total_no_question = len(Questions)
question_no = 1
time = 11
selected_option = -1


#                                   -----------------------------All the options, result and time-----------------------------
# displaying the options and questions
def display_questions_options():
    question.configure(text=Questions[question_no-1])
    option1.configure(text=Options[question_no-1][0])
    option2.configure(text=Options[question_no-1][1])
    option3.configure(text=Options[question_no-1][2])
    option4.configure(text=Options[question_no-1][3])


#                                   -----------------------------Next Button-----------------------------
# allows next button to change the question
def next_btn():
    global score, question_no, time, wrong, selected_option

    if var1.get() == 1:
        selected_option = 1
    elif var2.get() == 1:
        selected_option = 2
    elif var3.get() == 1:
        selected_option = 3
    elif var4.get() == 1:
        selected_option = 4
    else:
        selected_option = -1

    if(Answers[question_no-1] == selected_option):
        score += 1
    elif (Answers[question_no-1] != selected_option):
        wrong += 1
    #     # print(f"nxt wrong {wrong}")

    if question_no == 1:
        enable_previous_btn()
    
    if question_no <= total_no_question:
        question_no += 1


    time = 11

    if question_no > total_no_question:
        display_result()
        next_button.configure(state="disabled")
    else:
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        display_questions_options()


#                                   -----------------------------Previous Button-----------------------------
# allows previous button to change the question
def previous_btn():
    global score, question_no, time, wrong, selected_option

    question_no -= 1
    print(f"previous question {question_no}")

    display_questions_options()

    if(Answers[question_no] == selected_option):
        score -= 1
    elif (Answers[question_no] != selected_option):
        wrong -= 1
    
    if question_no == 1:
        prv_button.configure(state="disabled")

    time = 11
    
# enables the previous button
# enable the button at right time
def enable_previous_btn():
    prv_button.configure(state="normal")


#                                   -----------------------------Quit Button-----------------------------
# quit the game
def quit_btn():
    win.destroy()

  
# timer lable for displaying the time
time_left = customtkinter.CTkLabel(win, text="", font=("Helvetica", 20, "bold"), 
                                fg_color=("#2FA473"), padx=20, pady=10,
                                corner_radius=6)
time_left.place(x=574, y=65)


#                                   -----------------------------Time Fucntion-----------------------------
# shows 10 sec time for each questions
def countdown():
    global time

    time -= 1

    time_left.configure(text=time)
    time_left.after(1000, countdown)
    
    if time == 0 and question_no < total_no_question:
        next_btn()
        time = 11
    elif time == 0 and question_no >= total_no_question:
        time = 11

# calling the timer function
countdown()


#                                   -----------------------------Display result fuction-----------------------------
# displaying the result
def display_result():
    global time, question_no

    result_win = customtkinter.CTkToplevel()
    result_win.geometry("257x257")
    result_win.title("Result")
    result_win.attributes("-topmost", True)
    result_win.resizable(0,0)

    info_warning = customtkinter.CTkLabel(result_win, text="Are you sure to display the result?", font=("Helvetica", 15, "bold"), 
                                width=250, height=20, bg_color="#2FA473")
    info_warning.place(x=0, y=0)
    
    yes_button = customtkinter.CTkButton(result_win, text="Yes", width=100, height=40, font=("Helvetica", 20, "bold"),
                                    fg_color=("#2FA473"), state="normal", command=lambda: yes_btn())
    yes_button.place(x=65, y=70)

    no_button = customtkinter.CTkButton(result_win, text="No", width=100, height=40, font=("Helvetica", 20, "bold"),
                                    fg_color=("#2FA473"), state="normal", command=lambda: no_btn())
    no_button.place(x=65, y=150)

    def no_btn():
        global question_no, score, wrong, selected_option

        result_win.destroy()

        if var1.get() == 1:
            var1.set(0)
        elif var2.get() == 1:
            var2.set(0)
        elif var3.get() == 1:
            var3.set(0)
        elif var4.get() == 1:
            var4.set(0)


        next_button.configure(state="normal")
        question_no -= 1

        if(Answers[question_no-1] == selected_option):
            score -= 1
        elif (Answers[question_no-1] != selected_option):
            wrong -= 1

    def yes_btn():
        yes_button.destroy()
        no_button.destroy()

        info = customtkinter.CTkLabel(result_win, text="Score Box", font=("Helvetica", 20, "bold"), 
                                width=257, height=10, bg_color="#2FA473")
        info.place(x=0, y=0)

        result_correct = customtkinter.CTkLabel(result_win, text="Correct: " + str(score), font=("Helvetica", 20, "bold"))
        result_correct.pack(padx=12, pady=32)

        result_wrong = customtkinter.CTkLabel(result_win, text="Wrong: " + str(wrong), font=("Helvetica", 20, "bold"))
        result_wrong.pack(padx=12)

        if score <= len(Answers)/2:
            info_for_win = customtkinter.CTkLabel(result_win, text="Better luck\n Next Time", font=("Helvetica", 20, "bold"))
            info_for_win.place(x=70, y=150)
        else:
            info_for_loose = customtkinter.CTkLabel(result_win, text="Good Job", font=("Helvetica", 20, "bold"))
            info_for_loose.place(x=70, y=150)

        time = 0
        time_left.place_forget()


#                                   -----------------------------Option Fucntion-----------------------------
# single cheak button will be press each at a time
def CheakOption(option):
    if(option == 1):
        var2.set(0)
        var3.set(0)
        var4.set(0)
    elif(option == 2):
        var3.set(0)
        var4.set(0)
        var1.set(0)
    elif(option == 3):
        var1.set(0)
        var2.set(0)
        var4.set(0)
    elif(option == 4):
        var1.set(0)
        var2.set(0)
        var3.set(0)


# question lable for displaying the question
question = customtkinter.CTkLabel(win, corner_radius=5, width=120, height=40, font=("Helvetica", 20, "bold"),
                                fg_color=("#2FA473"),
                                text=Questions[0])
question.place(x=60, y=65)


# variabl for options
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()


# options cheakbox for displaying the options (total 4 options)
option1 = customtkinter.CTkCheckBox(win, text=Options[0][0], font=("Helvetica", 20, "bold"), variable=var1,
                                    command=lambda:  CheakOption(1))
option1.place(x=65, y=150)

option2 = customtkinter.CTkCheckBox(win, text=Options[0][1], font=("Helvetica", 20, "bold"), variable=var2, 
                                    command=lambda:  CheakOption(2))
option2.place(x=325, y=150)

option3 = customtkinter.CTkCheckBox(win, text=Options[0][2], font=("Helvetica", 20, "bold"), variable=var3, 
                                    command=lambda:  CheakOption(3))
option3.place(x=65, y=250)

option4 = customtkinter.CTkCheckBox(win, text=Options[0][3], font=("Helvetica", 20, "bold"), variable=var4, 
                                    command=lambda:  CheakOption(4))
option4.place(x=325, y=250)


#                                   -----------------------------All the buttons-----------------------------
# next button
next_button = customtkinter.CTkButton(win, text="Next", width=100, height=40, font=("Helvetica", 20, "bold"),
                                    fg_color=("#2FA473"), state="normal",
                                    command=lambda: next_btn())
next_button.place(x=255, y=335)

# previous button
prv_button = customtkinter.CTkButton(win, text="Previous", width=120, height=40, font=("Helvetica", 20, "bold"),
                                    fg_color=("#2FA473"), state="disabled",
                                    command=lambda: previous_btn())
prv_button.place(x=50, y=335)

# quit button
quit_button = customtkinter.CTkButton(win, text="Quit", width=100, height=40, font=("Helvetica", 20, "bold"), 
                                    fg_color=("#2FA473"),
                                    command=lambda: quit_btn())
quit_button.place(x=450, y=335)

# score label for displaying the score
Score = customtkinter.CTkLabel(win, text="", font=("Helvetica", 20, "bold"))
Score.place_forget()

# wrong lables for wrong answers
Wrong = customtkinter.CTkLabel(win, text="", font=("Helvetica", 20, "bold"))
Wrong.place_forget()

#                                   -----------------------------Title-----------------------------
# title for the main window
title = customtkinter.CTkLabel(win, text="Quiz Game", font=("Helvetica", 20, "bold"), 
                                width=680, height=10, bg_color="#2FA473", anchor=CENTER)
title.place(x=0,y=0)


#-----------------------------It makes the main window keep running-----------------------------
#loop
win.mainloop()