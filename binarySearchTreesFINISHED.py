"""
This program manipulates binary search trees.
Program by: Roberto A. Ruiz de la Cruz
2017-04-09
"""

# A BST node is a dict with three elements:
# 1. data: the value in the node
# 2. left: a reference to the left subtree
# 3. right: a reference to the right subtree

# Prints an indented display of the tree -- useful for debugging.
# The output will look kind of like a sideways version of a drawing
# of the tree.
def display(tree, indent=0):

    if tree == None: # empty
        pass

    else:
        # right tree first (so it's on the right when you tilt your
        # head to the left to look at the display)
        display(tree['right'],indent+1)
        print("    " * indent + str(tree['data']))
        # now the left tree
        display(tree['left'],indent+1)

        

# adds a value to a BST and returns a pointer to the modified BST
def add(tree, value):
    #the base case. If there are no more values to compare then just add a new node

    if tree == None:
        return {'data':value, 'left':None, 'right':None}
    #If there is no length then don't add it    

    elif len(value) <= 0:
        return tree
    #Compare whether the new value needs to go to the left or the right of that node.

    elif value[0] < tree['data'][0]:
        tree['left'] = add(tree['left'],value)
        return tree

    elif value[0] > tree['data'][0]:
        tree['right'] = add(tree['right'],value)
        return tree

    else: # value == tree['data']
        return tree # ignore duplicate
        
#take in a BST and return values from lowest to highest
def printValues(tree):
    if tree == None:
        return None
    #this recursion moves all the way to the smallest values, once none is returned it will print itself and check the left.

    printValues(tree['left'])
    print(tree['data'])
    #the same thing happens where it moves all the way to the smallest value on the right nodes to make sure the smallest values are accounted for.
    printValues(tree['right'])

    
#take in a BST and change the values of the nodes without a left or right node.
def changeLeaves(tree):
    #if the node is empty, finish the recursion 

    if tree == None:
        return
    #if the node to the left and the node to the right of the current node are empty, then change that node into Leif

    elif tree['left'] == None and tree['right'] == None:
        tree['data'] = "Leif"

    else:
    #since we're not returning anything and just manipulating values, do the leif thing to the left and right
        return changeLeaves(tree['left']),changeLeaves(tree['right'])

#input is a BST and the output is an integer that's counted up everything it finds whose data is has a w
def countNode(tree):
    #Base Case: if the node is empty don't add anymore
    if tree == None:
        return 0
    
    #if the node has less than 1 value then don't even count it.
    elif len(tree['data']) <= 1:
        return countNode(tree['left']) + countNode(tree['right'])
    #if the tree's data, on the string area and first letter. . .is it a w? if so, return a 1 plus whatever other 1's and 0's for every recursion that fulfills the if statement

    elif tree['data'][1][0] == "w" or tree['data'][1][0] == "W":
        return 1 + countNode(tree['left']) + countNode(tree['right'])
    
    else:
        return countNode(tree['left']) + countNode(tree['right'])

#input is a BST and the output is the printed nodes from highest to lowest
def printReverse(tree):
    if tree == None:
        return None
    
    #same idea as printValues
    
    printReverse(tree['right'])
    print(tree['data'])
    printReverse(tree['left'])

def main():
    
    myTree = None  #create an empty tree
    #Create a tree with the nodes [20, 2, 25, 14, 1, 23, 75, 93, 74]
    #Note that the add function always returns the root of the BST!
    myTree = add(myTree, [20, 'Carol'])
    myTree = add(myTree, [2, 'Beep Boop'])
    myTree = add(myTree, [25, 'Wendy'])
    myTree = add(myTree, [14, 'Bert'])
    myTree = add(myTree, [1, 'Winnipeg'])
    myTree = add(myTree, [23, "Blackwater"])
    myTree = add(myTree, [75, "Tarantula"])
    myTree = add(myTree, [93, "Baskets"])
    #See that not having a name doesn't break the program.
    myTree = add(myTree, [5])
    #See that -'s also work
    myTree = add(myTree, [-9])
    #See that an empty node doesn't break the program
    myTree = add(myTree, [])
    #See how print reverse works
    printReverse(myTree)
    #See how print values works as opposed to printReverse
    printValues(myTree)
    #See what countNode does. There are 3 nodes with a w that we added to myTree
    print(countNode(myTree), "are the number of nodes with a 'w'")
    #See how myTree looks like before changing them to leif
    display(myTree)
    changeLeaves(myTree)
    #See how myTree looks like after changing them to leif
    display(myTree)
    
main()
