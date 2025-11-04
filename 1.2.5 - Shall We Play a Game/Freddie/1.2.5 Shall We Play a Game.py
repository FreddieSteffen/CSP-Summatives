# 1.2.5 Shall We Play a Game Summitive
# Blackjack/Slots Game

import turtle as trtl
import random as rand
import tkinter as tk
from PIL import Image
'''import leaderboard as lb'''

#Turtle and screen setup
t = trtl.Turtle()  # Named this to save some time
wn = trtl.Screen()
screen = trtl.Screen()  #Used later for onclick

#Image resizing and card shapes
def resize_card(name, size):
    img = Image.open(f"{name}.gif")
    img = img.resize(size)
    img.save(f"{name}_small.gif")

for suit in ["hearts", "diamonds", "clubs", "spades"]:
    resize_card(suit, (30, 30))

hearts = "hearts_small.gif"
diamonds = "diamonds_small.gif"
clubs = "clubs_small.gif"
spades = "spades_small.gif"
wn.addshape(hearts)
wn.addshape(diamonds)
wn.addshape(clubs)
wn.addshape(spades)

hearts = trtl.Turtle(shape=hearts)
hearts.hideturtle()
diamonds = trtl.Turtle(shape=diamonds)
diamonds.hideturtle()
clubs = trtl.Turtle(shape=clubs)
clubs.hideturtle()
spades = trtl.Turtle(shape=spades)
spades.hideturtle()
player_card_turtles = []
card_turtle = trtl.Turtle()  # Draws outlines and numbers
card_turtle.hideturtle()
card_turtle.penup()
card_turtle.speed(0)

#Lists
SuitsList = ["Hearts", "Diamonds", "Spades", "Clubs"]
NumList = [1,2,3,4,5,6,7,8,9,10,11,12,13]

CardX = [20,160,-220,20,160,-220,20,160,-220,0]
OutlineX = [0,140,-240,0,140,-240,0,0]

PlayerOptions = ["Hit", "Stand", "bet"]
Options = PlayerOptions[0]

#Variables
CardName = ""
TempPlayerValue = 0
TempDealerValue = 0
PlayerScore = 0
DealerScore = 0
Chips = 100
max_chars = 8

#Functions
def FaceCardValue():
    global CardValue
    global CardSuit
    global CardName
    if CardValue == 13:
        CardValue = 10
        CardName = "King"
    if CardValue == 12:
        CardValue = 10
        CardName = "Queen"
    if CardValue == 11:
        CardValue = 10
        CardName = "Jack"
    if CardValue == 1:
        CardValue = 11
        CardName = "Ace"
    else:
        CardName = str(CardValue)
    print(CardName, "of", CardSuit)

def writerMove():
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.setheading(90)
    t.back(20)
    t.pendown()

def CardOutline():
    for i in range(2):
        t.forward(125)
        t.right(90)
        t.forward(150)
        t.right(90)

#Core game display
def MainGameCreate():
    global PlayerScore
    global DealerScore
    t.hideturtle()
    t.penup()
    t.goto(-200,200)
    t.write("Dealer", font=("Arial", 14, "bold"))

    t.goto(160,200)
    t.write(str(player_name), font=("Arial", 14, "bold"))

    t.goto(-200,-160)
    t.write("Dealer Score:" + str(DealerScore), font=("Arial", 14, "bold"))

    t.goto(160,-160)
    t.write(player_name + "Score:" + str(PlayerScore), font=("Arial", 14, "bold"))

    global Options
    pen.fillcolor("grey")
    pen.penup()
    pen.goto(-85,-200)
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.write("Hit", align="center", font=("Arial", 14, "bold"))

    pen.fillcolor("grey")
    pen.penup()
    pen.goto(5,-200)
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.write("Stand", align="center", font=("Arial", 14, "bold"))

score_turtle = trtl.Turtle()
chips_turtle = trtl.Turtle()
button_turtle = trtl.Turtle()
ChipsT = trtl.Turtle()

def update_display():
    # Clear previous display turtles
    score_turtle = trtl.Turtle()
    chips_turtle = trtl.Turtle()
    button_turtle = trtl.Turtle()

    for turt in [score_turtle, chips_turtle, button_turtle]:
        turt.hideturtle()
        turt.penup()
        turt.speed(0)

    # Write player/dealer scores
    score_turtle.goto(0, 100)
    score_turtle.write(f"Dealer: {DealerScore}   {player_name}: {PlayerScore}", align="center", font=("Arial", 15, "bold"))

    # Write chips
    chips_turtle.goto(0, -100)
    chips_turtle.write(f"Chips: {Chips}", align="center", font=("Arial", 15, "bold"))

    # Draw "Continue" button
    button_turtle.fillcolor("grey")
    button_turtle.goto(-200, 200)
    button_turtle.pendown()
    button_turtle.begin_fill()
    for i in range(2):
        button_turtle.forward(80)
        button_turtle.left(90)
        button_turtle.forward(40)
        button_turtle.left(90)
    button_turtle.end_fill()
    button_turtle.penup()
    button_turtle.goto(-160, 210)
    button_turtle.write("Continue", align="center", font=("Arial", 14, "bold"))

    # Draw "Cash Out" button
    button_turtle.goto(200, 200)
    button_turtle.pendown()
    button_turtle.begin_fill()
    for i in range(2):
        button_turtle.forward(80)
        button_turtle.left(90)
        button_turtle.forward(40)
        button_turtle.left(90)
    button_turtle.end_fill()
    button_turtle.penup()
    button_turtle.goto(240, 210)
    button_turtle.write("Cash Out", align="center", font=("Arial", 14, "bold"))

def Cashout():
    global Chips
    ChipsT = trtl.Turtle()
    ChipsT.hideturtle()
    ChipsT.penup()
    ChipsT.speed(0)
    ChipsT.goto(0,160)
    ChipsT.write(f"You got {Chips} Chips.", font=("Arial", 14, "bold"))

#Blackjack logic
def Blackjack():
    global CardValue, TempPlayerValue, PlayerScore, CardSuit, CardName, Chips, bet
    #Generate a new random card
    CardValue = rand.choice(NumList)
    CardSuit = rand.choice(SuitsList)
    FaceCardValue()
    #Add value to player score
    TempPlayerValue = CardValue
    PlayerScore += TempPlayerValue
    #Adjust for Ace if over 21
    if PlayerScore > 21 and CardName == "Ace":
        PlayerScore -= 10
    print(f"{player_name} score is {PlayerScore}")
    #Redraw display with new score
    '''update_display()'''
    #Lose condition
    if PlayerScore > 21:
        Chips -= int(bet)
        print("Busted! Chips:", Chips)
        t.clear()
        pen.clear()
        hearts.clear()
        diamonds.clear()
        spades.clear()
        clubs.clear()
        t.penup()
        t.goto(-20, 100)
        t.write("You lost", align="center", font=("Arial", 20, "bold"))
        ReplayGame()

def StartingCards():
    global DealerScore, PlayerScore, CardValue, CardSuit, TempDealerValue, CardName

    clear_screen()
    PlayerScore = 0
    DealerScore = 0

    # Deal two cards to player
    for i in range(2):
        CardValue = rand.choice(NumList)
        CardSuit = rand.choice(SuitsList)
        FaceCardValue()
        PlayerScore += CardValue
        x = CardX[0]
        DrawCards(x, 160, CardName, CardSuit)
        CardX.pop(0)

    # Deal one card to dealer
    CardValue = rand.choice(NumList)
    CardSuit = rand.choice(SuitsList)
    FaceCardValue()
    TempDealerValue = CardValue
    DealerScore += TempDealerValue
    x = CardX[0]
    DrawCards(x, 160, CardName, CardSuit)
    CardX.pop(0)

    # Update visible info (but NOT the dealer’s hidden logic)
    '''update_display()'''
    MainGameCreate()

def Dealer():
    global CardValue
    global TempDealerValue
    global DealerScore
    global CardSuit
    global Chips
    global bet

    while DealerScore < 17:
        CardValue = rand.choice(NumList)
        CardSuit = rand.choice(SuitsList)
        FaceCardValue()
        TempDealerValue = CardValue
        DealerScore = DealerScore + TempDealerValue
        pen.clear()
        t.clear()

    if DealerScore < PlayerScore and DealerScore <= 21 and PlayerScore <= 21:
        Chips = Chips + int(bet)
    if DealerScore == PlayerScore and DealerScore <= 21 and PlayerScore <= 21:
        Chips = Chips
    if DealerScore > PlayerScore and DealerScore <= 21 and PlayerScore <= 21:
        Chips = Chips - int(bet)
    print("Dealer score is", DealerScore)
    clear_screen()
    ReplayGame()

#Clearing everything on the screen
def clear_screen():
    t.speed(0)
    t.clear()
    pen.clear()
    hearts.clear()
    diamonds.clear()
    spades.clear()
    clubs.clear()
    # clear any last player card
    for ct in player_card_turtles:
        ct.clear()
        ct.hideturtle()
    player_card_turtles.clear()
    # also clear display turtles if you have them
    try:
        score_turtle.clear()
        chips_turtle.clear()
        button_turtle.clear()
    except NameError:
        pass
    wn.update()

#Drawing a new card
def DrawCards(x, y, card_name, card_suit):
    y = 160
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Draw outline
    for i in range(2):
        t.forward(125)
        t.right(90)
        t.forward(150)
        t.right(90)
    t.penup()
    
    # Write card name/number
    t.goto(x + 80, 135)
    t.write(card_name, font=("Arial", 20, "bold"))
    t.goto(x + 30, 10)
    t.write(card_name, font=("Arial", 20, "bold"))
    
    # Stamp suit
    suit_turtle = {'Hearts': hearts, 'Diamonds': diamonds, 'Spades': spades, 'Clubs': clubs}[card_suit]
    suit_turtle.hideturtle()
    suit_turtle.penup()
    suit_turtle.goto(x + 30, 135)
    suit_turtle.stamp()
    suit_turtle.goto(x + 80, 30)
    suit_turtle.stamp()

#Setting things up to replay
def ReplayGame():
    global PlayerScore
    global DealerScore

    pen.fillcolor("grey")
    pen.penup()
    pen.goto(-200,200)
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.write("Continue", align="center", font=("Arial", 14, "bold"))

    pen.begin_fill()
    pen.penup()
    pen.goto(200,200)
    pen.pendown()
    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.write("Cash Out", align="center", font=("Arial", 14, "bold"))
    PlayerScore = 0
    DealerScore = 0

#Start screen, player name input, and buttons
t.penup()
t.goto(-160,250)
t.pendown()
t.write("Black Jack Simplified", font=("Arial", 35, "bold"))

player_name = trtl.textinput("Name", "Enter your name, with max char "+str(max_chars))
player_name = player_name[:max_chars]

while "," in player_name or len(player_name) == 0 or "1" in player_name or "2" in player_name or "3" in player_name or "4" in player_name or "5" in player_name or "6" in player_name or "7" in player_name or "8" in player_name or "9" in player_name:
  player_name = trtl.textinput("Name", "Please do not use a comma, nothing, or number Enter your name")

#Create a turtle for text and buttons
pen = trtl.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

def YesNoButtons():
    #Draw Yes button
    pen.goto(-100, -100)
    pen.fillcolor("green")
    pen.begin_fill()
    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.goto(-60, -90)
    pen.write("YES", align="center", font=("Arial", 14, "bold"))

    #Draw No button
    pen.goto(100, -100)
    pen.fillcolor("red")
    pen.begin_fill()
    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.goto(140, -90)
    pen.write("NO", align="center", font=("Arial", 14, "bold"))

    #Display question
    pen.goto(0, 200)
    pen.write("Do you want to know the rules?", align="center", font=("Arial", 18, "bold"))

YesNoButtons()

#Click handler
def on_click(x, y):
    global pen
    global OutX
    global Chips
    global DealerScore
    global PlayerScore

    #YES button area
    if -100 < x < -20 and -100 < y < -60:
        pen.clear()
        t.penup()
        t.goto(-100,160)
        t.write("The rules are:")
        writerMove()
        t.write("Get to as close of a score of 21 without going over")
        writerMove()
        t.write("You get 2 cards to start with value on them unless Jack, Queen, King, Ace")
        writerMove()
        t.write("Jack, Queen and King are worth 10pts and Ace is worth 11 unless you would be over 21")
        writerMove()
        t.write("First you have to bet")
        writerMove()
        t.write("You can hit to get 1 more card")
        writerMove()
        t.write("You can stand to keep current amount")
        writerMove()
        t.write("The dealer then flips their card")
        writerMove()
        t.write("If you are closer to 21 but not over you gain what you betted but if you were farther you lose that amount")
        writerMove()
        ReplayGame()

    #NO button area
    elif 100 < x < 180 and -100 < y < -60:
        pen.clear()
        t.clear()
        hearts.clear()
        diamonds.clear()
        spades.clear()
        clubs.clear()
        BetValue()
        ReplayGame()

    #Continue
    elif -200 < x < -120 and 200 < y < 240:
        clear_screen()
        BetValue()
        CardX = [20,100,160,240,-220,-140,20,100,160,240,-220,-140,0]
        OutlineX = [0,140,-240,0,140,-240,0,0]
        x = CardX[0]
        OutX = OutlineX[0]

    #Cashout
    elif 200 < x < 280 and 200 < y < 240:
        clear_screen()
        Cashout()

    #Hit
    elif -85 < x < -5 and -200 < y < -160:  # Hit
        Blackjack()  # Update PlayerScore, CardName, CardSuit
        DrawCards(x, y, CardName, CardSuit)
        '''update_display()'''

    #Stand
    elif 5 < x < 85 and -200 < y < -160:
        #Player stands then dealer reveals cards
        Dealer()
        '''update_display()'''

#Listen for clicks
screen.onclick(on_click)

#Betting and Main game
def BetValue():
    global bet
    global Chips
    bet = trtl.textinput("Bet", "How much do you want to bet")
    if bet.isnumeric():
        if int(bet) <= Chips:
            clear_screen()
            StartingCards()
        else:
            bet = trtl.textinput("Bet", "Please enter only valid numbers")
    else:
        bet = trtl.textinput("Bet", "Please enter only valid numbers")

#Begin Playing
clear_screen()
BetValue()

#Keeping whats on the screen there
wn = trtl.Screen()
wn.mainloop()