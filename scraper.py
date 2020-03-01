import requests
from bs4 import BeautifulSoup

urls = ("http://assets.gfycat.com/adjectives", "http://assets.gfycat.com/animals")

def get_data():
	adj_page = requests.get(urls[0])
	ani_page = requests.get(urls[1])
	return adj_page, ani_page


def parse_data(first, second):
	adj_bs = BeautifulSoup(first.text, 'html.parser')
	ani_bs = BeautifulSoup(second.text, 'html.parser')
	adjectives = adj_bs.string.splitlines()
	animals = ani_bs.string.splitlines()
	return adjectives, animals

def main():
	adj_page, ani_page = get_data()
	adjectives, animals = parse_data(adj_page, ani_page)
	return adjectives, animals

adjectives, animals = main()
