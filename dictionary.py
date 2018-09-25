import json

from difflib import get_close_matches

import json

from difflib import get_close_matches

# Loading json data
data = json.load(open("data.json"))

def meaning(word):
	w = word.lower()
	first_letter_capitalized = w.title()
	capitalized_word = w.upper()
	if w in data:
		return data[w]
	# Accounting for capitalized words 
	elif first_letter_capitalized in data:
		return data[first_letter_capitalized]
	elif capitalized_word in data:
		return data[capitalized_word]
	# Looking for close matches
	elif len(get_close_matches(w, data.keys(), cutoff = 0.8)) > 0:	
		question = input("Did you mean %s? Enter Y for Yes: " % get_close_matches(w, data.keys(), cutoff = 0.8)[0])
		if question == "Y":
			return data[get_close_matches(w, data.keys(), cutoff = 0.8)[0]]
		elif question == "N":
			return "That word doesn't exist"
		else:
			return "We didn't understand your response."
	else:
		return "That word doesn't exist."
    


# Getting input from user
word = input("Enter Word: ")

# Returning the definition or suggestions
output = (meaning(word))
if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)
