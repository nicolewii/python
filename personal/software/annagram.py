#string off all possible punctuation
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#annagram definition that checks if the words are annagrams of each other
def check_annagram(word1, word2):
    result = sorted(word1.lower()) == sorted(word2.lower())
    return result

#takes in two words 
word1 = input("Please enter the first word: ")
word2 = input("Please enter the second word: ")
#remove any punctuation from the word
for x in word1:
    if x in punc:
        word1 = word1.replace(x, "")
for y in word2:
    if y in punc:
        word2 = word2.replace(y, "")
#remove any whitespaces
word1.strip()
word2.strip()

#prints true or false if it's an annagram (reguardless of spacing and punctuation)
print(check_annagram(word1, word2))
