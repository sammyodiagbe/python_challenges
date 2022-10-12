from tabnanny import check
from random_word import RandomWords

word = RandomWords().get_random_word()

print(word)

word_array = ["_"] * len(word)
game_is_done = False
missed_chance = 0


def check_game_status(check_array):
    for word in check_array:
        if word is None:
            return False
    return True
def draw_word(word):
    string = ""
    for character in word:
        string += character
    print(string)
    print()
    print(f"----------|")
    print(f" |        |")
    print(f" 0        |")
    print(f"{'/' if missed_chance >= 1 else ''}|{chr(92) if missed_chance >= 2 else ''}      |")
    print(" | ")
    print(f"{'/' if missed_chance >= 3 else ''}|{chr(92) if missed_chance >= 4 else ''}      |")


def check_game_status(word, word_array):
    if word == ''.join(word_array):
        return True
    if missed_chance >= 4:
        return True
    return False


# while the game is not done
while(not game_is_done):
    draw_word(word_array)
    user_selection = input('Enter a letter')
    # if the user enters a character that is in the word
    if user_selection in word:
        for index in range(len(word)):
            if word[index] == user_selection:
                word_array[index] = user_selection
    else:

       
        missed_chance += 1
    game_is_done = check_game_status(word, word_array)

    
print(word)