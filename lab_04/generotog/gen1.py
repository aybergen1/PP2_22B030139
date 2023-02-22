def square_generator(N):
    for i in range(1, N+1):
        yield i**2


def evennumbers(N):
    for i in range(1,N+1):
        if (i%2==0):
            yield i


def twelve(N):
    for i in range(1, N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def square(n,m):
    for i in range(n,m+1):
        yield i**2

def sqe(n):
   while n>=0:
        yield n
        n-=1
