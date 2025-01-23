#Assignment 3: Traversing through below list of digits, filter out the numbers which are divisible by 5.



a = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

n = len(a)
print("length of the list-",n)

for i in range (n):
    if a[i]%5 == 0:
        print("Multiples of 5 are-",a[i])
    