
#1
S = input()
print(S[2])
print(S[-2])
print(S[:5])
print(S[:-2])
print(S[::2])
print(S[1::2])
print(S[::-1])
print(S[::-2])
print(len(S))

#2
W = input()
print(W.count(" ") + 1)

#3
W = input()
c = len(W)//2
print(W[c:]+W[:c])


#1  минимум издвух чисел
a = int(input("1st"))
b = int(input("2nd "))
if a>b:
    print(b)
else:
    print(a)

#2  Знак числа
x = int(input(""))
if x>0:
    print("sign(x)=1")
elif x<0:
    print("sign(x)=-1")
else:
    print("sign(x)=0")


#3  Шахматная доска
x1 = int(input(""))
y1 = int(input(""))
x2 = int(input(""))
y2 = int(input(""))
if 1<=x1<8 and 1<=y1<8 and 1<=x2<8 and 1<=y2<8
    if (x1+y1)%2==0 and (x2+y2)%2==0:
    print("yes")
else:
    print("no")

#4Високосный год
Year = int(input())
if Year%4==0 and Year%100!=0 or Year%400==0:
    print("Yes")
else:
    print("No")


#5  сколько совпадает чисел
x1 = int(input())
x2 = int(input())
x3 = int(input())
if x1==x2==x3:
    print("3")
elif x1==x2 or x2==x3 or x1==x3:
    print("2")
else:
    print(0)


#6 ход ладьи
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")

#7 шоколадка

n, m, k = map(int, input().split())

if k % n == 0 or k % m == 0:
    print("YES")
else:
    print("NO")