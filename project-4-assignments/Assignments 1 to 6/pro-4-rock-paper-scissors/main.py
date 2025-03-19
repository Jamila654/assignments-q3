import time
def rock_paper_scissors():
  print("Welcome to Rock, Paper, Scissors!")
  time.sleep(2)
  player1 = input("Enter player 1 name: ")
  player2 = input("Enter player 2 name: ")
  time.sleep(1)
  print("Enter r for rock, p for paper, s for scissors")
  player1_score = 0
  player2_score = 0
  attempts = 3
  while attempts <= 3:
    player1_choice = input(f"{player1}, enter your choice: ")
    if player1_choice not in ["r", "p", "s"]:
      print("Invalid input! You must enter r, p or s.")
      continue
    player2_choice = input(f"{player2}, enter your choice: ")
    if player2_choice not in ["r", "p", "s"]:
      print("Invalid input! You must enter r, p or s.")
      continue

    if player1_choice == player2_choice:
      print("It's a tie!")
      player1_score += 1
      player2_score += 1
    elif player1_choice == "r" and player2_choice == "s":
      print(f"{player1} wins!")
      player1_score += 1
    elif player1_choice == "p" and player2_choice == "r":
      print(f"{player1} wins!")
      player1_score += 1
    elif player1_choice == "s" and player2_choice == "p":
      print(f"{player1} wins!")
      player1_score += 1
    elif player2_choice == "r" and player1_choice == "s":
      print(f"{player2} wins!")
      player2_score += 1
    elif player2_choice == "p" and player1_choice == "r":
      print(f"{player2} wins!")
      player2_score += 1
    elif player2_choice == "s" and player1_choice == "p":
      print(f"{player2} wins!")
      player2_score += 1
    else:
      print("Invalid input! You must enter r, p or s.")
    attempts -= 1
    if attempts == 0:
      print("Game over!")
      print(f"{player1} score: {player1_score}")
      print(f"{player2} score: {player2_score}")
      if player1_score > player2_score:
        print(f"{player1} wins the game!")
      elif player1_score < player2_score:
        print(f"{player2} wins the game!")
      else:
        print("The game is a tie!")
      break


rock_paper_scissors()