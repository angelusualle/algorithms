void selectionSort(int arr[], int size){
    for (int i = 0; i < size; i++){
        int smallest = arr[i];
        int smallestIndex = i;
        for (int j = i; j < size; j++){
            if (arr[j] < smallest){
                smallest = arr[j];
                smallestIndex = j;
            }
        }
        int t = arr[i];
        arr[i] = smallest;
        arr[smallestIndex] = t;
    }
}