geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]

# https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python