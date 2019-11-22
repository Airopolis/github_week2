# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,100):

       fib = fibs[0]+fibs[1]
       fibs[0] = fibs[0] +1
       fibs[1] = fibs[1] +1

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
