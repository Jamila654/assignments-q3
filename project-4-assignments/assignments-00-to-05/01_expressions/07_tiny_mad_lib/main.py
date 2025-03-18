#type: ignore
from colorama import Fore, Style
def main():
    print(Fore.BLUE + "\n\t\t\t\t\t\t\t\tWelcome to Madlibs!" + Style.BRIGHT + "\n")
    print(Fore.CYAN + "\t\tPlease enter the following words to create a story 👇" + Style.BRIGHT)
    print(Fore.GREEN + Style.BRIGHT)
    adjective1 = input("\t\tEnter an adjective: ")
    noun1 = input("\t\tEnter a noun: ")
    verb_past1 = input("\t\tEnter a verb (past tense): ")
    adverb1 = input("\t\tEnter an adverb: ")
    adjective2 = input("\t\tEnter another adjective: ")
    noun2 = input("\t\tEnter another noun: ")
    noun3 = input("\t\tEnter one more noun: ")
    adjective3 = input("\t\tEnter one more adjective: ")
    verb1 = input("\t\tEnter a verb: ")
    adverb2 = input("\t\tEnter another adverb: ")
    verb_past2 = input("\t\tEnter another verb (past tense): ")
    adjective4 = input("\t\tEnter a final adjective: ")

    story = f"""Once upon a time, in a {adjective1} land, there was a {noun1} who loved to {verb_past1} {adverb1}.
    \t\tOne day, the {noun1} found a {adjective2} {noun2} lying on the ground. Curious, the {noun1} picked it up and
    \t\tdecided to take it to the {noun3}. Along the way, the {noun1} encountered a {adjective3} creature who tried to
    \t\t{verb1} {adverb2}. But the {noun1} {verb_past2} quickly and escaped safely. In the end, the {noun1}
    \t\tfelt {adjective4} and lived happily ever after.
    """
    print(Fore.BLUE + "\n\t\tHere's your Mad Libs story: \n" + Style.BRIGHT)
    print(Fore.CYAN + f"\t\t{story}\n" + Style.BRIGHT)

    print(Fore.GREEN + Style.BRIGHT)
    play_again = input( "\t\tDo you want to play again? (yes/no) ")
    if play_again.lower() == "yes":
        madlibs()
    else:
        print("\t\tThanks for playing!☺️")


if __name__ == "__main__":
    main()
