# if every integer must be unique then we can solve with sets
def get_additions_from_arrays_uniques(current, target):
    return list(set(target) - set(current))


def get_deletions_from_arrays_uniques(current, target):
    return list(set(current) - set(target))


# if uniques are not guaranteed
def get_additions_from_arrays(current, target):
    c = target[:]

    for i in current:
        if i in c:
            c.remove(i)

    return c


def get_deletions_from_arrays(current, target):
    c = current[:]

    for i in target:
        if i in c:
            c.remove(i)

    return c

def main():
    current = [1, 3, 5, 6, 8, 9]
    target = [1, 2, 5, 7, 9]
    
    print "unique additions: {0}".format(
        get_additions_from_arrays_uniques(current, target))
    print "unique deletions: {0}".format(
        get_deletions_from_arrays_uniques(current, target))
    print "additions: {0}".format(
        get_additions_from_arrays(current, target))
    print "deletions: {0}".format(
        get_deletions_from_arrays(current, target))

if __name__ == "__main__":
    main()
