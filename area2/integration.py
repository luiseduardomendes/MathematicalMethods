

def trapezium_integrate(x, y):
    s = 0
    n = len(x)
    for i in range(n-1):
        s += (x[i+1]-x[i])/2 * (y[i] + y[i+1])
    return s

def simpson_integrate(x, y):
    s = 0
    n = len(x)
    n1 = n-(n%2)

    for i in range(2,n,2):
        s += (x[i]-x[i-2])/6 * (y[i-2] + 4*y[i-1] + y[i])
    
    if (n%2 == 0):
        s += (x[n-1]-x[n-2])/2 * (y[n-2] + y[n-1])
    
    return s