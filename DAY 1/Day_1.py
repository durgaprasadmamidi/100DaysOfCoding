wordList = ['cat', 'dog', 'rabbit']
print([word for word in ''.join(wordList)])  # getting all letters
print(list(dict.fromkeys([ch for word in wordList for ch in word])))  # removing duplicates


#########


class Fraction:

    def __init__(self, num, denm):
        self.num = num
        self.denm = denm

    def __str__(self):
        return str(self.num) + '/' + str(self.denm)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.denm + self.denm * otherfraction.num

        newden = self.denm * otherfraction.denm
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
    def __mul__(self, otherfraction):
        return Fraction(self.num * otherfraction.num, self.denm * otherfraction.denm)

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

f1 = Fraction(7, 9)
f2 = Fraction(7, 3)
print(f1 + f2)
print(f1 * f2)
