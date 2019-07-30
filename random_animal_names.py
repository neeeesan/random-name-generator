import random
import requests
from bs4 import BeautifulSoup

adj_page = requests.get('http://assets.gfycat.com/adjectives')
ani_page = requests.get('http://assets.gfycat.com/animals')

adj_bs = BeautifulSoup(adj_page.text, 'html.parser')
ani_bs = BeautifulSoup(ani_page.text, 'html.parser')

adjectives = adj_bs.string.splitlines()
animals = ani_bs.string.splitlines()


def append(list):
    for word in list:
        adjectives.append(word)
    
def capitalise(first_list, second_list):
    i = j = 0 
    for _word in first_list:
        first_list[i] = first_list[i].capitalize()
        i += 1

    for _word in second_list:
        second_list[j] = second_list[j].capitalize()
        j += 1

def random_word():
    choice = random.randint(1, 2)
    word1 = random.choice(adjectives)
    word2 = random.choice(adjectives)
    animal = random.choice(animals)
    
    if (choice == 1):
        return f"{word1} {word2} {animal}"
    else:
        return f"{word1} {animal}"


def loop(n):
    list = []
    num = 0
    while num < int(n):
        word = random_word()
        while (word in list):
            word = random_word()
        list.append(word)
        num += 1
    
    for idx, word in enumerate(list, 1):
        print(f"{idx}: {word}")


def save_word(word):
    print(word)

def usr_input():
    num = input("Enter the number of words you want: ")
    loop(num)

def cust_animal():
    animal = input("Enter an animal you would like to use: ")

    for word in animals:
        if animal.lower == word:
            return word

if __name__ == '__main__':
    # capitalise(adj_list, ani_list)
    usr_input()

