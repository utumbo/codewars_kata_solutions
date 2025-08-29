def positive_sum(arr):
    res = []
    for i in arr:
        if i > 0:
            res.append(i)
    total = sum(res)
    return total

# https://www.codewars.com/kata/5715eaedb436cf5606000381/solutions/python?filter=me&sort=best_practice&invalids=false