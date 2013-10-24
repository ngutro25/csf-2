n = 6
series = 'fibonacci'
a,b = 1,1

def fibonacci(n):
    a,b = 1,1
    for i in range (n-2): # Starting 0 + 1 = 1, 1 + 1 = 2...
        a,b = b, a+b
    return a

def sum(n):
    i = 0
    answer = 0
    for i in range(n+1):
        answer += i
    return answer

if series == 'fibonacci':
    print fibonacci(n)            
elif series == 'sum':
    print sum(n)
else:
    print 'Invalid String'