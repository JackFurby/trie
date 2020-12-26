import trie

# Create new trie

trie = trie.Trie()

# Populate from list

exampleWords = ['example', 'tree', 'dog', 'cat', 'toffee', 'tea', 'coffee']
trie.addWords(exampleWords)

# Add single word

trie.addWord('hello')

# Check if the trie has a word

inputLetters = input("Enter a word to check: ")
# Makes sure input is in lower case
inputLetters = inputLetters.lower()

if trie.hasWord(inputLetters):
	print("Yes")
else:
	print("No")

# Check the trie for all words containing a list of letters

inputLetters = input("Enter letters ('?' is a wildcard): ").lower()
wordList = trie.wordSearch(list(inputLetters))
for i in wordList:
	print(i[0])

# Check the trie for all words containing a list of letters and a Prefix

prefixLetters = input("Enter prefix (in order): ").lower()
inputLetters = input("Enter letters ('?' is a wildcard): ").lower()
wordList = trie.prefix(list(inputLetters), prefixLetters)
for i in wordList:
	print(i[0])

# Check the trie for all words containing a list of letters and a suffix

suffixLetters = input("Enter suffix (in order): ").lower()
inputLetters = input("Enter letters ('?' is a wildcard): ").lower()
wordList = trie.wordSearch(list(inputLetters), suffix=suffixLetters)
for i in wordList:
	print(i[0])

# Check the trie for all words containing a list of letters and a set string

suffixLetters = input("Enter string words must contain (in order): ").lower()
inputLetters = input("Enter letters ('?' is a wildcard): ").lower()
wordList = trie.contains(list(inputLetters), suffixLetters)
for i in wordList:
	print(i[0])
