def factorial(n):
    if(n==0):
        return 1
    else:
        return (n * factorial(n-1))
    
def main():
    input = [0,2,4,6,8,10,12,14]
    for i in input:
        print("{0:d} : {1:d}".format(i,factorial(i)))

if __name__ == '__main__':
    main()
