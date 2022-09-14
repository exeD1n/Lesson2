"""Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."""

def multNumberDir():
    factorial = []
    n = int(input("Впишите число: "))
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
        factorial.append(fact)
    print(factorial)
    
if __name__ == "__main__":
    multNumberDir()