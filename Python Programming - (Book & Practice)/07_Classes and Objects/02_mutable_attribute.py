class Number():
    evens = []
    odds = []
    def __init__(self,num):
        self.num = num
        if num%2 == 0:
            Number.evens.append(num)
        else:
            Number.odds.append(num)

N1 = Number(19)
N2 = Number(20)
N3 = Number(22)
N4 = Number(23)
N5 = Number(25)

print("Even numbers are: ",Number.evens)
print("Odd numbers are: ",Number.odds)