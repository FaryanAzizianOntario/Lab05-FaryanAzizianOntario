# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("-i", "--ignore-case", action="store_true")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")


    args = parser.parse_args()

    wanted = args.pattern
    l = []
    
    selectedFile = open(args.filename)
    a = selectedFile.readlines()

    for fruit in a:
        fruit = fruit.rstrip("\n")

        if(args.ignore_case == True and wanted in fruit.lower()):
                    l.append(fruit)

        elif(wanted in fruit):
            l.append(fruit)
    
    for index, ans in enumerate(l, start=1):
        print(f"{index}:", ans)
    

if __name__ == "__main__":
    main()
