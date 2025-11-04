#Leaderboard.py
#The leaderboard module to be used in Activity 1.2.2
import turtle as trtl
import random as rand
import a125_Shall_We_Play_a_Game

#Set the levels of scoring
bronze_score = 500
silver_score = 1000
gold_score = 5000

#Return names in the leaderboard file
def get_names(file_name):
  leaderboard_file = open(file_name, "r")

  names = []
  for line in leaderboard_file:
    leader_name = ""
    index = 0

    # Read the leader name (format: name,score)
    while (line[index] != ","):
      leader_name += line[index]
      index += 1

    names.append(leader_name)
    print("leader name is:", leader_name)

  leaderboard_file.close()
  return names


#Return scores from the leaderboard file
def get_scores(file_name):
  leaderboard_file = open(file_name, "r")

  scores = []
  for line in leaderboard_file:
    leader_score = ""
    index = 0

    # Move past the name
    while (line[index] != ","):
      index += 1
    index += 1

    # Get the score
    while index < len(line) and line[index] != "\n":
      leader_score += line[index]
      index += 1

    scores.append(int(leader_score))
    print("leader score is:", leader_score)

  leaderboard_file.close()
  return scores


#Update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):
  index = 0
  # Loop through scores to find correct position
  for index in range(len(leader_scores)):
    if (player_score > leader_scores[index]):
      break
    else:
      index = index + 1

  # Insert new player and score
  leader_names.insert(index, player_name)
  leader_scores.insert(index, player_score)

  # Keep only top 5
  if len(leader_names) > 5:
    leader_names.pop()
    leader_scores.pop()

  # Write updated leaderboard back to file
  leaderboard_file = open(file_name, "w")
  for i in range(len(leader_names)):
    leaderboard_file.write(leader_names[i] + "," + str(leader_scores[i]) + "\n")
  leaderboard_file.close()


#Draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-160,100)
  turtle_object.hideturtle()
  turtle_object.down()

  # Draw leaderboard entries
  for index in range(len(leader_names)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
    turtle_object.down()

  # Move turtle to new line
  turtle_object.penup()
  turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
  turtle_object.pendown()

  # Display message for making leaderboard or not
  if player_score >= leader_scores[-1]:
    turtle_object.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
  else:
    turtle_object.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)

  # Move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
  turtle_object.pendown()

  # Display medal message
  if player_score >= gold_score:
    turtle_object.write("You earned a gold medal!", font=font_setup)
  elif player_score >= silver_score:
    turtle_object.write("You earned a silver medal!", font=font_setup)
  elif player_score >= bronze_score:
    turtle_object.write("You earned a bronze medal!", font=font_setup)

def Leaderboard():
  # ---------- TESTING / DEMO SECTION ----------
  if __name__ == "__main__":
    file_name = "a125_leaderboard.txt"

    # Get existing names and scores
    names = get_names(file_name)
    scores = get_scores(file_name)

    # Example player data for testing
    from a125_Shall_We_Play_a_Game import player_name as player_name
    from a125_Shall_We_Play_a_Game import Chips as player_score

    print("\nAdding player:", player_name, "with score:", player_score)

    # Update leaderboard
    update_leaderboard(file_name, names, scores, player_name, player_score)

    # Draw leaderboard
    turtle = trtl.Turtle()
    draw_leaderboard(names[0], names, scores, turtle, player_score)
    trtl.done()