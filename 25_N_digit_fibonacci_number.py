# Enter your code here. Read input from STDIN. Print output to STDOUT
def new(N):
    a,b,ctr = 1,1,2
    while(len(str(a)) != N):
        a,b = a+b,a
        ctr += 1
    print ctr
T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    new(N)
