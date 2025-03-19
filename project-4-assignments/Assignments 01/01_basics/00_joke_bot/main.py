#type: ignore
def main():
 PROMPT: str = "What do you want? (joke/quit) "
 JOKE: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
 SORRY: str = "Sorry I only tell jokes."
 
 ai = input(PROMPT)
 while ai != "quit":
     if "joke" in ai:
         print(JOKE)
     else:
         print(SORRY)
     ai = input(PROMPT)


if __name__ == "__main__":
    main()
