# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
aMax = 0;bMax = 2;nMax = 0
N = int(raw_input())
if N%2 == 0:
    for a in range(-N,N+1,2):
        n = 0
        while(isprime(abs(n*n + a*n + 2))):
            n+=1
        if n > nMax:
            nMax = n;aMax = a
    for a in range(-N+1,N,2):
        for b in range(3,N,2):
            n = 0
            while(isprime(abs(n*n + a*n + b))):
                n+=1
            if n > nMax:
                aMax = a;nMax = n;bMax = b
elif N%2 == 1:
    for a in range(-N+1,N,2):
        n = 0
        while(isprime(abs(n*n + a*n + 2))):
            n+=1
        if n > nMax:
            nMax = n;aMax = a;bMax = 2
    for a in range(-N,N+1,2):
        for b in range(3,N+1,2):
            n = 0
            while(isprime(abs(n*n + a*n + b))):
                n+=1
            if n > nMax:
                aMax = a;bMax = b;nMax = n
print str(aMax) + " " + str(bMax)
