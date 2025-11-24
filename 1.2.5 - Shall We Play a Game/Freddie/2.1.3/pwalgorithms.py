# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def two_words(password):
  words = get_dictionary()
  guesses = 0
  for w1 in words:
    for w2 in words:
      guesses = guesses + 1
      phrase = w1 + w2
      if phrase == password:
        return True, guesses
  return False, guesses

def two_words_and_digit(password):
  words = get_dictionary()
  guesses = 0
  diget = [1,2,3,4,5,6,7,8,9]
  for w1 in words:
    for w2 in words:
      guesses = guesses + 1
      for num in diget:
        phrase = w1 + w2 + str(num)
        if phrase == password:
          return True, guesses
  return False, guesses