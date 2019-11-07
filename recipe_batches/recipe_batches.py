#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
	# loop over all recipe ingredients and check how many times they divide into
	# the ingredients available
	batches = 0	
	batch_dict = {}

	for ingredient in recipe:
		try: ingredients[ingredient]
		except KeyError: ingredients[ingredient] = None
		if ingredients[ingredient] == None:
			return 0
		
		if ingredients[ingredient] // recipe[ingredient] < 1:
			return 0	 
		batch_dict[ingredient] = ingredients[ingredient] // recipe[ingredient]
		
	values = list(batch_dict.values())
	lowest_batch_num = values[0]
	for batch_num in batch_dict:
		if batch_dict[batch_num] < lowest_batch_num:
			lowest_batch_num = batch_num

	return lowest_batch_num

	
	

if __name__ == '__main__':
	# Change the entries of these dictionaries to test 
	# your implementation with different inputs
	recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
	ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
	print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }

print(recipe_batches(recipe, ingredients))
