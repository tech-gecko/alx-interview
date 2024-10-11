#!/usr/bin/python3
"""This file contains a function that takes a parameter, boxes
(a list of lists). If n is the number of locked boxes, with each box being
numbered from 0 to n - 1, and each box may contain keys to the other boxes, the
function determines if all the boxes can be opened by returning 'True' if they
can be opened. Else, it returns 'False'. A key with the same number as a box
opens that box. You can assume all keys will be positive integers. There can be
keys that do not have boxes. The first box, 'boxes[0]' is unlocked."""


def canUnlockAll(boxes):
    n = len(boxes)  # Get the number of boxes
    boxSet = set(range(n))  # Set of all boxes (0 to n-1)
    openedBoxSet = set()  # Set to keep track of opened boxes
    newFoundKeySet = set()  # Set to store newly found keys

    # Start by opening the first box
    openedBoxSet.add(0)

    # Add keys from the first box to the newFoundKeySet
    newFoundKeySet.update(boxes[0])

    # Continue to open boxes while there are new keys found
    while newFoundKeySet:
        currentKeys = set()  # Temp set to track all keys in this iteration

        for key in newFoundKeySet:
            if key < n and key not in openedBoxSet:
                openedBoxSet.add(key)  # Mark the box as opened
                currentKeys.update(boxes[key])  # Add keys from new open box

        # Update newFoundKeySet with keys found in this iteration
        # Remove already opened boxes from the current keys
        newFoundKeySet = currentKeys - openedBoxSet

    # Return True if all boxes can be opened
    return openedBoxSet == boxSet
