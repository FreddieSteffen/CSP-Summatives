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
DealerScore = 0
PlayerScore = 0
PlayerBet = 0
PlayerAces = 0
DealerAces = 0
Chips = 100

#Functions
#TKinter Elements
def Make_TKinter_Elements():
  global root, button_frame, WelcomeLabel, QuestionLabel, StartButton, RulesButton, StartingTextName, NameEntry, PlayerName, RulesTitle, RulesLabel, BackButton, DealerLabel, PlayerLabel, HitButton, StandButton, NewGameButton, BlackjackLabel, StartingTextBet, BetEntry, PlayerBet, BetLabel, ChipsLabel, OutcomeLabel, BustLabel, CashoutButton, TotalLabel, ResetButton
  root = tk.Tk()
  root.configure(bg="#8C1515")
  root.title("Fredddie Steffen Create Task")
  root.columnconfigure(0, weight=1)
  root.rowconfigure(3, weight=1)
  button_frame = tk.Frame(root, bg="#8C1515")
  button_frame.grid(row=3, column=0, pady=10)

  WelcomeLabel = tk.Label(root, text="Welcome to Blackjack", bg="#8C1515", fg="white", font=("times", 24, "bold"), padx=10)
  WelcomeLabel.grid(row=0, column=0, padx=5, pady=10)
  StartingTextName = "Enter Your Name Here:"
  NameEntry = tk.Entry(root, bg="#FFFFFF", fg="#8C1515", font=("Source Sans 3", 14))
  NameEntry.insert(0, StartingTextName)
  NameEntry.bind("<Button-1>", clear_on_click)
  NameEntry.grid(row=1, column=0, padx=5, pady=10)

  QuestionLabel = tk.Label(root, text="If you would like to know the rules or just get right into it, click the respective buttons", compound="center", bg="#8C1515", fg="white", font=("times", 12), padx=10)
  QuestionLabel.grid(row=2, column=0, padx=5, pady=10)
  StartButton = tk.Button(button_frame, text="Start", command=lambda:OnClick("Start"))
  StartButton.grid(row=3, column=1, padx=5)
  RulesButton = tk.Button(button_frame, text="Rules", command=lambda:OnClick("Rules"))
  RulesButton.grid(row=3, column=2, padx=5)

  RulesTitle = tk.Label(root, text="Rules", bg="#8C1515", fg="white", font=("times", 24, "bold"), padx=10)
  RulesTitle.grid(row=0, column=0, padx=10, pady=10)
  RulesLabel = tk.Label(root, text="The rules are that all players get cards face up, with the dealer's first card being face up and the second being face down.\n The goal is to get closer to 21 points than the dealer does without going over 21.\n If your hand goes over 21, it is called a “bust” and you lose the betted amount.\n You can “hit” to get another card, or “stand” to not get anymore cards and then the dealer will “hit” until they are over the score of 17.", bg="#8C1515", fg="white", font=("times", 12), padx=10)
  RulesLabel.grid(row=1, column=0, padx=10, pady=10)
  BackButton = tk.Button(button_frame, text="Back", command=lambda:OnClick("Back"))
  BackButton.grid(row=2, column=0, padx=5)

  DealerLabel = tk.Label(root, text="Dealer Score: " + str(DealerScore), bg="#8C1515", fg="white", font=("times", 12), padx=10)
  DealerLabel.grid(row=1, column=0, padx=5, pady=10)
  PlayerName = NameEntry.get()
  PlayerLabel = tk.Label(root, text=PlayerName +" Score: " + str(PlayerScore), bg="#8C1515", fg="white", font=("times", 12), padx=10)
  PlayerLabel.grid(row=1, column=1, padx=5, pady=10)
  HitButton = tk.Button(button_frame, text="Hit", command=lambda:OnClick("Hit"))
  HitButton.grid(row=2, column=0, padx=5)
  StandButton = tk.Button(button_frame, text="Stand", command=lambda:OnClick("Stand"))
  StandButton.grid(row=2, column=1, padx=5)
  NewGameButton = tk.Button(button_frame, text="New Round", command=lambda:OnClick("Start"))
  NewGameButton.grid(row=2, column=2, padx=5)

  BlackjackLabel = tk.Label(root, text="Blackjack", bg="#8C1515", fg="white", font=("times", 24, "bold"), padx=10)
  BlackjackLabel.grid(row=0, column=0, padx=5, pady=10)
  StartingTextBet = "Enter Bet Here:"
  BetEntry = tk.Entry(root, bg="#FFFFFF", fg="#8C1515", font=("Source Sans 3", 14))
  BetEntry.insert(0, StartingTextBet)
  BetEntry.bind("<Button-1>", clear_on_click)
  BetEntry.bind("<Return>", on_enter)
  BetEntry.grid(row=1, column=0, padx=10, pady=10)
  BetLabel = tk.Label(text="Bet: " + str(PlayerBet))
  BetLabel.grid(row=0, column=1, padx=5, pady=10)
  ChipsLabel = tk.Label(text="Chips: " + str(Chips))
  ChipsLabel.grid(row=0, column=2, padx=5, pady=10)

  OutcomeLabel = tk.Label(root, text="", bg="#8C1515", fg="white", font=("times", 12), padx=10)
  OutcomeLabel.grid(row=1, column=0, padx=10, pady=10)
  BustLabel = tk.Label(root, text="Dealer has Lost (Bust)", bg="#8C1515", fg="white", font=("times", 12), padx=10)
  BustLabel.grid(row=1, column=1, padx=10, pady=10)

  CashoutButton = tk.Button(button_frame, text="Cash Out", command=lambda:OnClick("CashOut"))
  CashoutButton.grid(row=2, column=3, padx=5)
  TotalLabel = tk.Label(text=PlayerName + " total Chips: " + str(Chips))
  TotalLabel.grid(row=1, column=0, padx=5, pady=10)
  ResetButton = tk.Button(text="Reset Game", command=lambda:OnClick("Reset"))
  ResetButton.grid(row=2, column=0, padx=5)

def ClearScreen():
  WelcomeLabel.grid_remove()
  NameEntry.grid_remove()
  QuestionLabel.grid_remove()
  StartButton.grid_remove()
  RulesButton.grid_remove()
  RulesTitle.grid_remove()
  RulesLabel.grid_remove()
  BackButton.grid_remove()
  DealerLabel.grid_remove()
  PlayerLabel.grid_remove()
  HitButton.grid_remove()
  StandButton.grid_remove()
  NewGameButton.grid_remove()
  BlackjackLabel.grid_remove()
  BetEntry.grid_remove()
  BetLabel.grid_remove()
  ChipsLabel.grid_remove()
  OutcomeLabel.grid_remove()
  BustLabel.grid_remove()
  CashoutButton.grid_remove()
  TotalLabel.grid_remove()
  ResetButton.grid_remove()

def StartGame():
  global DealerScore, PlayerScore, PlayerBet, Chips
  ClearScreen()
  WelcomeLabel.grid(row=0, column=0, padx=10, pady=10)
  NameEntry.grid(row=1, column=0, padx=5, pady=10)
  QuestionLabel.grid(row=2, column=0, padx=10, pady=10)
  StartButton.grid(row=3, column=1, padx=5)
  RulesButton.grid(row=3, column=2, padx=5)
  DealerScore = 0
  PlayerScore = 0
  PlayerBet = 0
  Chips = 100

def CardsValues(target):
  global PlayerAces, DealerAces
  card = rand.choice(NumbersList)
  suit = rand.choice(SuitsList)
  if card == "Ace":
    value = 11
    if target == "player": 
      PlayerAces += 1
    else: 
      DealerAces += 1
  elif card in ["King", "Queen", "Jack"]:
    value = 10
  else:
    value = int(card)
  print(f"{card} of {suit}")
  return value

def clear_on_click(event):
  if event.widget == BetEntry and BetEntry.get() == StartingTextBet:
    BetEntry.delete(0, tk.END)
  if event.widget == NameEntry and NameEntry.get() == StartingTextName:
    NameEntry.delete(0, tk.END)

def on_enter(event):
  global PlayerBet, Chips, PlayerScore, DealerScore, PlayerName
  if Chips <= 0:
    StartGame()
    return

  bet_text = BetEntry.get()
  if not bet_text.isdigit():
    BetEntry.delete(0, tk.END)
    BetEntry.insert(0, "Enter a number")
    return

  PlayerBet = int(bet_text)
  if PlayerBet <= 0 or PlayerBet > Chips:
    BetEntry.delete(0, tk.END)
    BetEntry.insert(0, f"Max bet: {Chips}")
    return

  BetEntry.grid_remove()
  BetLabel.config(text="Bet: " + str(PlayerBet))
  ChipsLabel.config(text="Chips: " + str(Chips))
  PlayerName = NameEntry.get()
  PlayerLabel.config(text=PlayerName + "'s Score: " + str(PlayerScore))
  DealerLabel.config(text="Dealer Score: " + str(DealerScore))
  BetLabel.grid(row=0, column=1, padx=5, pady=10)
  ChipsLabel.grid(row=0, column=2, padx=5, pady=10)
  PlayerLabel.grid(row=1, column=1, padx=5, pady=10)
  DealerLabel.grid(row=1, column=0, padx=5, pady=10)
  HitButton.grid(row=2, column=0, padx=5)
  StandButton.grid(row=2, column=1, padx=5)

def GameLogic():
  global DealerScore, PlayerScore, Chips, PlayerBet
  BlackjackLabel.grid(row=0, column=0, padx=5, pady=10)
  NewGameButton.grid(row=2, column=0, padx=5)
  if PlayerScore > 21:
    Chips = Chips - PlayerBet
    OutcomeLabel.config(text="You busted! Dealer wins.")
  elif DealerScore > 21:
    Chips = Chips + PlayerBet
    OutcomeLabel.config(text="Dealer busted! You win.")
  elif PlayerScore > DealerScore:
    Chips = Chips + PlayerBet
    OutcomeLabel.config(text="You win! " + str(PlayerScore) + "-" + str(DealerScore))
  elif DealerScore > PlayerScore:
    Chips = Chips - PlayerBet
    OutcomeLabel.config(text="Dealer wins. Dealer: " + str(DealerScore) + "-" + str(PlayerScore))
  else:
    OutcomeLabel.config(text="Push (tie).")
  OutcomeLabel.grid(row=1, column=0, padx=10, pady=10)
  ChipsLabel.config(text="Chips: " + str(Chips))
  ChipsLabel.grid(row=0, column=1, padx=5, pady=10)
  CashoutButton.grid(row=2, column=3, padx=5)
  PlayerLabel.config(text=PlayerName + "'s Score: " + str(PlayerScore))
  DealerLabel.config(text="Dealer Score: " + str(DealerScore))
  ChipsLabel.config(text="Chips: " + str(Chips))
  BetLabel.config(text="Bet: " + str(PlayerBet))

def OnClick(command):
  global PlayerScore, DealerScore, Chips, PlayerName, PlayerAces, DealerAces, PlayerBet
  if command == "Start":
    ClearScreen()
    PlayerScore = 0
    DealerScore = 0
    PlayerBet = 0
    PlayerAces = 0
    DealerAces = 0
    for i in range(2):
      card_val = CardsValues("player")
      PlayerScore += card_val

    dealer_card_val = CardsValues("dealer")
    DealerScore += dealer_card_val
    print("Dealer Score: " + str(DealerScore))
    BlackjackLabel.grid(row=0, column=0, padx=5, pady=10)
    BetEntry.grid(row=1, column=0, padx=10, pady=10)

  if command == "Rules":
    ClearScreen()
    RulesTitle.grid(row=0, column=0, padx=10, pady=10)
    RulesLabel.grid(row=1, column=0, padx=10, pady=10)
    BackButton.grid(row=2, column=0, padx=5)

  if command == "Back":
    ClearScreen()
    WelcomeLabel.grid(row=0, column=0, padx=10, pady=10)
    QuestionLabel.grid(row=2, column=0, padx=10, pady=10)
    StartButton.grid(row=3, column=1, padx=5)
    RulesButton.grid(row=3, column=2, padx=5)

  if command == "Hit":
    PlayerScore += CardsValues("player")
    PlayerLabel.config(text=PlayerName + "'s Score: " + str(PlayerScore))
    print(PlayerScore)
    print("Hit")
    if PlayerScore > 21:
      while PlayerAces > 0 and PlayerScore > 21:
        PlayerScore -= 10
        PlayerAces -= 1
      if PlayerScore > 21:
        OutcomeLabel.config(text=f"{PlayerName} Busted! Dealer Wins.")
        Chips -= PlayerBet
        ChipsLabel.config(text="Chips: " + str(Chips))
        return
    print(PlayerName + " Score: " + str(PlayerScore))

  if command == "Stand":
    while DealerScore < 17:
      card_val = CardsValues("dealer")
      DealerScore += card_val
      while DealerScore > 21 and DealerAces > 0:
        DealerScore -= 10
        DealerAces -= 1
      DealerLabel.config(text="Dealer Score: " + str(DealerScore))
    if DealerScore > 21:
        ClearScreen()
        BustLabel.config(text=PlayerName + "Wins! Dealer Bust (" + str(DealerScore) + ")")
        BustLabel.grid(row=1, column=1, padx=10, pady=10)
        Chips = Chips + PlayerBet
        GameLogic()
    else:
        GameLogic()

  if command == "CashOut":
    ClearScreen()
    print("Cash Out")
    BlackjackLabel.grid(row=0, column=0, padx=5, pady=10)
    PlayerName = NameEntry.get()
    TotalLabel.config(text=PlayerName + " total Chips: " + str(Chips))
    TotalLabel.grid(row=1, column=0, padx=5, pady=10)
    ResetButton.grid(row=2, column=0, padx=5)
  
  if command == "Reset":
    ClearScreen()
    print("Reseted Game")
    StartGame()

#General Game
Make_TKinter_Elements()
StartGame()

#Keeping game there
root.mainloop()