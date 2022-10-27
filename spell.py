//pip install pyspellchecker
//Now below is how you can use this module to correct any misspelt word using Python:

from spellchecker import SpellChecker
corrector = SpellChecker()
word = input("Enter a Word : ")
if word in corrector:
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct Spelling is ", correct_word)
