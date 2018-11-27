'''
Created by: Kevin Rodriguez
Last Modified: November, 26
Professor: Diego Aguirre


Purpose: In this lab, I had to finish the class for a Min Heap. We had to create a function that will create the min heap as well
as being able to create a function that extracts the min and keep the Min_Heap property. By using the extract min method, I was
able to create a the Heap_Sort method that was part of the lab as well.

BIG O Notation: Heap Sort's Big O is O(n log n). The advantage that this sorting algorithm has over something like Quick Sort, is that
Heap Sort has a worst case scenario with a running time of O(n log n) comparing to Quick Sort's worst case of O(n^2)

'''

class Heap:

    def __init__(self):
        self.heap_array = []


    def insert(self, k):
        self.heap_array.append(k)

        self.creating_min_heap()


    """this method is used in order heapify the heap whenever is created"""
    def heapify(self, index):

        #starting from the end of the list to check every index to its parent
        while index > 0:

            parent = (index - 1) // 2

            #if the son is greater than parent, minHeap property holds
            if self.heap_array[index] >= self.heap_array[parent]:
                index = parent

            #violates minHeap property swap parent with child
            else:

                temp = self.heap_array[index]
                self.heap_array[index] = self.heap_array[parent]
                self.heap_array[parent] = temp

                index = parent

    '''This method extracts the min from the heap and heapifies in order to preserve min_heap
    properties'''
    def extract_min(self):

        if self.is_empty():
            return None

        #smallest element is the first element
        min_elem = self.heap_array[0]

        #hold value of the last element in the list
        replacement = self.heap_array[len(self.heap_array) - 1]

        #remove the last element from the list
        self.heap_array.remove(self.heap_array[len(self.heap_array) - 1])

        #replace the first element with the last element of the list
        self.heap_array[0] = replacement

        #heapify to maintain minHeap property
        self.creating_min_heap()


        return min_elem


    '''this method extracts the min from the heap until it is empty in order to do heap sort'''
    def heap_sort(self):

        sorted_list = []

        while len(self.heap_array) is not 1:

            min_val = self.extract_min()

            sorted_list.append(min_val)

        sorted_list.append(self.heap_array[0])

        return sorted_list



    '''This method is used in order to create a min heap from a file reader'''
    def creating_min_heap(self):

        if len(self.heap_array) == 1:
            return self

        child = len(self.heap_array) - 1

        while child > 0:

            parent = (child - 1) // 2

            if self.heap_array[child] < self.heap_array[parent]:
                temp = self.heap_array[child]
                self.heap_array[child] = self.heap_array[parent]
                self.heap_array[parent] = temp

            child -= 1

        return self



    '''checks if the heap is empty'''
    def is_empty(self):
        return len(self.heap_array) == 0

    '''prints the heap'''
    def print_heap(self):
        for i in range(len(self.heap_array)):
            print(self.heap_array[i])


def read_file(file):

    heap_array = Heap()
    for line in file:
        number = line.split(",")
        for i in range(len(number)):
            heap_array.insert(int(number[i]))

    file.close()

    return heap_array

def print_list(list):
     for i in range(len(list)):
        print(list[i])


'''function in order to test program if it works by inserting random numbers'''
def creating_min_heap():

    min_heap = Heap()

    min_heap.insert(5)
    min_heap.insert(10)
    min_heap.insert(2)
    min_heap.insert(1)
    min_heap.insert(1)

    print("----------MIN_HEAP----------------")
    min_heap.print_heap()



    print("----------HEAPSORT----------------")
    sorted_list = min_heap.heap_sort()
    print_list(sorted_list)


'''Method in order to test program to see if it works with a CSV file'''
def from_file():

    min_heap = Heap()

    file = open('numbers.txt','r')

    min_heap = read_file(file)

    print("----------MIN_HEAP----------------")

    min_heap.print_heap()



    print("----------HEAPSORT----------------")
    sorted_heap = min_heap.heap_sort()
    print_list(sorted_heap)



creating_min_heap()
from_file()