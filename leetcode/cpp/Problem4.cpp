#include "Problem4.h"
#include <limits>


// O(log(min(m+n))) run time where n and m are size of nums1 and nums2
float findMedianSortedArrays(vector<int> nums1, vector<int> nums2){
    vector<int> *a = &nums1;
    vector<int> *b = &nums2;
    if (nums1.size() > nums2.size()){
        b = &nums1;
        a = &nums2;
    }
    int total = nums1.size() + nums2.size();
    int half = total / 2;

    int l = 0;
    int r = a->size() - 1;
    while (true){
        int i = floor((l + r) / 2.0);
        if ((l == -1  && r == 0) || (r == -1 && l == 0)){
            i = -1;
        }
        int j = half - i - 2;

        int al = i >= 0 ? (*a)[i] : std::numeric_limits<int>::min();
        int ar = (i + 1) < (*a).size() ? (*a)[i + 1] : std::numeric_limits<int>::max();

        int bl = j >= 0 ? (*b)[j] : std::numeric_limits<int>::min();
        int br = (j + 1) < (*b).size() ? (*b)[j + 1] : std::numeric_limits<int>::max();

        if (al <= br && bl <= ar){
            if (total % 2 == 1){
                if (ar < br){
                    return ar;
                }
                else{
                    return br;
                }
            }
            else {
                int max = -1;
                if (al > bl){
                    max = al;
                }
                else{
                    max = bl;
                }
                int min = -1;
                if (ar < br){
                    min = ar;
                }
                else{
                    min = br;
                }
                return ((min + max) / 2.0);
            }
        }
        else if (al > br){
            r = i - 1;
        }
        else{
            l = i + 1;
        }
    }
}
/*
// O(m+n) run time where n and m are size of nums1 and nums2
float findMedianSortedArrays(vector<int> nums1, vector<int> nums2){
    vector<int> concat;
    int i = 0;
    int j = 0;
    while (i < nums1.size() or j < nums2.size()){
        if (i < nums1.size()){
            if (j < nums2.size()){
                if (nums1[i] < nums2[j]){
                    concat.push_back(nums1[i]);
                    ++i;
                }
                else {
                    concat.push_back(nums2[j]);
                    ++j;
                }
            }
            else{
                concat.push_back(nums1[i]);
                ++i;
            }
        }
        else {
            concat.push_back(nums2[j]);
            ++j;
        }
    }
    if (concat.size() % 2 == 0){
        return (concat[concat.size() / 2] + concat[concat.size() /2 - 1]) / 2.0;
    }
    else{
        return concat[concat.size() / 2];
    }
}
*/