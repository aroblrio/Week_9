
i = 2

Fibonacci= []
Fibonacci.append(0)
Fibonacci.append(1)
print("0. ",Fibonacci[0])
print("1. ",Fibonacci[1])

while i <= 100:
    Fibonacci.append(Fibonacci[i-1] + Fibonacci[i-2])
    print(i,".",Fibonacci [i])
    i = i+1
