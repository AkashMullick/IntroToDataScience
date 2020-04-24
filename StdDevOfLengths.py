import statistics

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """

    if L == []:
        return float("NaN")
    else:
        # lengths = []
        # for string in L:
        #     lengths.append(len(string))
        lengths = [len(string) for string in L]  # create a list of string lengths using list comprehension
        return statistics.pstdev(lengths)

arr1 = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(arr1))
