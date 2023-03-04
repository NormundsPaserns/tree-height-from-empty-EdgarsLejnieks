#python 3

"""
asdfasfasfasfasf

    # prepare for the worst solution in the world
    global exit_iteration
    
    hashedlist = {}
    for iter, val in enumerate(splitlist):
        hashedlist.update({iter:val})
        if int(splitlist[iter]) < 0:
            exit_iteration = iter
            print(exit_iteration)

    iterations = list(hashedlist.keys())
    values = list(hashedlist.values())

    tgt = values.index(exit_iteration)
    tgt_iter = iterations[tgt]
    print(tgt_iter)
    #for iter, val in enumerate(hashedlist):
    #    poslist = val_list.index()

"""

import sys
import threading
import numpy

def recursive_find(splitlist, index, counter):
    counter += 1
    if splitlist[index] == -1: 
        return counter
    return recursive_find(splitlist, splitlist[index], counter)

def compute_height(n, parents):
    print("Debug: running compute_height")
    splitlist = [int(x) for x in parents.split(" ")]
    counters = [0] * len(splitlist)
    for i, j in enumerate(splitlist):
        if splitlist[i] == -1: continue
        counters[i] = recursive_find(splitlist, splitlist[i], counters[i])
    print(max(counters)+1)


def main():
    # implement input form keyboard and from files
    # print("I for text input, F for file input")
    # print("select input type: ")
    #inputtype = input()
    #if "I" in inputtype:
    try:
        # print("Input node count: ")
        nodecount = input()
        # print("Input node values: ")
        parents = input()

        #for n in range(nodecount):
        #    parents = parents + input() + " "

        # print("Parents var: " + parents)
        compute_height(nodecount, parents)
    except EOFError as e:
        print(e)
        
    """
    elif "F" in inputtype:
        try:
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
            file.close()
        except EOFError as e:
            print(e) 

        #text = file.read()
        #todo: function
    """
    
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