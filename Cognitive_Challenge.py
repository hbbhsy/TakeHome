# Code Challenge For Congnitive.ai
# Agnes He
# agneshesf@gmail.com
# July 26, 2020


# Question 1: Implement a moving average function which takes an array of numbers ("arr")
# and a window size ("k"); and returns an array of numbers which represents the moving
# average of "arr" given "k".

from typing import List, Tuple


def moving_avg(arr: List[int], k: int) -> List[int]:
    """
    A moving average function which takes an array of numbers ("arr") and a window size ("k");
    and returns an array of numbers which represents the moving average of "arr" given "k".

    :param arr: an array of numbers
    :param k: window size
    :return: an array of numbers which represents the moving average of "arr" given "k".
    """

    if len(arr) < k:
        raise ValueError("Window size is greater than the input array!")
    if k == 0:
        raise ValueError("Window size is zero!")

    res = []
    if not arr:
        # return empty array if the input array is empty
        return res
    for i in range(len(arr) - k + 1):
        # Looping through the input array and calculate the window average
        avg = sum(arr[i:i + k]) / k
        res.append(avg)

    return res


# Question 2. Given an infinite stream of positive integers ("s"),
# and a target positive integer ("t"), implement a function that
# iterates through the "s" and returns when and only when a combination
# of the numbers seen so far sums to "t".

def stream_sum(s, t: int) -> Tuple[int]:
    """
    iterates through the "s" and returns when and only when a combination
    of the numbers seen so far sums to "t".

       :param s: streaming data in the format of List, Generator, Or Iterator
       :param t: target
       :return List: the first combination sums up to target
    """

    dic = {}  # initiate a dictionary

    for i in s:
        # check if i greater than target, if true go to the next data
        if i > t:
            continue

        # check if i is equal to target, if true return i as a tuple
        elif i == t:
            return (i,)

        # if haven't seen i and i less than target, update the dictionary
        elif i < t and i not in dic:
            dic[(i,)] = t - i

        # check the dictionary, if a solution exits then return the solution
        # if not, adding new combinations whose sums less than targe
        for k in list(dic.keys()):
            if dic[k] - i == 0:
                return k + (i,)
            elif dic[k] - i > 0:
                dic[k + (i,)] = dic[k] - i


if __name__ == "__main__":
    # Question 1
    # Test Case 1
    arr = [1, 2, 3, 4, 5.75]
    k = 3
    print ('Question 1 Test Result: {}'.format(moving_avg(arr, k)))

    # Question 2
    # Test Case 1
    def generator():
        for i in [3, 8, 15, 8, 15, 18, 14, 22, 10, 21]:
            yield i
    t = 33
    print ('Question 2 Test 1 Result: {}'.format(stream_sum(generator(), t)))

    # Test Case 2
    def generator():
        for i in range(1000000):
            yield 2
        yield 1
    t = 5
    print ('Question 2 Test 2 Result: {}'.format(stream_sum(generator(), t)))
