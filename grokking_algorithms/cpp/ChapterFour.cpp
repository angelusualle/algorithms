#include <stdlib.h>

int partition(int arr[], int a, int b) {
    int randNum = rand();
    int range = b-a + 1;
    int p = a;
    if (range == 1){
        return p;
    }
    p = (randNum % range) + a;

    int piv = arr[p];
    arr[p] = arr[b];
    arr[b] = piv;
    int j = b - 1;
    int i = a;
    while (i <= j){
        while (arr[i] <= piv && i <= j){
            i ++;
        }
        while (arr[j] >= piv && j >= i){
            j--;
        }
        if (i < j){
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    arr[b] = arr[i];
    arr[i] =piv;
    return i;
}

void quickSort(int arr[], int size, int a = 0, int b = -1){
    if (b == -1){
        b = size-1;
    }
    while (a < b) {
        int p = partition(arr, a, b);
        if ((p - a) < (b - p)){
            quickSort(arr, size, a, p-1);
            a = p + 1;
        }
        else{
            quickSort(arr, size, p+1, b);
            b = p - 1;
        }
    }

}