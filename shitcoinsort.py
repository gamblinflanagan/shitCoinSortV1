# Iterative Merge sort 
# Iterative mergesort function to sort arr[0...n-1] 
 
# perform bottom up merge
def mergeSort(a):
    # start with least partition size of 2^0 = 1
    width = 1   
    n = len(a)                                          
    # subarray size grows by powers of 2 
    # since growth of loop condition is exponential, 
    # time consumed is logarithmic (log2n)
    while (width < n):
        # always start from leftmost
        l=0
        while (l < n): 
            r = min(l+(width*2-1), n-1)         
            m = min(l+width-1,n-1)
            # final merge should consider 
            # unmerged sublist if input arr
            # size is not power of 2              
            merge(a, l, m, r)
            l += width*2
        # Increasing sub array size by powers of 2
        width *= 2
    return a
   
# Merge Function 
def merge(a, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = a[l + i] 
    for i in range(0, n2): 
        R[i] = a[m + i + 1] 
 
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        inputBool = input("is asset ["+str(L[i])+"] outperforming asset ["+str(R[j])+"] (y/n)\t")
        if inputBool == 'y':#L[i] <= R[j]: 
            a[k] = L[i] 
            i += 1
        else: 
            a[k] = R[j] 
            j += 1
        k += 1
 
    while i < n1: 
        a[k] = L[i] 
        i += 1
        k += 1
 
    while j < n2: 
        a[k] = R[j] 
        j += 1
        k += 1
 
 
# Driver code 
#a = [69, 60, 30, 44]
inputArr = input("Enter elements of array separated by a space ' ' \t")
a = inputArr.split(' ')
if a[-1] == '':
    a.remove('')
print("Given list of assets is ") 
print(a) 
mergeSort(a) 
 
print("Assets listed in order of best to worst performing is ") 
for i in range(0, len(a)):
    print(str(i+1)+" "+str(a[i]))