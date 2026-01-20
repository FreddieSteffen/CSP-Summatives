import tkinter as tk
import random as rand
from PIL import Image, ImageTk

SuitsList = ["Hearts", "Diamonds", "Spades", "Clubs"]
NumbersList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
PlayerCards = []
DealerCards = []

DealerScore = 0
PlayerScore = 0
PlayerBet = 0
PlayerAces = 0
DealerAces = 0
Chips = 100
GameState = "menu"
TITLE_FONT = ("Times New Roman", 48, "bold")
HEADER_FONT = ("Times New Roman", 24, "bold")
BODY_FONT = ("Times New Roman", 24)
SMALL_FONT = ("Times New Roman", 16)

def Make_TKinter_Elements():
  global root, TABLE_GREEN, TitleFrame, InfoFrame, TableFrame, ButtonFrame, OutcomeFrame, GameInfoFrame, DealerCardsFrame, PlayerCardsFrame, WelcomeLabel, NameEntry, QuestionLabel, StartButton, RulesButton, RulesTitle, RulesLabel, BackButton, CardValueLabel, DealerLabel, PlayerName, PlayerLabel, HitButton, StandButton, ReplayButton, BlackjackLabel, BetEntry, BetLabel, ChipsLabel, OutcomeLabel, CashoutButton, TotalLabel, ResetButton, HeartsImage, HeartsPhoto, HeartsLabel, DiamondsImage, DiamondsPhoto, DiamondsLabel, SpadesImage, SpadesPhoto, SpadesLabel, ClubsImage, ClubsPhoto, ClubsLabel, photo, StartingTextName, StartingTextBet
  root = tk.Tk()
  root.configure(bg="#8C1515")
  root.attributes('-fullscreen', True)
  root.title("Blackjack Create Task")
  root.columnconfigure(0, weight=1)
  TABLE_GREEN = "#3E9123"
  TitleFrame = tk.Frame(root, bg="#8C1515")
  InfoFrame = tk.Frame(root, bg="#8C1515")
  TableFrame = tk.Frame(root, bg=TABLE_GREEN, width=800, height=300)
  ButtonFrame = tk.Frame(root, bg="#8C1515")
  OutcomeFrame = tk.Frame(root, bg="#8C1515")
  GameInfoFrame = tk.Frame(InfoFrame, bg="#8C1515")
  TitleFrame.grid(row=0, column=0, sticky="ew", pady=5)
  InfoFrame.grid(row=1, column=0, sticky="ew")
  TableFrame.grid(row=2, column=0, pady=10)
  TableFrame.grid_propagate(False)
  ButtonFrame.grid(row=3, column=0, pady=10)
  OutcomeFrame.grid(row=4, column=0, pady=10)
  GameInfoFrame.grid(row=0, column=0, columnspan=4, pady=5, sticky="ew")
  root.columnconfigure(0, weight=1)
  GameInfoFrame.columnconfigure((0,1,2,3), weight=1)
  for frame in (TitleFrame, InfoFrame, ButtonFrame, OutcomeFrame):
    frame.columnconfigure(0, weight=1)
  ButtonFrame.columnconfigure((0,1), weight=1)
  DealerCardsFrame = tk.Frame(TableFrame, bg=TABLE_GREEN)
  DealerCardsFrame.grid(row=0, column=0, sticky="w", padx=10, pady=5)
  PlayerCardsFrame = tk.Frame(TableFrame, bg=TABLE_GREEN)
  PlayerCardsFrame.grid(row=1, column=0, sticky="w", padx=10, pady=5)

  WelcomeLabel = tk.Label(TitleFrame, text="Welcome to Blackjack", bg="#8C1515", fg="white", font=TITLE_FONT, padx=10)
  WelcomeLabel.grid(row=0, column=0, padx=5, pady=10)
  StartingTextName = "Enter Your Name Here:"
  NameEntry = tk.Entry(InfoFrame, bg="#FFFFFF", fg="#8C1515", font=("Source Sans 3", 14))
  NameEntry.insert(0, StartingTextName)
  NameEntry.bind("<Button-1>", ClearOnClick)
  NameEntry.grid(row=0, column=0, padx=5, pady=10)
  QuestionLabel = tk.Label(InfoFrame, text="If you would like to know the rules or just get right into it, click the respective buttons", compound="center", bg="#8C1515", fg="white", font=BODY_FONT, padx=10)
  QuestionLabel.grid(row=0, column=1, padx=5, pady=10)
  StartButton = tk.Button(ButtonFrame, text="Start", font=BODY_FONT, command=lambda:OnClick("Start"))
  StartButton.grid(row=0, column=1, padx=5)
  RulesButton = tk.Button(ButtonFrame, text="Rules", font=BODY_FONT, command=lambda:OnClick("Rules"))
  RulesButton.grid(row=0, column=2, padx=5)

  RulesTitle = tk.Label(ButtonFrame, text="Rules", bg="#8C1515", fg="white", font=HEADER_FONT, padx=10)
  RulesTitle.grid(row=0, column=0, padx=10, pady=10)
  RulesLabel = tk.Label(InfoFrame, text="The rules are that all players get cards face up, with the dealer's first card being face up and the second being not shown until you stand.\n The goal is to get closer to 21 points than the dealer does without going over 21.\n If your hand goes over 21, it is called a “bust” and you lose the betted amount.\n You can “hit” to get another card, or “stand” to not get anymore cards and then the dealer will “hit” until they are over the score of 17.\n The game is played with multiple decks so you may have multiple of the same card", bg="#8C1515", fg="white", font=SMALL_FONT, padx=10)
  RulesLabel.grid(row=1, column=0, padx=10, pady=10)
  BackButton = tk.Button(ButtonFrame, text="Back", font=BODY_FONT, command=lambda:OnClick("Back"))
  BackButton.grid(row=0, column=0, padx=5)

  CardValueLabel = tk.Label(root, bg="#8C1515")
  CardValueLabel.grid(row=1, column =1, padx=5, pady=10)
  DealerLabel = tk.Label(GameInfoFrame, text="Dealer Score: " + str(DealerScore), bg="#8C1515", fg="white", font=BODY_FONT, padx=5)
  DealerLabel.grid(row=0, column=0, padx=5, pady=10)
  PlayerName = NameEntry.get()
  PlayerLabel = tk.Label(GameInfoFrame, text=PlayerName +" Score: " + str(PlayerScore), bg="#8C1515", fg="white", font=BODY_FONT, padx=5)
  PlayerLabel.grid(row=0, column=1, padx=5, pady=10)
  HitButton = tk.Button(ButtonFrame, text="Hit", font=BODY_FONT, command=lambda:OnClick("Hit"))
  HitButton.grid(row=0, column=0, padx=5)
  StandButton = tk.Button(ButtonFrame, text="Stand", font=BODY_FONT, command=lambda:OnClick("Stand"))
  StandButton.grid(row=0, column=1, padx=5)
  ReplayButton = tk.Button(ButtonFrame, text="Replay", font=BODY_FONT, command=lambda:OnClick("Start"))
  ReplayButton.grid(row=0, column=2, padx=5)
  BlackjackLabel = tk.Label(TitleFrame, text="Blackjack", bg="#8C1515", fg="white", font=TITLE_FONT, padx=10)
  BlackjackLabel.grid(row=0, column=0, padx=5, pady=10)
  StartingTextBet = "Enter Bet Here:"
  BetEntry = tk.Entry(InfoFrame, bg="#FFFFFF", fg="#8C1515", font=("Source Sans 3", 14))
  BetEntry.insert(0, StartingTextBet)
  BetEntry.bind("<Button-1>", ClearOnClick)
  BetEntry.bind("<Return>", OnEnter)
  BetEntry.grid(row=1, column=0, padx=10, pady=10)
  BetLabel = tk.Label(GameInfoFrame, text="Bet: " + str(PlayerBet), font=BODY_FONT, padx=5)
  BetLabel.grid(row=0, column=2, padx=5, pady=10)
  ChipsLabel = tk.Label(GameInfoFrame, text="Chips: " + str(Chips), font=BODY_FONT, padx=5)
  ChipsLabel.grid(row=0, column=3, padx=5, pady=10)

  OutcomeLabel = tk.Label(OutcomeFrame, text="", bg="#8C1515", fg="white", font=BODY_FONT, padx=10)
  OutcomeLabel.grid(row=0, column=0, padx=10, pady=10)
  CashoutButton = tk.Button(ButtonFrame, text="Cash Out", font=BODY_FONT, command=lambda:OnClick("CashOut"))
  CashoutButton.grid(row=0, column=3, padx=5)
  TotalLabel = tk.Label(text=PlayerName + " total Chips: " + str(Chips), font=BODY_FONT)
  TotalLabel.grid(row=1, column=0, padx=5, pady=10)
  ResetButton = tk.Button(ButtonFrame, text="Reset Game", font=BODY_FONT, command=lambda:OnClick("Reset"))
  ResetButton.grid(row=3, column=0, padx=5)

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
  WelcomeLabel.grid(row=0, column=0, padx=10, pady=10)
  NameEntry.grid(row=0, column=0, padx=5, pady=10)
  QuestionLabel.grid(row=0, column=1, padx=10, pady=10)
  StartButton.grid(row=0, column=1, padx=5)
  RulesButton.grid(row=0, column=2, padx=5)
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
      PlayerAces = PlayerAces + 1
    else: 
      DealerAces = DealerAces+ 1
  elif card in ["King", "Queen", "Jack"]:
    value = 10
  else:
    value = int(card)
  return value, suit, card

def ShowCards(suit, CardName, target):
  global HeartsPhoto, DiamondsPhoto, SpadesPhoto, ClubsPhoto, PlayerCards, DealerCards
  if suit == "Hearts":
    photo = HeartsPhoto
  elif suit == "Diamonds":
    photo = DiamondsPhoto
  elif suit == "Spades":
    photo = SpadesPhoto
  else:
    photo = ClubsPhoto
  CardFrame = tk.Frame(TableFrame, bg=TABLE_GREEN, width=photo.width(), height=photo.height())
  CardFrame.grid_propagate(False)
  imgLabel = tk.Label(CardFrame, image=photo, bg=TABLE_GREEN)
  imgLabel.image = photo
  imgLabel.place(x=0, y=0)
  if CardName in ["Jack", "Queen", "King", "Ace"]:
    CardNameDisplay = CardName[0]
  else:
    CardNameDisplay = CardName

  ValueLabel = tk.Label(CardFrame, text=CardNameDisplay, fg="black", bg="white", font=("times", 16, "bold"))
  ValueLabel.place(relx=0.5, rely=0.5, anchor="center")
  if target == "player":
    CardFrame.pack(side="left", in_=PlayerCardsFrame, padx=10, pady=5)
    PlayerCards.append(CardFrame)
  else:
    CardFrame.pack(side="left", in_=DealerCardsFrame, padx=10, pady=5)
    DealerCards.append(CardFrame)

def ResetCards():
  global PlayerCards, DealerCards
  for card in PlayerCards:
    card.destroy()
  for card in DealerCards:
    card.destroy()
  PlayerCards = []
  DealerCards = []

def ClearOnClick(event):
  if event.widget == BetEntry and BetEntry.get() == StartingTextBet:
    BetEntry.delete(0, tk.END)
  if event.widget == NameEntry and NameEntry.get() == StartingTextName:
    NameEntry.delete(0, tk.END)

def OnEnter(event):
  global PlayerBet, Chips, PlayerScore, DealerScore, PlayerName, GameState
  if GameState != "betting":
    return
  if Chips <= 0: 
    ClearScreen()
    ResetCards()
    NameEntry.config(state="normal")
    PlayerAces = 0
    DealerAces = 0
    StartGame()
  BetText = BetEntry.get()
  if not BetText.isdigit():
    BetEntry.delete(0, tk.END)
    BetEntry.insert(0, "Enter a number")
    return
  PlayerBet = int(BetText)
  if PlayerBet <= 0 or PlayerBet > Chips:
    BetEntry.delete(0, tk.END)
    BetEntry.insert(0, text="Max bet: " + str(Chips))
    return
  Chips = Chips - PlayerBet
  GameState = "playing"
  BetEntry.grid_remove()
  BetLabel.config(text="Bet: " + str(PlayerBet))
  ChipsLabel.config(text="Chips: " + str(Chips))
  BetLabel.grid(row=0, column=2, padx=5, pady=10)
  ChipsLabel.grid(row=0, column=3, padx=5, pady=10)
  HitButton.grid(row=0, column=0, padx=5)
  StandButton.grid(row=0, column=1, padx=5)
  HitButton.config(state="normal")
  StandButton.config(state="normal")
  TableFrame.grid()
  for i in range(2):
    CardVal, CardSuit, CardName = CardsValues("player")
    PlayerScore = PlayerScore+ CardVal
    ShowCards(CardSuit, CardName, "player")
  CardVal, CardSuit, CardName = CardsValues("dealer")
  DealerScore = DealerScore + CardVal
  ShowCards(CardSuit, CardName, "dealer")
  PlayerName = NameEntry.get()
  PlayerLabel.config(text=PlayerName + "'s Score: " + str(PlayerScore))
  NameEntry.config(state="disabled")
  DealerLabel.config(text="Dealer Score: " + str(DealerScore))
  DealerLabel.grid(row=0, column=0, padx=5, pady=10)
  PlayerLabel.grid(row=0, column=1, padx=5, pady=10)

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
  ReplayButton.grid(row=0, column=0, padx=5)
  if PlayerScore > 21:
    OutcomeLabel.config(text="You busted! Dealer wins.")
  elif DealerScore > 21:
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
  OutcomeLabel.grid(row=4, column=0, padx=10, pady=10)
  ChipsLabel.config(text="Chips: " + str(Chips))
  ChipsLabel.grid(row=0, column=2, padx=5, pady=10)
  CashoutButton.grid(row=0, column=3, padx=5)

def OnClick(command):
  global PlayerScore, DealerScore, Chips, PlayerName, PlayerAces, DealerAces, PlayerBet, GameState
  if command == "Start":
    GameState = "betting"
    ClearScreen()
    ResetCards()
    PlayerScore = 0
    DealerScore = 0
    PlayerBet = 0
    PlayerAces = 0
    DealerAces = 0
    BlackjackLabel.grid(row=0, column=0, padx=5, pady=10)
    BetEntry.grid(row=1, column=0, padx=10, pady=10)
  if command == "Rules":
    ClearScreen()
    BlackjackLabel.grid(row=0, column=0, padx=10, pady=10)
    RulesTitle.grid(row=0, column=0, padx=10, pady=10)
    RulesLabel.grid(row=0, column=0, padx=10, pady=10)
    BackButton.grid(row=0, column=0, padx=5)
  if command == "Back":
    ClearScreen()
    WelcomeLabel.grid(row=0, column=0, padx=10, pady=10)
    QuestionLabel.grid(row=0, column=0, padx=10, pady=10)
    StartButton.grid(row=0, column=0, padx=5)
    RulesButton.grid(row=0, column=1, padx=5)
  if command == "Hit":
    CardVal, CardSuit, CardName = CardsValues("player")
    PlayerScore = PlayerScore + CardVal
    ShowCards(CardSuit, CardName, "player")
    if PlayerScore > 21:
      while PlayerAces > 0 and PlayerScore > 21:
        PlayerScore = PlayerScore - 10
        PlayerAces = PlayerAces - 1
      if PlayerScore > 21:
        GameLogic()
        return
    PlayerLabel.config(text=PlayerName + "'s Score: " + str(PlayerScore))
  if command == "Stand":
    if GameState != "playing":
      return
    while DealerScore < 17:
      CardVal, CardSuit, CardName = CardsValues("dealer")
      DealerScore = DealerScore + CardVal
      ShowCards(CardSuit, CardName, "dealer")
      while DealerScore > 21 and DealerAces > 0:
        DealerScore = DealerScore - 10
        DealerAces = DealerAces - 1
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
    HitButton.grid_remove()
    StandButton.grid_remove()
    BlackjackLabel.grid(row=0, column=0, padx=5, pady=10)
    TotalLabel.config(text=PlayerName + "'s total Chips: " + str(Chips))
    TotalLabel.grid(row=1, column=0, padx=5, pady=10)
    ResetButton.grid(row=3, column=0, padx=5)
  if command == "Reset":
    ClearScreen()
    ResetCards()
    NameEntry.config(state="normal")
    PlayerAces = 0
    DealerAces = 0
    StartGame()
Make_TKinter_Elements()
StartGame()
root.bind("<Escape>", lambda e:root.attributes("-fullscreen", False))
root.mainloop()

#Comments in order
#CreateTask.py
#Imports
#Lists
#Variables
#Fonts and Sizes
#Functions
#Frames for things so they don't overlap
#Starting Screen
#Rules Screen
#Game Screen 
#Post-Game Screen
#Card Images
#Clears Most of Screen so I can just Regrid them when needed
#Sets up the Starting Screen (Both at setup and resetting)
#Sets the value of each random Card
#Shows the Cards Images
#Frame that holds the card
#Card image
#Card value that goes onto the image
#Resets the Cards
#Clears text entrys
#When the player enters on the bet it goes to the Game Screen
#Validation
#Starting Cards
#Things the Player Will See
#Finds out who wins (Player or Dealer) and give the player the proper chips
#Chips Removed Earlier
#When buttons are clicked do what they are meant to
# #Sets up the Betting
#Brings player to Rules Screen
#Brings Player Back to Starting Screen
#Gives Player another Card
#Finds Dealers Score
#Shows players total Chips and lets them Replay
#Resets the Game
#General Game
#Keeping the game there