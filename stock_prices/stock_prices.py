#!/usr/bin/python

import argparse

def find_max_profit(prices):
	curr_min = prices[0] # initialize curr min to first value in list
	curr_max = prices[1] # initialize curr max to second value in list 
	curr_max_index = 0 # initialize the index of the current max

	for index, price in enumerate(prices): # loop over list to find max value and it's index
		if price > curr_max and index > 0: # update max value and max index if price is
			curr_max = price	           # greater than curr max value and index is > 0
			curr_max_index = index

	for index, price in enumerate(prices): # loop over to find min value that comes before
		if price < curr_min and index < curr_max_index: # the curr_max_index
			curr_min = price
	
	return curr_max - curr_min

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
