#!/usr/bin/python

import argparse

def find_max_profit(prices):
	curr_min = prices[0]
	curr_max = prices[1]
	curr_max_index = 0

	for index, price in enumerate(prices):
		if price > curr_max and index > 0:
			curr_max = price	
			curr_max_index = index

	print(curr_min, curr_max)
	for index, price in enumerate(prices):
		if price < curr_min and index < curr_max_index:
			curr_min = price
	
	return curr_max - curr_min




prices_list = [1050, 270, 1540, 3800, 2]

print(find_max_profit(prices_list))






if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
