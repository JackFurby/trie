"""STAR."""
import time
from trie import Trie, Node, setup, save_trie, load_trie
import sys

#trie = Trie()
#setup(trie)
#save_trie(trie, 'example')
trie = load_trie('example')  # Word list

while True:
	"""Text interface for user"""
	print()
	action = input("What do you want to do? Enter 'help' for more: ")

	if action == "\q":
		sys.exit()
	elif action == "contains":
		inputLetters = input("Enter a word to check: ")

		# Makes sure input is in lower case
		inputLetters = inputLetters.lower()

		if trie.hasWord(inputLetters):
			print("Yes")
		else:
			print("No")
	elif action == "findWords":
		inputLetters = input("Enter letters ('?' is a wildcard): ").lower()
		start = time.time()
		wordList = trie.wordSearch(list(inputLetters))
		for i in wordList:
			print(i[0])
		end = time.time()
		print("Completed search in", end - start, 'seconds')
	elif action == "findWordsPrefix":
		prefixLetters = input("Enter prefix (in order): ").lower()
		inputLetters = input("Enter letters ('?' is a wildcard): ").lower()
		start = time.time()
		wordList = trie.prefix(list(inputLetters), prefixLetters)
		for i in wordList:
			print(i[0])
		end = time.time()
		print("Completed search in", end - start, 'seconds')
	elif action == "findWordsSuffix":
		suffixLetters = input("Enter suffix (in order): ").lower()
		inputLetters = input("Enter letters ('?' is a wildcard): ").lower()
		start = time.time()
		wordList = trie.wordSearch(list(inputLetters), suffix=suffixLetters)
		for i in wordList:
			print(i[0])
		end = time.time()
		print("Completed search in", end - start, 'seconds')
	elif action == "findWordsContains":
		suffixLetters = input("Enter string words must contain (in order): ").lower()
		inputLetters = input("Enter letters ('?' is a wildcard): ").lower()
		start = time.time()
		wordList = trie.contains(list(inputLetters), suffixLetters)
		for i in wordList:
			print(i[0])
		end = time.time()
		print("Completed search in", end - start, 'seconds')

	elif action == "help":
		print("")
		print("=== Trie help ===")
		print("")
		print("\q			-	Exit Trie")
		print("contains		-	Enter a single word to find out if it is accepted or not")
		print("findWords		-	Find all words you can make with a given set of characters")
		print("findWordsPrefix		-	Find all words you can make with a given set of characters + a prefix")
		print("findWordsSuffix		-	Find all words you can make with a given set of characters + a suffix")
		print("findWordsContains	-	Find all words you can make with a given set of characters + a set string")
		print("")
	else:
		print("Input not recognised")
