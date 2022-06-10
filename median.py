from multiprocessing import Array
from statistics import median


def solution():
    nums1 = list(map(int, input()))
    nums2 = list(map(int, input()))

    arr = nums1 + nums2
    med = median(arr)
    print(med)
solution()