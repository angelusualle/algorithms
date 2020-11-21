# O(n)
def sort_valley_peaks(arr):
    i = 1
    while i < len(arr):
        if i +1 < len(arr) and arr[i] < arr[i+1] and arr[i - 1] <= arr[i + 1]:
            arr[i],arr[i+1] = arr[i + 1], arr[i]
        elif arr[i - 1] > arr[i] and arr[i-1] >= arr[i + 1]:
            arr[i], arr[i -1] = arr[i-1], arr[i]        
        i += 2