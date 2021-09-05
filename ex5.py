# prime nos

def isprime(n):
    if n<=1:
        return False
    for x in range(2,n):
        if(n%x == 0):
            return False
    else:
        return True

for y in range(0,50,3):
    if isprime(y):
        print('{} prime'.format(y))
    else:
        print('{} not prime'.format(y))