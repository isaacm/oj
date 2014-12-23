import sys

def validrange(l):
    for x in l:
        if not -100 <= x <= 100:
            sys.exit(0)

def main():
    len1 = raw_input()
    dat1 = raw_input()

    len2 = raw_input()
    dat2 = raw_input()

    if not len1 or not dat1 or not len2 or not dat2:
        sys.exit(0)

    len1 = int(len1, 10)
    if len1 < 2 or len1 > 100:
        sys.exit(0)
    len2 = int(len2, 10)
    if len2 < 2 or len2 > 100:
        sys.exit(0)

    dat1 = dat1.split(" ")
    if len(dat1) != len1:
        sys.exit(0)
    dat1 = [int(x, 10) for x in dat1]
    validrange(dat1)

    dat2 = dat2.split(" ")
    if len(dat2) != len2:
        sys.exit(0)
    dat2 = [int(x, 10) for x in dat2]
    validrange(dat2)

    avg1 = sum(dat1)/float(len1)
    avg2 = sum(dat2)/float(len2)

    o1 = ''
    if avg2 < avg1:
        for i in dat1: o1 = o1 + str(i) + " "
    else:
        for i in dat2: o1 = o1 + str(i) + " "
    print o1

if __name__ == "__main__":
    main()
