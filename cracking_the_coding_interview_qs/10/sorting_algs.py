class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def print(self):
        return "Name: %s, Age: %i" % (self.name, self.age)

# O(n) since specified range
def bucket_sort_age(people):
    buckets = {}
    for person in people:
        if person.age in buckets:
            buckets[person.age].append(person)
        else:
            buckets[person.age]= [person]
    ans = []
    for age in range(0, 151):
        while age in buckets and len(buckets[age]) > 0:
            ans.append(buckets[age].pop())
    return ans

# O(n^2) average and worst case
def bubble_sort(arr):
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(len(arr) -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                unsorted = True

# O(n^2) average and worst case
def selection_sort(arr):
    for i in range(len(arr)):
        j = i
        y = i
        while y < len(arr):
            if arr[y] < arr[j]:
                j = y
            y += 1
        arr[i], arr[j] = arr[j], arr[i]

# O(nlogn) average and worst case time and O(n) space
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    ans = left[:]
    ans.extend(right)
    i = 0
    j = 0
    z = 0
    while i< len(left) and j < len(right):
        if left[i] < right[j]:
            ans[z] = left[i]
            i += 1
            z += 1
        else:
            ans[z] = right[j]
            z += 1
            j += 1
    while i < len(left):
        ans[z] = left[i]
        i += 1
        z += 1
    return ans

# O(n^2) time worst case  O(nlogn) if random access to partition is used, O(1) space, but usually faster than mergesort
# Typically, quicksort is significantly faster in practice than other Θ(nlogn) algorithms, because it requires little
# additional space and exhibits good cache locality, and this makes it faster than merge sort in many cases.
# In addition, it’s very easy to avoid quicksort’s worst-case run time of O(n2) almost entirely by using an 
# appropriate choice of the pivot – such as picking it at random (this is an excellent strategy).
# As many people have noted, the average case performance for quicksort is faster than mergesort. But 
# this is only true if you are assuming constant time to access any piece of memory on demand.
# In RAM this assumption is generally not too bad (it is not always true because of caches, but it is not too bad). 
# However if your data structure is big enough to live on disk, then quicksort gets killed by the fact that your average disk
#  does something like 200 random seeks per second. But that same disk has no trouble reading or writing megabytes per second of
#  data sequentially. Which is exactly what mergesort does. Therefore if data has to be sorted on disk, you really, really want
#  to use some variation on mergesort. (Generally you quicksort sublists, then start merging them together above some size threshold.)
# best case is median hit.
from random import randint
def quick_sort(arr):
    return quick_sort_recursive(arr, 0, len(arr) - 1)

def quick_sort_recursive(A, a, b):
    while a < b:
        p = partition(A, a, b)
        if p - a < b - p:
            quick_sort_recursive(A,a,p-1)
            a = p + 1
        else:
            quick_sort_recursive(A,p+1,b)
            b = p - 1
    
def partition(A, a, b):
    p = randint(a,b)
    piv = A[p]
    A[p], A[b] = A[b], A[p]
    i = a
    j = b - 1
    while i <= j:
        while A[i] <= piv and i <= j:
            i += 1
        while A[j] >= piv and j >= i:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[b] = A[i]
    A[i] = piv
    return i
    