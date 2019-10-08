import math

def mergesort(gee):

    #using math.ceil returns the highest integer value
    mid = math.ceil(len(gee)/2)

    L=gee[:mid]
    R=gee[mid:]

    print("Left",L)
    print("Right",R)
    print()

    if len(L) > 1 or len(R) > 1:
        mergesort(L)

        print('*' * 30)
        print("Continue Splitting the Previous Right")

        mergesort(R)


    # initialises three variables as o
    i = j = k = 0


    # While Loops to do the Value Swapping
    # First While Loops Swaps the lower value into the place of the larger value
    while i < len(L) and j < len(R):

        if L[i] < R[j]:
            gee[k] = L[i]
            i += 1
        else:
            gee[k] = R[j]
            j += 1
        k += 1


    # Second and Third While Loop Places the larger value in the alternate position
    while i < len(L):
        gee[k] = L[i]
        i += 1
        k += 1

        print("List being Rebuilt in correct order - Left was greater than Right")
        print(gee)

    while j < len(R):
        gee[k] = R[j]
        j += 1
        k += 1

        print("List being Rebuilt in correct order - Left was smaller than Right")
        print(gee)


gee = [38,27,43,3,9,82,10]

print(gee)
mergesort(gee)
#print(gee)
