class Node:
	"""Node object for trie."""

	# children contains links to other nodes
	# data contains word if node is the end of a word
	# end indicates if the current node is the end of a word
	def __init__(self, end=False, data=None):
		"""Initilise the node."""
		self.end = end
		self.data = data
		self.children = dict()


class Trie:
	"""Trie data structure."""

	def __init__(self):
		"""Initilise the trie."""
		self.head = Node()

	def addWord(self, word):
		"""Add a word to the trie."""
		currentNode = self.head

		# make sure word is in lowercase
		word = word.lower()

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

	def addWords(self, wordList):
		"""Add a list of words to the trie"""
		for word in wordList:
			self.addWord(word)

	def hasWord(self, word):
		"""If the trie has the word being searched for return true."""
		if word == '' or word is None:
			return False

		currentNode = self.head
		for letter in word:
			if letter in currentNode.children:
				currentNode = currentNode.children[letter]
			else:
				return False

		# if final node marks the end of a word return true
		if currentNode.end is False:
			return False
		else:
			return True

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

		if len(letters) != 0:
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
							# Regular word search
							else:
								words += self.wordSearch(newLetters, contains=contains, containsSet=containsSet, currentNode=currentNode.children[char])
					elif letter in currentNode.children:
						newLetters = letters.copy()
						del newLetters[i]
						# Suffix word search
						if suffix is not None:
							words += self.wordSearch(newLetters, suffix=suffix, currentNode=currentNode.children[letter])
						# Regular word search
						else:
							words += self.wordSearch(newLetters, contains=contains, containsSet=containsSet, currentNode=currentNode.children[letter])
				i += 1

		# return words found
		return words

	def contains(self, letters, contains, currentNode=None):
		"""Given a list of letters find all words that can be made containing a string."""
		letters.append(contains)
		return self.wordSearch(letters, containsSet=True)

	def prefix(self, letters, prefix, currentNode=None):
		"""Given a list of letters find all words that can be made begining with a string."""
		if currentNode is None:
			currentNode = self.head

		# Apply prefix to search
		for char in prefix:
			currentNode = currentNode.children[char]

		# move over to regular wordSearch (with prefix in place)
		return self.wordSearch(letters, currentNode=currentNode)
