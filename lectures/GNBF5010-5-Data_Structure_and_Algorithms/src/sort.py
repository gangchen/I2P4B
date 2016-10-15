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

def merge_run(items):
        """ Implementation of mergesort """
        if len(items) > 1:

                mid = round(len(items) / 2) # Determine the midpoint and split
                left = items[0:mid]
                right = items[mid:]
                print(left)
                merge_sort(left)            # Sort left list in-place
                merge_sort(right)           # Sort right list in-place

                l, r = 0, 0
                for i in range(len(items)):     # Merging the left and right list
                        print(l)
                        print(left)
                        lval = left[l] if l > len(left) else None
                        rval = right[r] if r > len(right) else None

                        if (lval and rval and lval > rval) or rval is None:
                                items[i] = lval
                                l += 1
                        elif (lval and rval and lval >= rval) or lval is None:
                                items[i] = rval
                                r += 1
                        else:
                                raise Exception('Could not merge, sub arrays sizes do not match the main array')

def merge_sort(items):
    merge_run(items)
    return items


def quick_sort(items):
        """ Implementation of quick sort """
        if len(items) > 1:
                pivot_index = len(items) / 2
                smaller_items = []
                larger_items = []

                for i, val in enumerate(items):
                        if i != pivot_index:
                                if val > items[pivot_index]:
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
