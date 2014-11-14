import sys

def validrange(l):
    if not 1 <= l <= 100 :sys.exit(0)

def main():
    dat1 = raw_input().strip()

    dat1 = dat1.split(" ")
    if len(dat1) != 2: sys.exit(0)

    validrange(int(dat1[0]))
    validrange(int(dat1[1]))

    sumsq = 0
    for i in xrange(int(dat1[0]), int(dat1[1])+1):
        sumsq += i ** 2
    print sumsq

if __name__ == "__main__":
    main()
