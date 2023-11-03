#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    result = 0
    for x in sys.argv:
        result += int(x)
        print("{}".format(result))
