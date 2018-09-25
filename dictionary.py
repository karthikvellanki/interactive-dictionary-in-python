import json

from difflib import get_close_matches

# Loading json data
data = json.load(open("data.json"))

def meaning(word):
	w = word.lower()
	firstlettercapitalized = w.title()
	capitalizedword = w.upper()
	if w in data:
		return data[w]
	# Accounting for capitalized words 
	elif firstlettercapitalized in data:
		return data[firstlettercapitalized]
	elif capitalizedword in data:
		return data[capitalizedword]
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
