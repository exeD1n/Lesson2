"""Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число."""

def multNumberDir():
    N = int(input("Введите число: "))
    num = []
    for i in range(-N, N+1):
        num.append(i)
        
        
    with open('file.txt','w', encoding='utf-8') as f:
        f.writelines([str(d) + '\n' for d in num])
        
        
        
if __name__ == "__main__":
    multNumberDir()