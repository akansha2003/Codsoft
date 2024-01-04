from tkinter import *
from PIL import Image, ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Scissor Paper game")
root.configure(background="magenta")


#picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor.png"))

#insert picture
user_label = Label(root, image=scissor_img,bg="magenta")
comp_label = Label(root, image=scissor_img_comp,bg="magenta")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#scores
playerScore = Label(root,text=0,font=100,bg="magenta",fg="white")
computerScore = Label(root,text=0,font=100,bg="magenta",fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)
#indicator
user_indicator = Label(root,font=50,text='USER',bg="magenta",fg="white")
comp_indicator = Label(root,font=50,text='COMPUTER',bg="magenta",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#popup
msg = Label(root, font=50,bg="magenta",fg="white")
msg.grid(row=3,column=2)

#update msg
def updateMessage(x):
    msg['text'] = x 
#update player and comp score
def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)

def updateCompScore():
    score = int(computerScore['text'])
    score += 1
    computerScore['text'] = str(score)

#declare winner
def chechWin(player,computer):
    if player == computer:
        updateMessage('Its a tie')
    elif player == 'rock':
        if computer == 'paper':
            updateMessage('You loose')
            updateCompScore()
        else:
            updateMessage('You win')
            updateUserScore()
    elif player == 'paper':
        if computer == 'scissor':
            updateMessage('You loose')
            updateCompScore()
        else:
            updateMessage('You win')
            updateUserScore()
    elif player == 'scissor':
        if computer == 'rock':
            updateMessage('You loose')
            updateCompScore()
        else:
            updateMessage('You win')
            updateUserScore()

    else:
        pass

#function to update choices
choices = ['rock','paper','scissor']
def updateChoice(x):
#computer
    compChoice = choices[randint(0,2)]
    if compChoice == 'rock':
        comp_label.configure(image=rock_img_comp)
    elif compChoice == 'paper':
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

#user
    if x=='rock':
        user_label.configure(image=rock_img)
    elif x=='paper':
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    chechWin(x,compChoice)

    
'''buttons'''
rock = Button(root,width=20,height=2,text='ROCK',bg='orange',fg='white',
              command = lambda:updateChoice('rock')).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text='PAPER',bg='blue',fg='white',
               command = lambda:updateChoice('paper')).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text='SCISSOR',bg='green',fg='white',
                 command = lambda:updateChoice('scissor')).grid(row=2,column=3)


root.mainloop()