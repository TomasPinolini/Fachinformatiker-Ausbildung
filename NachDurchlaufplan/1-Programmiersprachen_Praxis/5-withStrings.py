#5.1 Repeat a Word.
word = input("Enter a word: ")
times = int(input("How many times should it repeat? "))
print(word * times)

#5.2 Word length.
word = input("Enter a word: ")
print("The word", word, "has", len(word), "letters.")

#5.3 Uppercase and lowercase conversion.
color = input("What is your favorite color? ")
print("Uppercase:", color.upper())
print("Lowercase:", color.lower())

#5.4 Reverse a string.
word = input("Enter a word: ")
reversed_word = word[::-1]
print("The reverse of", word, "is", reversed_word)

#5.5 Favorite things.
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
food = input("What is your favorite food? ")
print("Your favorite color is", color + ", your favorite animal is", animal + ", and your favorite food is", food + ".")
