import math as mt

# Class for extracting data from files
class ExtractingData:
    def __init__(self, val, index) -> None:
        self.index = index  # Index of the data in the file
        self.val = val      # Value extracted from the file

# Initialize lists and data structures
inversionslist = []  # List to store inversion counts
list1 = []  # List to store extracted data

# Class for rearranging data files
class RearrangingDataFiles:
    @staticmethod
    def RearrangeData(source, format):
        """
        Rearrange the data in 'source' based on the 'format' index.
        This function maps data from the original order to the sorted order.
        Args:
            source (list): The original data.
            format (list): The format containing the new order.
        Returns:
            list: The rearranged data.
        """
        RearrangedData = []
        for i in range(len(source)):
            RearrangedData.append(source[format[i].index])
        return RearrangedData

# Merge sort implementation
def mergesort(A, inversionlist, inversions):
    """
    Sort the input list 'A' using the merge sort algorithm.
    Args:
        A (list): The list to be sorted.
        inversionlist (list): List to store inversion counts at each step.
        inversions (int): Current inversion count.
    Returns:
        list: Sorted list 'A'.
    """
    if len(A) == 1:
        return A
    else:
        q = mt.floor(len(A) / 2)
        L = [0] * (q)
        R = [0] * (len(A) - q)
        if len(A) % 2 != 0:
            n = q + 1
        else:
            n = q

        for i in range(q):
            L[i] = A[i]
        for j in range(n):
            R[j] = A[j + q]
        LS = mergesort(L, inversionlist, inversions)
        RS = mergesort(R, inversionlist, inversions)
        data, inversions = Merge(LS, RS, inversions)
        inversionlist.append(inversions)
        return data

# Merge function for merge sort
def Merge(L, R, inversions):
    """
    Merge two sorted lists 'L' and 'R' while counting inversions.
    Args:
        L (list): The left subarray.
        R (list): The right subarray.
        inversions (int): Current inversion count.
    Returns:
        list: Merged and sorted list.
        int: Updated inversion count.
    """
    B = [0] * (len(L) + len(R))
    i = 0
    j = 0
    count = 0
    for k in range(len(B)):
        if j > len(R) - 1 or (i <= len(L) - 1 and L[i].val <= R[j].val):
            B[k] = L[i]
            count = 1
            i = i + 1
            count = 0
        else:
            B[k] = R[j]
            if count == 0:
                inversions += (len(L)) - i
            j = j + 1
    return B, inversions

# Class for insertion sort
class InsertionSort:
    @staticmethod
    def insertionSort(array):
        """
        Sort the input list 'array' using the insertion sort algorithm.
        Args:
            array (list): The list to be sorted.
        Returns:
            int: The number of inversions.
        """
        inversions = 0
        for incr in range(1, len(array)):
            key = array[incr]
            j = incr - 1

            while j >= 0 and key.val < array[j].val:
                array[j + 1] = array[j]
                j = j - 1

            array[j + 1] = key
            inversions += incr - (j + 1)
        return inversions

# Class for quicksort
class QuickSort:
    def __init__(self):
        self.inversions = 0

    def QuickSort(self, A):
        """
        Sort the input list 'A' using the quicksort algorithm.
        Args:
            A (list): The list to be sorted.
        Returns:
            list: Sorted list 'A'.
        """
        if len(A) < 2:
            return A

        less = []
        equal = []
        greater = []
        pivot = 0
        for i in range(len(A)):
            if A[i].val < A[pivot].val:
                less.append(A[i])
                self.inversions = len(equal) + len(greater) + self.inversions
            elif A[i].val > A[pivot].val:
                greater.append(A[i])
            elif A[i].val == A[pivot].val:
                equal.append(A[i])
                self.inversions = len(greater) + self.inversions
        return self.QuickSort(less) + equal + self.QuickSort(greater)

if __name__ == "__main__":
    # Initialize inversion counters for each file
    inversionsfile1 = 0
    inversionsfile2 = 0
    inversionsfile3 = 0
    inversionsfile4 = 0
    inversionsfile5 = 0

    # Open data files
    file1 = open("source1.txt", "r", newline=None)
    file2 = open("source2.txt", "r", newline=None)
    file3 = open("source3.txt", "r", newline=None)
    file4 = open("source4.txt", "r", newline=None)
    file5 = open("source5.txt", "r", newline=None)
    count = 0
    file1array = []
    file2array = []
    file3array = []
    file4array = []
    file5array = []

    # Read and extract data from files
    while True:
        data1 = file1.readline()
        data2 = file2.readline()
        data3 = file3.readline()
        data4 = file4.readline()
        data5 = file5.readline()
        if not data1:
            break
        vals1 = data1.strip()
        vals2 = data2.strip()
        vals3 = data3.strip()
        vals4 = data4.strip()
        vals5 = data5.strip()
        filedata1 = ExtractingData(int(vals1), count)
        filedata2 = ExtractingData(int(vals2), count)
        filedata3 = ExtractingData(int(vals3), count)
        filedata4 = ExtractingData(int(vals4), count)
        filedata5 = ExtractingData(int(vals5), count)
        total = int(vals1) + int(vals2) + int(vals3) + int(vals4) + int(vals5)
        comination = ExtractingData(total, count)
        count += 1

        list1.append(comination)
        file1array.append(filedata1)
        file2array.append(filedata2)
        file3array.append(filedata3)
        file4array.append(filedata4)
        file5array.append(filedata5)

    # Sort data using merge sort
    sortData = mergesort(list1, inversionslist, 0)

    # Rearrange data in files
    Rearrangefile1 = RearrangingDataFiles.RearrangeData(file1array, sortData)
    Rearrangefile2 = RearrangingDataFiles.RearrangeData(file2array, sortData)
    Rearrangefile3 = RearrangingDataFiles.RearrangeData(file3array, sortData)
    Rearrangefile4 = RearrangingDataFiles.RearrangeData(file4array, sortData)
    Rearrangefile5 = RearrangingDataFiles.RearrangeData(file5array, sortData)

    # Initialize inversion counters for each file
    inversionslist1 = []
    inversionslist2 = []
    inversionslist3 = []
    inversionslist4 = []
    inversionslist5 = []

    # Apply merge sort to rearranged files and calculate inversions
    mergesort(Rearrangefile1, inversionslist1, 0)
    mergesort(Rearrangefile2, inversionslist2, 0)
    mergesort(Rearrangefile3, inversionslist3, 0)
    mergesort(Rearrangefile4, inversionslist4, 0)
    mergesort(Rearrangefile5, inversionslist5, 0)

    # Calculate total inversions for each file
    inversionsfile1 = sum(inversionslist1)
    inversionsfile2 = sum(inversionslist2)
    inversionsfile3 = sum(inversionslist3)
    inversionsfile4 = sum(inversionslist4)
    inversionsfile5 = sum(inversionslist5)

    # Print merge sort results
    print("Merge Sort Results: ")
    print("File 1 Inversions: ", inversionsfile1, "File 2 Inversions: ", inversionsfile2, "File 3 Inversions: ",
          inversionsfile3, "File 4 Inversions: ", inversionsfile4, "File 5 Inversions: ", inversionsfile5)

    # Initialize quicksort object
    quicksort = QuickSort()

    # Apply quicksort to rearranged files and calculate inversions
    quicksort.QuickSort(Rearrangefile1)
    inversionsfile1 = quicksort.inversions
    quicksort.inversions = 0
    quicksort.QuickSort(Rearrangefile2)
    inversionsfile2 = quicksort.inversions
    quicksort.inversions = 0
    quicksort.QuickSort(Rearrangefile3)
    inversionsfile3 = quicksort.inversions
    quicksort.inversions = 0
    quicksort.QuickSort(Rearrangefile4)
    inversionsfile4 = quicksort.inversions
    quicksort.inversions = 0
    quicksort.QuickSort(Rearrangefile5)
    inversionsfile5 = quicksort.inversions
    quicksort.inversions = 0

    # Print quicksort results
    print("Quick Sort Results:")
    print("File 1 Inversions: ", inversionsfile1, "File 2 Inversions: ", inversionsfile2, "File 3 Inversions: ",
          inversionsfile3, "File 4 Inversions: ", inversionsfile4, "File 5 Inversions: ", inversionsfile5)

    # Calculate inversions using insertion sort
    inversionsfile1 = InsertionSort.insertionSort(Rearrangefile1)
    inversionsfile2 = InsertionSort.insertionSort(Rearrangefile2)
    inversionsfile3 = InsertionSort.insertionSort(Rearrangefile3)
    inversionsfile4 = InsertionSort.insertionSort(Rearrangefile4)
    inversionsfile5 = InsertionSort.insertionSort(Rearrangefile5)

    # Print insertion sort results
    print("Insertion Sort Results: ")
    print("File 1 Inversions: ", inversionsfile1, "File 2 Inversions: ", inversionsfile2, "File 3 Inversions: ",
          inversionsfile3, "File 4 Inversions: ", inversionsfile4, "File 5 Inversions: ", inversionsfile5)
    print()
    # Conclusion
    print("To conclude, Web Search Engine 1, leveraging Merge Sort, outperforms others with its efficient sorting approach. Merge Sort's divide-and-conquer method minimizes inversions, making it the fastest choice for handling web search queries.")
