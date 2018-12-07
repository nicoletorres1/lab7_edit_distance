'''
Author: Nicole Torres
CS2302: Lab 7
Last Modified: 12/05/18
'''

debug = True


def get_upper_three(adjMat, row, col):
    top = adjMat[row-1][col]
    left = adjMat[row][col-1]
    top_left = adjMat[row-1][col-1]
    return min(top, left, top_left)


def edit_distance(s1, s2):
    if s1 == s2:
        return 0
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        len(s1)

    # At this point, none of the above conditions were true,
    # so, we know s1 and s2 are not equal and both
    # non-empty. it will require some unknown amount of
    # deletes, insertions, and replacements

    edits = []

    # initializing edits
    for i in range(len(s1)+1):
        row = [0] * (len(s2)+1)
        edits.append(row)

    # fill first row
    for i in range(len(edits[0])):
        edits[0][i] = i
    # fill first column
    for j in range(len(edits)):
        edits[j][0] = j

    for row in range(1,len(edits)):
        for col in range(1,len(edits[0])):

            if s1[row-1] == s2[col-1]:
                edits[row][col] = edits[row-1][col-1]
            else:
                edits[row][col] = get_upper_three(edits, row, col) + 1
            if debug: print(row, col)
            if debug:
                for thing in edits:
                    print(thing)
                print()

    return edits[-1][-1]


s1 = 'SMART'
s2 = 'STACK'

print(edit_distance(s1,s2))

