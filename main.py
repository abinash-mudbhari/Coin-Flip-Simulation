# Coin Flip Simulation
# write some code that simulates flipping a single coin however many times the user decides. 
# The code should record the outcomes and count the number of tails and heads.
import random


# flip the nos and count the heads and tails
def main():
	num = int(input("enter the no of flips:"))
	
	heads = 0
	tails = 0
	head_list = []
	tail_list = []
	for i in range(num):
		flip = random.randint(0,1)
		if flip == 0:
			print("you got head")
			heads += 1
		else:
			print("you got tail")
			tails += 1
	print("HEADS:",heads)
	print("TAILS:",tails)

# ask user input how many numbers of flip
main()