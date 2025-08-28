def find_short(s):
    words = s.split()
    short_words = min(words, key=len)
    return len(short_words)

# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python