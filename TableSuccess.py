import math
import argparse 

parser = argparse.ArgumentParser(description='Dark Eye Success')

parser.add_argument('s1', action="store", type=int)
parser.add_argument('s2', action="store", type=int)
parser.add_argument('s3', action="store", type=int)
parser.add_argument('pool', action="store",  type=int)

try:
    args = parser.parse_args()
    s1, s2, s3 = args.s1, args.s2, args.s3
    pool = args.pool
except:
    print("Please enter s1 s2 s3 pool")


pmf, cdf = [], []

def main():
    print('With Funtion')
    for i in range(pool + 1):
        p_str = "i = " + str(i)
        p_str += ", p(" + str(i) + ") = " + str(p(i))
        p_str += ", F(" + str(i) + ") = " + str(F(i))
        print p_str
        
    print('\nBrute Force:')

    for i in range(pool + 1):
        p_str = "i = " + str(i)
        p_str += ", p(" + str(i) + ") = " + str(pmf[i])
        p_str += ", F(" + str(i) + ") = " + str(cdf[i])
        print p_str

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r) #definition

def p(x):
    if(x == 0):
        return s1 * s2 * s3 / 8000.0   

    prob = s3*s2 + s3*s1 + s1*s2
    prob += (x - 1) * (s1 + s2 + s3)
    prob += nCr(x + 2, 2) - 3*x
    return prob / 8000.0

def F(x):
    prob = 0
    for i in range(x + 1):
        prob += p(i)
    return prob


def bruteForce():
    #init arrays
    for i in range(pool + 1):
        pmf.append(0)
        cdf.append(0)

    for r1 in range (1, 21):
        for r2 in range (1, 21):
            for r3 in range (1, 21):
                used1 = max(0, r1 - s1)
                used2 = max(0, r2 - s2)
                used3 = max(0, r3 - s3)

                totalUsed = used1 + used2 + used3
                if (totalUsed <= pool):
                    pmf[used1 + used2 + used3] += 1
    formalize()

def formalize():
    pmf[0] /= 8000.0 # //normalize
    cdf[0] = pmf[0] # //by definition
    for i in range(1, pool + 1):
        pmf[i] /= 8000.0
        cdf[i] = pmf[i] + cdf[i - 1] # //remember we're discrete

bruteForce()
main()
