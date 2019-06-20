# Problem 1. -> Cyclic	Rotation:
# Shift	the	elements of	Multi Value Container A	to the right with R	shifts

A = [3,8,9,7,6]
B = 3
for i in range(B):
    C = A.pop()
    A.insert(0,C)
print("Its the answer after doing",B,"right shift: ",A)
print()
print("********************************")
"""
R = 3
list_1 = [3, 8, 9, 7, 6]
list_1 = (list_1[-n:] + list_1[:-n])
print(list_1)

print(list_1)
print("********************************")
def rotate(A, n):
   x = A[n - 1]
   for i in range(n - 1, 0, -1):
      A[i] = A[i - 1];
   A[0] = x;
# Driver function
A=list()
n=int(input("Enter the size of the List :"))
print("Enter the Element of  List :")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
print ("The array is ->")
for i in range(0, n):
   print (A[i], end = ' ')
rotate(A, n)
print ("\nRotated array is")
for i in range(0, n):
   print (A[i], end = ' ')
"""
# Problem 2. ->
N = int(input())
M = int(input())
a = []
for i in range(0,N):
    a.append(1)
i = 0
while i < N:
    if a[i] == 0:
        break
    a[i] = 0
    i = (i+M) % N
print(a)
print(a.count(0))