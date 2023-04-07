# 5-1 실습
import random

def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))
             

	return card_list

p1 = random.choice(making_card_list())
p2 = random.choice(making_card_list())

for i in range(6):






trump_card_list = making_card_list()