# Program takes 2 inputs (word1 & word2) and checks whether word1's letters can make word2 

word1 = input("Enter word to use: ")
word2 = input("Enter word to make: ")

def checkWord(word1, word2):
  return all(word2.count(i) <= word1.count(i) for i in word2)

if checkWord(word1, word2): 
  print("Can be made!")

else:
  print("Nope")
    
