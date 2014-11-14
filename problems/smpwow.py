import sys

def validrange(l):
    if not 0 < l < 50 :sys.exit(0)

def main():
    dat1 = raw_input()

    dat1 = int(dat1,10)
    validrange(dat1)

    print 'W' + 'o'*dat1 + 'w'

if __name__ == "__main__":
    main()
