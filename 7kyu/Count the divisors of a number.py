def divisors(n):
    divisor = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisor.append(i)

    return len(divisor)

# https://www.codewars.com/kata/542c0f198e077084c0000c2e/solutions/python