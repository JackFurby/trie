# Trie

This repo contains a trie data structure that was initially implemented in my repo for [STAR](https://github.com/JackFurby/STAR) and thus does not have git history for that. If you wish to view it please visit STAR.

## Definition

A trie is a data structure used to store a dynamic set or associative array where the keys are usually strings. Each node will have a key who's value will be based on its position. This will be such that nodes before node X will be the prefix and nodes after will become the suffix. The root node is the empty string In this project a trie data structure will be used to store accepted words in a format that is efficient to search.

### node

A trie is made up of nodes linked together. Each node is made up of a **value**, **indicator** and **pointers**. In my implementation the value is called data, indicator is called end and pointers are children.
* The indicator is used to mark the current node as the end of a word.
* The value stores the current word. This is not required but will save time if you want to return the word found.
* the pointers can be seperated out but in my implementation I have used a dictionary as it means I can store as many unique keys as I like and will not be taking up any extra storage for unused pointers.

```Python
class Node:
	def __init__(self, end=False, data=None):
		"""Initilise the node."""
		self.end = end
		self.data = data
		self.children = dict()
```

A word is represented by leaf nodes and by some inner nodes that are marked as accepted words.

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Trie_example.svg/400px-Trie_example.svg.png)

(Image of trie data structure was taken from https://en.wikipedia.org/wiki/Trie)

## Words

Word list file can be found here: https://www.wordgamedictionary.com/sowpods/. This is a SOWPODS Scrabble word list.

## Adding words to trie

When adding to the trie the start point is the trie head. From here the trie is traversed until either a node is not present in the current node children or the current character being checked is the last letter in the word being added. If the node is not present then a new node is added. If the current character being checked is the last letter in the word being added then the node is edited to say it is then end of a word.

```Python

def addWord(self, word):
	"""Add a word to the trie."""
	currentNode = self.head

	for i in range(len(word)):
		# if letter already exists in children move to the node
		if word[i] in currentNode.children:
			currentNode = currentNode.children[word[i]]
			# if letter is then end of word being added update node to show this
			if i == len(word) - 1:
				currentNode.end = True
				currentNode.data = [word]
		# if letter is not in children add it
		else:
			if i < len(word) - 1:
				currentNode.children[word[i]] = Node(False)
			else:
				currentNode.children[word[i]] = Node(True, [word])
			currentNode = currentNode.children[word[i]]

```

## Finding all words from a list

wordSearch will recursively call itself and on each call will check to see if the current node is the end of a word. To make sure the same path is not searched twice a list of current letters searched is kept. If a letter is already present in this then that letter is skipped. The method here is not perfect and if you enter a wild card then you may get duplicates in your result

Given a list of characters wordSearch will return a list of all words that can be created with them.

This function ha been extended to accept a prefix, suffix or an extra string that must be included in the results.

```Python

def wordSearch(self, letters, suffix=None, contains=False, containsSet=False, currentNode=None):
	"""Given a list of letters find all words that can be made (with optional extra components)."""
	# list of all words found
	words = []

	if currentNode is None:
		currentNode = self.head

	# If suffix is set apply suffix to search
	if suffix is not None:
		suffixNode = currentNode
		suffixTrue = True
		for char in suffix:
			if char in suffixNode.children:
				suffixNode = suffixNode.children[char]
			else:
				# If suffix is not accepted then apply this
				suffixTrue = False
		# if word found and suffix accepted then add it to words
		if suffixNode.end and suffixTrue:
			# only add word to words list
			words.append([suffixNode.data[0]])
	# In contains has been set then make sure contains is true before seeing if word exists
	elif containsSet:
		if contains:
			if currentNode.end:
				# only add word to words list
				words.append([currentNode.data[0]])
	# Regualr word search
	else:
		# if word found then add it to words
		if currentNode.end:
			# only add word to words list
			words.append([currentNode.data[0]])

	if len(letters) is not 0:
		# i keeps track of current letter
		# searched stop duplicate searches if input has repeated letters
		i = 0
		searched = []
		for letter in letters:
			if letter not in searched:
				searched.append(letter)
				containsTrue = True
				# Apply contains to search
				if len(letter) > 1:
					containsNode = currentNode
					for char in letter:
						if char in containsNode.children:
							containsNode = containsNode.children[char]
						else:
							# If contains string is not accepted then apply this
							containsTrue = False
					if containsTrue:
						newLetters = letters.copy()
						del newLetters[i]
						words += self.wordSearch(newLetters, suffix=suffix, contains=containsTrue, containsSet=True, currentNode=containsNode)
				# if wildcard played then look at all children
				elif letter == '?':
					for char in currentNode.children:
						newLetters = letters.copy()
						del newLetters[i]
						# Suffix word search
						if suffix is not None:
							words += self.wordSearch(newLetters, suffix=suffix, currentNode=currentNode.children[char])
						# Regualr word search
						else:
							words += self.wordSearch(newLetters, contains=contains, containsSet=containsSet, currentNode=currentNode.children[char])
				elif letter in currentNode.children:
					newLetters = letters.copy()
					del newLetters[i]
					# Suffix word search
					if suffix is not None:
						words += self.wordSearch(newLetters, suffix=suffix, currentNode=currentNode.children[letter])
					# Regualr word search
					else:
						words += self.wordSearch(newLetters, contains=contains, containsSet=containsSet, currentNode=currentNode.children[letter])
			i += 1

	# return words found
	return words

```

## Usage


```

$ git clone https://github.com/JackFurby/trie.git
$ cd trie
$ python interface.py

```

On start you will either have to load in a saved trie or create a new one.

```
=== Trie help ===

\q			-	Exit Trie
saveTrie		-	Saves all words in the file words/example.txt to the trie and .pkl file
loadTrie		-	Loads a previously saved trie from words/example.pkl
contains		-	Enter a single word to find out if it is accepted or not
findWords		-	Find all words you can make with a given set of characters
findWordsPrefix		-	Find all words you can make with a given set of characters + a prefix
findWordsSuffix		-	Find all words you can make with a given set of characters + a suffix
findWordsContains	-	Find all words you can make with a given set of characters + a set string

```
