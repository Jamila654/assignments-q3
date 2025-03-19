import time, random
def hangman():
  user_name = input("What is your name? ")
  print("Hello, " + user_name + "!")
  time.sleep(1)
  print("Welcome to Hangman!")
  time.sleep(1)
  print("You have 5 guesses to get the word correct")
  words = ["python","programming","hangman","challenge","developer"]
  word = random.choice(words)
  attempts = 5
  correct_word = ["_"] * len(word)
  guessed_letters = []
  print("There are " + str(len(word)) + " letters "+  " ".join(correct_word))
  while attempts <=5:
    try:
      time.sleep(1)
      guess = input("\nGuess a letter: ").lower()
      if len(guess) != 1 or not guess.isalpha():
        raise ValueError
        continue
    except ValueError:
      print("Invalid input. Please enter a single letter.\n")
      continue

    if guess in guessed_letters:
      print("You have already guessed that letter.\n")
      continue
    guessed_letters.append(guess)
    if guess in word:
      for i in range(len(word)):
        if word[i] == guess:
          print(f"Good job! '{guess}' is in the word.")
          correct_word[i] = guess
          print(" ".join(correct_word))
      if "".join(correct_word) == word:
        print(f"Congratulations! You guessed the word correctly {word}!")
        break
    else:
      print(f"Sorry, '{guess}' is not in the word.")
      attempts -= 1
      if attempts != 1:
        print(f"You have {attempts} attempts left.")
      elif attempts == 1:
        print(f"You have {attempts} attempt left.")

      if attempts == 0:
        print("Sorry, you have run out of attempts.")
        break

hangman()