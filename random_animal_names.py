import random
from scraper import adjectives, animals

def random_word():
    choice = random.randint(1, 2)
    word1 = random.choice(adjectives)
    word2 = random.choice(adjectives)
    animal = random.choice(animals)
    
    if (choice == 1):
        return f"{word1} {word2} {animal}"
    else:
        return f"{word1} {animal}"


def main(n):
    final_list = []
    num = 0
    while num < int(n):
        word = random_word()
        while (word in final_list):
            word = random_word()
        final_list.append(word)
        num += 1
    
    for idx, word in enumerate(final_list, 1):
        print(f"{idx}: {word}")


def usr_input():
    num = input("Enter the number of words you want: ")
    main(num)

if __name__ == '__main__':
    # capitalise(adj_list, ani_list)
    usr_input()

