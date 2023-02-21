
def Nsum(n):
    if n <= 1:
        return n
    else:
        return n + Nsum(n-1)
n = int(input("Enter a number: "))
add=Nsum
print("The sum is",+add)