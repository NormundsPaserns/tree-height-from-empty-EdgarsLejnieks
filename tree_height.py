# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # print("Debug: running compute_height")
    # Write this function

    # firstly, i turn the string into an array
    splitar = parents.split(" ")
    # sort it
    splitar.sort()
    # put the first element in a var
    prevnum = splitar[0]
    # i make a variable for counting higher elements
    count = 0
    # then i iterate through the sorted array
    for x, y in enumerate(splitar):
        # i have a variable referencing current element
        curnum = splitar[x]
        # i check if it is larger than the previous
        if curnum > prevnum:
            # if yes, then add one to a counter
            count += 1
        # then assign current as previous
        prevnum = curnum
    # once loop is done, print the count
    print(count)
    #voila

    max_height = 0
    # Your code here
    return max_height


def main():
    # implement input form keyboard and from files
    # print("I for text input, F for file input")
    # print("select input type: ")
    inputtype = input()
    if inputtype == "I":
        # print("Input node count: ")
        nodecount = int(input())
        # print("Input node values: ")
        parents = input()

        #for n in range(nodecount):
        #    parents = parents + input() + " "

        # print("Parents var: " + parents)
        compute_height(nodecount, parents)
        

    elif inputtype == "F":
        # print("Input file path ")
        filepath = input()
        file = open(filepath, "r")
        lines = file.readlines()
        lncount = 0
        for line in lines:
            lncount += 1
            if lncount == 1:
                nodecount = int(line)
            if lncount == 2:
                parents = line
        compute_height(nodecount, parents)
            

        #text = file.read()
        #todo: function
    
    # todo:
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # todo:
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))