#FreddieSteffen_CreateTask.py

#Imports
import tkinter as tk
import random as rand
from PIL import Image, ImageTk

#Lists
SuitsList = ["Hearts", "Diamonds", "Spades", "Clubs"]
NumbersList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
PlayerCards = []
DealerCards = []

#Variables
DealerScore = 0
PlayerScore = 0
PlayerBet = 0
PlayerAces = 0
DealerAces = 0
Chips = 100
GameState = "menu"

#Functions
#TKinter Elements
def Make_TKinter_Elements():
  global root, button_frame, WelcomeLabel, QuestionLabel, StartButton, RulesButton, StartingTextName, NameEntry, PlayerName, RulesTitle, RulesLabel, BackButton, DealerLabel, PlayerLabel, HitButton, StandButton, ReplayButton, BlackjackLabel, StartingTextBet, BetEntry, PlayerBet, BetLabel, ChipsLabel, OutcomeLabel, CashoutButton, TotalLabel, ResetButton, photo, HeartsImage, HeartsLabel, DiamondsImage, DiamondsLabel, ClubsImage, ClubsLabel, SpadesImage, SpadesLabel, HeartsPhoto, DiamondsPhoto, ClubsPhoto, SpadesPhoto, CardValueLabel, TABLE_GREEN, TableFrame, DealerCardsFrame, PlayerCardsFrame
  root = tk.Tk()
  root.configure(bg="#8C1515")
  root.title("Freddie Steffen Create Task")
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

  TABLE_GREEN = "#3E9123"
  TableFrame = tk.Frame(root, bg=TABLE_GREEN, width=800, height=300)
  TableFrame.grid(row=4, column=0, columnspan=3, pady=10)
  TableFrame.grid_propagate(False)
  DealerCardsFrame = tk.Frame(TableFrame, bg=TABLE_GREEN)
  DealerCardsFrame.grid(row=0, column=0, sticky="w", padx=10, pady=5)
  PlayerCardsFrame = tk.Frame(TableFrame, bg=TABLE_GREEN)
  PlayerCardsFrame.grid(row=1, column=0, sticky="w", padx=10, pady=5)

  QuestionLabel = tk.Label(root, text="If you would like to know the rules or just get right into it, click the respective buttons", compound="center", bg="#8C1515", fg="white", font=("times", 12), padx=10)
  QuestionLabel.grid(row=2, column=0, padx=5, pady=10)
  StartButton = tk.Button(button_frame, text="Start", command=lambda:OnClick("Start"))
  StartButton.grid(row=3, column=1, padx=5)
  RulesButton = tk.Button(button_frame, text="Rules", command=lambda:OnClick("Rules"))
  RulesButton.grid(row=3, column=2, padx=5)

  RulesTitle = tk.Label(root, text="Rules", bg="#8C1515", fg="white", font=("times", 24, "bold"), padx=10)
  RulesTitle.grid(row=0, column=0, padx=10, pady=10)
  RulesLabel = tk.Label(root, text="The rules are that all players get cards face up, with the dealer's first card being face up and the second being not shown until you stand.\n The goal is to get closer to 21 points than the dealer does without going over 21.\n If your hand goes over 21, it is called a “bust” and you lose the betted amount.\n You can “hit” to get another card, or “stand” to not get anymore cards and then the dealer will “hit” until they are over the score of 17.\n The game is played with multiple decks so you may have multiple of the same card.", bg="#8C1515", fg="white", font=("times", 12), padx=10)
  RulesLabel.grid(row=1, column=0, padx=10, pady=10)
  BackButton = tk.Button(button_frame, text="Back", command=lambda:OnClick("Back"))
  BackButton.grid(row=2, column=0, padx=5)

  DealerLabel = tk.Label(root, text="Dealer Score: " + str(DealerScore), bg="#8C1515", fg="white", font=("times", 12), padx=10)
  DealerLabel.grid(row=1, column=0, padx=5, pady=10)
  #So that the PlayerLabel wont cause an error at the beggining
  PlayerName = NameEntry.get()
  PlayerLabel = tk.Label(root, text=PlayerName +" Score: " + str(PlayerScore), bg="#8C1515", fg="white", font=("times", 12), padx=10)
  PlayerLabel.grid(row=1, column=1, padx=5, pady=10)
  HitButton = tk.Button(button_frame, text="Hit", command=lambda:OnClick("Hit"))
  HitButton.grid(row=2, column=0, padx=5)
  StandButton = tk.Button(button_frame, text="Stand", command=lambda:OnClick("Stand"))
  StandButton.grid(row=2, column=1, padx=5)
  ReplayButton = tk.Button(button_frame, text="Replay", command=lambda:OnClick("Start"))
  ReplayButton.grid(row=2, column=2, padx=5)

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

  CashoutButton = tk.Button(button_frame, text="Cash Out", command=lambda:OnClick("CashOut"))
  CashoutButton.grid(row=2, column=3, padx=5)
  TotalLabel = tk.Label(text=PlayerName + " total Chips: " + str(Chips))
  TotalLabel.grid(row=1, column=0, padx=5, pady=10)
  ResetButton = tk.Button(text="Reset Game", command=lambda:OnClick("Reset"))
  ResetButton.grid(row=2, column=0, padx=5)

  HeartsImage = Image.open("Hearts.png")
  HeartsPhoto = ImageTk.PhotoImage(HeartsImage)
  photo = ImageTk.PhotoImage(HeartsImage)
  HeartsLabel = tk.Label(root, image=photo)
  HeartsLabel.grid(row=2, column=0, padx=5, pady=10)
  DiamondsImage = Image.open("Diamonds.png")
  DiamondsPhoto = ImageTk.PhotoImage(DiamondsImage)
  photo = ImageTk.PhotoImage(DiamondsImage)
  DiamondsLabel = tk.Label(root, image=photo)
  DiamondsLabel.grid(row=2, column=0, padx=5, pady=10)
  SpadesImage = Image.open("Spades.png")
  SpadesPhoto = ImageTk.PhotoImage(SpadesImage)
  photo = ImageTk.PhotoImage(SpadesImage)
  SpadesLabel = tk.Label(root, image=photo)
  SpadesLabel.grid(row=2, column=0, padx=5, pady=10)
  ClubsImage = Image.open("Clubs.png")
  ClubsPhoto = ImageTk.PhotoImage(ClubsImage)
  photo = ImageTk.PhotoImage(ClubsImage)
  ClubsLabel = tk.Label(root, image=photo)
  ClubsLabel.grid(row=2, column=0, padx=5, pady=10)

  CardValueLabel = tk.Label(root, bg="#8C1515")
  CardValueLabel.grid(row=1, column =1, padx=5, pady=10)

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
  ReplayButton.grid_remove()
  BlackjackLabel.grid_remove()
  BetEntry.grid_remove()
  BetLabel.grid_remove()
  ChipsLabel.grid_remove()
  OutcomeLabel.grid_remove()
  CashoutButton.grid_remove()
  TotalLabel.grid_remove()
  ResetButton.grid_remove()
  HeartsLabel.grid_remove()
  DiamondsLabel.grid_remove()
  SpadesLabel.grid_remove()
  ClubsLabel.grid_remove()
  CardValueLabel.grid_remove()

def StartGame():
  global DealerScore, PlayerScore, PlayerBet, Chips
  ClearScreen()
  ResetCards()
  TableFrame.grid_remove()
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
  return value, suit, card

def ShowCards(suit, card_name, target):
  global HeartsPhoto, DiamondsPhoto, SpadesPhoto, ClubsPhoto, PlayerCards, DealerCards

  if suit == "Hearts":
    photo = HeartsPhoto
  elif suit == "Diamonds":
    photo = DiamondsPhoto
  elif suit == "Spades":
    photo = SpadesPhoto
  else:
    photo = ClubsPhoto

  #Frame that holds the card
  card_frame = tk.Frame(TableFrame, bg=TABLE_GREEN, width=photo.width(), height=photo.height())
  card_frame.grid_propagate(False)

  #Card image
  img_label = tk.Label(card_frame, image=photo, bg=TABLE_GREEN)
  img_label.image = photo
  img_label.place(x=0, y=0)

  if card_name in ["Jack", "Queen", "King", "Ace"]:
    card_name_display = card_name[0]
  else:
    card_name_display = card_name

  #Card value that goes onto the image
  value_label = tk.Label(card_frame, text=card_name_display, fg="black", bg="white", font=("times", 16, "bold"))
  value_label.place(relx=0.5, rely=0.5, anchor="center")
  if target == "player":
    card_frame.pack(side="left", in_=PlayerCardsFrame, padx=10, pady=5)
    PlayerCards.append(card_frame)
  else:
    card_frame.pack(side="left", in_=DealerCardsFrame, padx=10, pady=5)
    DealerCards.append(card_frame)

def ResetCards():
  global PlayerCards, DealerCards
  for card in PlayerCards:
    card.destroy()
  for card in DealerCards:
    card.destroy()
  PlayerCards = []
  DealerCards = []

def clear_on_click(event):
  if event.widget == BetEntry and BetEntry.get() == StartingTextBet:
    BetEntry.delete(0, tk.END)
  if event.widget == NameEntry and NameEntry.get() == StartingTextName:
    NameEntry.delete(0, tk.END)

def on_enter(event):
  global PlayerBet, Chips, PlayerScore, DealerScore, PlayerName, GameState
  if GameState != "betting":
    return
  if Chips <= 0:
    StartGame()
    return
  #Validation
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
  Chips -= PlayerBet
  GameState = "playing"
  BetEntry.grid_remove()
  BetLabel.config(text="Bet: " + str(PlayerBet))
  ChipsLabel.config(text="Chips: " + str(Chips))
  BetLabel.grid(row=0, column=1, padx=5, pady=10)
  ChipsLabel.grid(row=0, column=2, padx=5, pady=10)
  HitButton.grid(row=2, column=0, padx=5)
  StandButton.grid(row=2, column=1, padx=5)
  HitButton.config(state="normal")
  StandButton.config(state="normal")

  TableFrame.grid()
  for i in range(2):
    card_val, card_suit, card_name = CardsValues("player")
    PlayerScore += card_val
    ShowCards(card_suit, card_name, "player")
  card_val, card_suit, card_name = CardsValues("dealer")
  DealerScore += card_val
  ShowCards(card_suit, card_name, "dealer")

  PlayerName = NameEntry.get()
  PlayerLabel.config(text=PlayerName + "'s Score: " + str(PlayerScore))
  NameEntry.config(state="disabled")
  DealerLabel.config(text="Dealer Score: " + str(DealerScore))
  PlayerLabel.grid(row=1, column=1, padx=5, pady=10)
  DealerLabel.grid(row=1, column=0, padx=5, pady=10)

def GameLogic():
  global DealerScore, PlayerScore, Chips, PlayerBet, GameState
  GameState = "round_over"
  HitButton.config(state="disabled")
  StandButton.config(state="disabled")
  HitButton.grid_remove()
  StandButton.grid_remove()
  WelcomeLabel.grid_remove()
  QuestionLabel.grid_remove()
  BetEntry.grid_remove()
  BlackjackLabel.grid(row=0, column=0, padx=5, pady=10)
  ReplayButton.grid(row=2, column=0, padx=5)
  if PlayerScore > 21:
    OutcomeLabel.config(text="You busted! Dealer wins.")
  elif DealerScore > 21:
    #Chips Removed Earlier
    Chips = Chips + PlayerBet * 2
    OutcomeLabel.config(text="Dealer busted! You win.")
  elif PlayerScore > DealerScore:
    Chips = Chips + PlayerBet * 2
    OutcomeLabel.config(text="You win! " + str(PlayerScore) + "-" + str(DealerScore))
  elif DealerScore > PlayerScore:
    OutcomeLabel.config(text="Dealer wins. Dealer: " + str(DealerScore) + "-" + str(PlayerScore))
  else:
    Chips = Chips + PlayerBet
    OutcomeLabel.config(text="Push (tie).")
  OutcomeLabel.grid(row=1, column=0, padx=10, pady=10)
  ChipsLabel.config(text="Chips: " + str(Chips))
  ChipsLabel.grid(row=0, column=1, padx=5, pady=10)
  CashoutButton.grid(row=2, column=3, padx=5)

def OnClick(command):
  global PlayerScore, DealerScore, Chips, PlayerName, PlayerAces, DealerAces, PlayerBet, GameState
  if command == "Start":
    GameState = "betting"
    ClearScreen()
    ResetCards()
    TableFrame.grid_remove()
    PlayerScore = 0
    DealerScore = 0
    PlayerBet = 0
    PlayerAces = 0
    DealerAces = 0
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
    card_val, card_suit, card_name = CardsValues("player")
    PlayerScore += card_val
    ShowCards(card_suit, card_name, "player")
    print("Hit")
    if PlayerScore > 21:
      while PlayerAces > 0 and PlayerScore > 21:
        PlayerScore -= 10
        PlayerAces -= 1
      if PlayerScore > 21:
        GameLogic()
        return
    PlayerLabel.config(text=PlayerName + "'s Score: " + str(PlayerScore))
    print(PlayerName + " Score: " + str(PlayerScore))

  if command == "Stand":
    if GameState != "playing":
      return
    while DealerScore < 17:
      card_val, card_suit, card_name = CardsValues("dealer")
      DealerScore += card_val
      ShowCards(card_suit, card_name, "dealer")
      while DealerScore > 21 and DealerAces > 0:
          DealerScore -= 10
          DealerAces -= 1
      DealerLabel.config(text="Dealer Score: " + str(DealerScore))
    if DealerScore > 21:
        ClearScreen()
        GameLogic()
    else:
        GameLogic()

  if command == "CashOut":
    GameState = "cashout"
    ClearScreen()
    ResetCards()
    TableFrame.grid_remove()
    HitButton.grid_remove()
    StandButton.grid_remove()
    print("Cash Out")
    BlackjackLabel.grid(row=0, column=0, padx=5, pady=10)
    TotalLabel.config(text=PlayerName + " total Chips: " + str(Chips))
    TotalLabel.grid(row=1, column=0, padx=5, pady=10)
    ResetButton.grid(row=2, column=0, padx=5)
  
  if command == "Reset":
    ClearScreen()
    ResetCards()
    NameEntry.config(state="normal")
    print("Reset Game")
    PlayerAces = 0
    DealerAces = 0
    StartGame()

#General Game
Make_TKinter_Elements()
StartGame()

#Keeping game there
root.mainloop()