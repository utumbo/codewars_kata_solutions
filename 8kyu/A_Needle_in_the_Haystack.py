def find_needle(haystack):
    for index, item in enumerate(haystack):
        if item == 'needle':
            return (f"found the needle at position {index}")

# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python