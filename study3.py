"""Задайте список из n чисел последовательности Sn = (Sn-1 + 3) и выведите на экран их сумму."""

def multNumberDir():
    fact = {1:4}
    n = int(input("Впишите число: "))
    for i in range(2, n+1):
        fact[i] = fact[i-1] + 3
    print(fact)
        
        

if __name__ == "__main__":
    multNumberDir()