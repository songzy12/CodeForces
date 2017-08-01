## Binary Index Tree

http://www.geeksforgeeks.org/binary-indexed-tree-range-updates-point-queries/

Given an array arr[0..n-1]. The following operations need to be performed.

* update(l, r, val) : Add ‘val’ to all the elements in the array from [l, r].
* getElement(i) : Find element in the array indexed at ‘i’.

Initially all the elements in the array are 0. Queries can be in any oder, i.e., there can be many updates before point query.

The problem can reduced to update and prefix sum queries.

* update(l, r, val) : Add ‘val’ to the lth element and subtract ‘val’ from the (r+1)th element, do this for all the update queries.
  arr[l]   = arr[l] + val
  arr[r+1] = arr[r+1] - val
* getElement(i) : To get ith element in the array find the sum of all integers in the array from 0 to i.(Prefix Sum).

BIT can be used to do update and prefix sum queries in O(Logn) time.

```
// C++ code to demonstrate Range Update and
// Point Queries on a Binary Index Tree
#include <iostream>
using namespace std;
 
// Updates a node in Binary Index Tree (BITree) at given index
// in BITree. The given value 'val' is added to BITree[i] and
// all of its ancestors in tree.
void updateBIT(int BITree[], int n, int index, int val)
{
    // index in BITree[] is 1 more than the index in arr[]
    index = index + 1;
 
    // Traverse all ancestors and add 'val'
    while (index <= n)
    {
        // Add 'val' to current node of BI Tree
        BITree[index] += val;
 
        // Update index to that of parent in update View
        index += index & (-index);
    }
}
 
// Constructs and returns a Binary Indexed Tree for given
// array of size n.
int *constructBITree(int arr[], int n)
{
    // Create and initialize BITree[] as 0
    int *BITree = new int[n+1];
    for (int i=1; i<=n; i++)
        BITree[i] = 0;
 
    // Store the actual values in BITree[] using update()
    for (int i=0; i<n; i++)
        updateBIT(BITree, n, i, arr[i]);
 
    // Uncomment below lines to see contents of BITree[]
    //for (int i=1; i<=n; i++)
    //      cout << BITree[i] << " ";
 
    return BITree;
}
 
// SERVES THE PURPOSE OF getElement()
// Returns sum of arr[0..index]. This function assumes
// that the array is preprocessed and partial sums of
// array elements are stored in BITree[]
int getSum(int BITree[], int index)
{
    int sum = 0; // Iniialize result
 
    // index in BITree[] is 1 more than the index in arr[]
    index = index + 1;
 
    // Traverse ancestors of BITree[index]
    while (index>0)
    {
        // Add current element of BITree to sum
        sum += BITree[index];
 
        // Move index to parent node in getSum View
        index -= index & (-index);
    }
    return sum;
}
 
// Updates such that getElement() gets an increased
// value when queried from l to r.
void update(int BITree[], int l, int r, int n, int val)
{
    // Increase value at 'l' by 'val'
    updateBIT(BITree, n, l, val);
 
    // Decrease value at 'r+1' by 'val'
    updateBIT(BITree, n, r+1, -val);
}
 
// Driver program to test above function
int main()
{
    int arr[] = {0, 0, 0, 0, 0};
    int n = sizeof(arr)/sizeof(arr[0]);
    int *BITree = constructBITree(arr, n);
 
    // Add 2 to all the element from [2,4]
    int l = 2, r = 4, val = 2;
    update(BITree, l, r, n, val);
 
    // Find the element at Index 4
    int index = 4;
    cout << "Element at index " << index << " is " <<
         getSum(BITree,index) << "\n";
 
    // Add 2 to all the element from [0,3]
    l = 0, r = 3, val = 4;
    update(BITree, l, r, n, val);
 
    // Find the element at Index 3
    index = 3;
    cout << "Element at index " << index << " is " <<
         getSum(BITree,index) << "\n" ;
 
    return 0;
}
```