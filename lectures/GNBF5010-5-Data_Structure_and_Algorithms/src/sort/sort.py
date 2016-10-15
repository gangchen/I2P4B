import sys

def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-i):
                if items[j] > items[j+1]:
                        items[j], items[j+1] = items[j+1], items[j]     # Swap!

    return items


def insertion_sort(items):
    """ Implementation of insertion sort """
    for i in range(1, len(items)):
            j = i
            while j > 0 and items[j] < items[j-1]:
                    items[j], items[j-1] = items[j-1], items[j]
                    j -= 1
    return items

def merge_sort(items):
    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1

    return items


def quick_sort(items):
        """ Implementation of quick sort """
        if len(items) > 1:
                pivot_index = len(items) // 2
                smaller_items = []
                larger_items = []

                for i, val in enumerate(items):
                        if i != pivot_index:
                                if val < items[pivot_index]:
                                        smaller_items.append(val)
                                else:
                                        larger_items.append(val)

                quick_sort(smaller_items)
                quick_sort(larger_items)
                items[:] = smaller_items + [items[pivot_index]] + larger_items

        return items

def readitems(filename):
    l = [float(i) for i in open(filename).read().strip().split('\n')]
    return l

def run(alg, filename):
    l = readitems(filename)
    algs = {"bubble": bubble_sort,
            "insertion": insertion_sort,
            "merge": merge_sort,
            "quick": quick_sort,
    }
    print(algs[alg](l))

if __name__ == '__main__':
    alg = sys.argv[1]
    filename = sys.argv[2]
    run(alg, filename)
