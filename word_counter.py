import sys
import re
print("Enter your text (press Enter, then Ctrl+D or Ctrl+Z to finish):")

user_string = sys.stdin.read()

# word to count
word = input("Enter the word to count: ")

# ignore case and normalize whitespace

normalized_text = re.sub(r'\s+', ' ', user_string).lower()

words_list = normalized_text.split()

count = words_list.count(word.lower())
print(f"The word '{word}' occurs {count} times.")
