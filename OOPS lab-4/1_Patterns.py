# #pattern 1

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

#pattern 2
n=5
for i in range(1,n+1):
    print(" "*(i-1), end=" ")
    for j in range(n-i+1):
        print(i, end=" ")
    print()

#pattern 3
n=5
for i in range(n,0,-1):
    print(" "*(i-1), end=" ")
    for j in range(1,n-i+2):
        print(j, end=" ")
    print()

#pattern 4
n=5
for i in range(n,0,-1):
    print(" "*(i-1), end=" ")
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print(i, end=" ")
    print()

#pattern 5
n=5
for i in range(1,n+1):
    print(" "*(i-1), end=" ")
    for j in range(n-i+1):
        print(5, end=" ")
    print()

# pattern 6
n=5
for i in range(n,0,-1):
    print(" "*(i-1), end=" ")
    for j in range(n-i+1,0,-1):
        print(j, end=" ")
    print()

#pattern 7
n=5
for i in range(n+1,1,-1):
    for j in range(i):
        print(j, end=" ")
    print()

# #pattern 8
n=3
current_number=1
for i in range(1,n+1):
    for j in range(1,2*i):
        print(current_number, end=" ")
        current_number+=1
    print()

# pattern 9
n=4
current=1
for i in range (1,n+1):
    row_length=i
    start= current+ row_length-1
    for j  in range(start, current-1, -1):
        print(j,end=" ")
    current+=row_length
    print() 

#pattern 10
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    for j in range(i-1,0,-1):
        print(j, end=" ")
    print()
    
#pattern 11
n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    for j in range(1,i+1):
        print(j, end=" ")
    print()

# pattern 12
n=5
even=10
for i in range(1,n+1):
    for j in range(i):
        print(even-(j*2), end=" ")
    print()

#pattern 13
# n=7
for i in range(n):
    for j in range(i+1):
        print(i*j, end=" ")
    print()

#pattern 14
# n=5
for i in range(n):
    current=2*i+1
    for j in range(i+1):
        print(current, end=" ")
    print()

#pattern 15
# n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        print(j, end=" ")
    print()

# pattern 16
n=7
for i in range(n,0,-1):
    print(" "*(i-1), end=" ")
    for j in range(n-i+1):
        print("*", end=" ")
    print()
    
#pattern 17
n=7
for i in range(1,n+1):
    print(" "*(i-1), end=" ")
    for j in range(n-i+1):
        print("*", end=" ")
    print()

#pattern 18
n=5
for i in range(1,n+1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()
