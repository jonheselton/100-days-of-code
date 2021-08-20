import os
import sys
template = """##!/usr/bin/python


def main():


if __name__ == "__main__":
    main()
    
    """
os.mkdir(sys.argv[1])
fo = open(sys.argv[1] + '/scratch.py', 'w+')
fo.write(template)
fo.close()
