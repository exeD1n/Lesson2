"""Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр."""


def summNumber():
    n = int(input("Впишите ваше число: "))
    
    suma = 0
    
    while n > 0:
        digit = n % 10
        suma = suma + digit
        n = n // 10
    
    print("Сумма:", suma)
    
if __name__ == "__main__":
    summNumber()