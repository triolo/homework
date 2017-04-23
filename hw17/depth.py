import os
def depth():
    max = 0
    maxroot = ""
    for root, dirs, files in os.walk("."):
        curr = root.count(r"/")
        if curr > max:
            max = curr
            maxroot = root
    print(max, maxroot)
depth()
