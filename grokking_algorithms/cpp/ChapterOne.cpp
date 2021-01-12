int binary_search(int arr[], int size, int target){
    int high = size - 1;
    int low = 0;
    while (low <= high){
        int mid = (high + low) / 2;
        if (target == arr[mid]){
            return mid;
        }
        else if (target < arr[mid]){
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
    }
    return -1;
}