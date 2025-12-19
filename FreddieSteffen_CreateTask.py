#FreddieSteffen_CreateTask.py

#Imports
import tkinter as tk
from PIL import Image, ImageTk
import turtle as trtl
import random as rand

#Lists
SuitsList = ["Hearts", "Diamonds", "Spades", "Clubs"]
NumbersList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

#Variables
CardName = rand.choice(NumbersList)
CardSuit = rand.choice(SuitsList)

#Functions
def StartScreenClear():
  WelcomeLabel.grid_remove()
  QuestionLabel.grid_remove()
  StartButton.grid_remove()
  RulesButton.grid_remove()

def BackClear():
  RulesTitle.grid_remove()
  RulesLabel.grid_remove()
  BackButton.grid_remove()

def CardsValues():
  global CardValue, CardName
  if CardName == "Ace":
    CardValue = 11
    Card = ("Ace of " + CardSuit)
  if CardName == "King":
    CardValue = 10
    Card = ("King of " + CardSuit)
  if CardName == "Queen":
    CardValue = 10
    Card = ("Queen of " + CardSuit)
  if CardName == "Jack":
    CardValue = 10
    Card = ("Jack of " + CardSuit)
  if CardName != "Ace" and CardName != "King" and CardName != "Queen" and CardName != "Jack":
    CardValue = int(CardName)
    Card = (CardName + " of " + CardSuit)
  print(Card)

def OnClick(command):
  global WelcomeLabel, QuestionLabel, StartButton, RulesButton, BlackjackLabel, RulesTitle, RulesLabel, BackButton
  if command == "Start":
    StartScreenClear()
    BlackjackLabel = tk.Label(root, text="Blackjack", bg="#8C1515", fg="white", font=("times", 24, "bold"), padx=10)
    BlackjackLabel.grid(row=0, column=0, padx=10, pady=10)
    HitButton = tk.Button(button_frame, text="Hit", command=lambda:OnClick("Hit"))
    HitButton.grid(row=1, column=0, padx=5)
    StandButton = tk.Button(button_frame, text="Stand", command=lambda:OnClick("Stand"))
    StandButton.grid(row=1, column=1, padx=5)
    NewGameButton = tk.Button(button_frame, text="New Game", command=lambda:OnClick("New Game"))
    NewGameButton.grid(row=1, column=2, padx=5)

  if command == "Rules":
    StartScreenClear()
    RulesTitle = tk.Label(root, text="Rules", bg="#8C1515", fg="white", font=("times", 24, "bold"), padx=10)
    RulesTitle.grid(row=0, column=0, padx=10, pady=10)
    RulesLabel = tk.Label(root, text="The rules are that all players get cards face up, with the dealer's first card being face up and the second being face down.\n The goal is to get closer to 21 points than the dealer does without going over 21.\n If your hand goes over 21, it is called a “bust” and you lose the betted amount.\n You can “hit” to get another card, or “stand” to not get anymore cards and then the dealer will “hit” until they are over the score of 17.", bg="#8C1515", fg="white", font=("times", 12), padx=10)
    RulesLabel.grid(row=1, column=0, padx=10, pady=10)
    BackButton = tk.Button(button_frame, text="Back", command=lambda:OnClick("Back"))
    BackButton.grid(row=2, column=0, padx=5)

  if command == "Back":
    BackClear()
    WelcomeLabel.grid(row=0, column=0, padx=10, pady=10)
    QuestionLabel.grid(row=1, column=0, padx=10, pady=10)
    StartButton.grid(row=2, column=1, padx=5)
    RulesButton.grid(row=2, column=2, padx=5)

  if command == "Hit":
    print("Hit")
  if command == "Stand":
    print("Stand")
  if command == "New Game":
    print("New Game")

#General Game
root = tk.Tk()
root.configure(bg="#8C1515")
root.title("Fredddie Steffen Create Task")
root.columnconfigure(0, weight=1)
root.rowconfigure(3, weight=1)
button_frame = tk.Frame(root, bg="#8C1515")
button_frame.grid(row=3, column=0, pady=10)

WelcomeLabel = tk.Label(root, text="Welcome to Blackjack", bg="#8C1515", fg="white", font=("times", 24, "bold"), padx=10)
WelcomeLabel.grid(row=0, column=0, padx=10, pady=10)
QuestionLabel = tk.Label(root, text="If you would like to know the rules or just get right into it, click the respective buttons", compound="center", bg="#8C1515", fg="white", font=("times", 12), padx=10)
QuestionLabel.grid(row=1, column=0, padx=10, pady=10)

StartButton = tk.Button(button_frame, text="Start", command=lambda:OnClick("Start"))
StartButton.grid(row=2, column=1, padx=5)
RulesButton = tk.Button(button_frame, text="Rules", command=lambda:OnClick("Rules"))
RulesButton.grid(row=2, column=2, padx=5)

CardsValues()

#Keeping game there
root.mainloop()