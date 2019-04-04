
'''Tries to find the median of two sorted arrays in O(m+n) time'''

def findMedianSortedArrays(nums1, nums2) -> float:
    result = 0
    combined = sorted(nums1 + nums2)
    if len(combined) % 2 is 0:
        first_candidate = int(combined[(len(combined)//2)-1])
        second_candidate = int(combined[(len(combined)//2)])
        result = (first_candidate+second_candidate)/2
    else:
        index = (len(combined)+1)//2
        result = combined[index-1]
    return result


if __name__ == '__main__':
    arr1 = input("Array 1: ").split(" ")
    arr2 = input("Array 2: ").split(" ")
    f = findMedianSortedArrays(arr1,arr2)
    print(f)
