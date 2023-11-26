numbers1 = [4, 1, 2, 3, 16, 9, 10, 14, 8, 7]
numbers2 = [1, 4, 7, 2, 5, 9, 0, 3, 6, 8]

def max_heapify(arr, index, length):
    '''
    Consider teh array as a tree,
    where left is 2 * index, right is 2 * index + 1
    and Keep the larget elements as a root
    '''
    left = 2 * index + 1
    right = left + 1
    max_idx = index
    
    if left < length and arr[left] > arr[index]:
        max_idx = left
    if right < length and arr[right] > arr[max_idx]:
        max_idx = right
    
    if max_idx != index:
        arr[max_idx], arr[index] = arr[index], arr[max_idx]
        max_heapify(arr, max_idx, length)
        
def build_heap(arr):
    '''
    Convert a normal array into a heap
    '''
    mid = len(arr)
    for index in range(mid, -1, -1):
        max_heapify(arr, index, len(arr))
        
def heap_sort(arr):
    '''
    Since the heap has the maximum element in the root
    exchange it with the last element
    get the max heap again and so on
    '''
    build_heap(arr)
    length = len(arr)
    for index in range(len(arr) -1, -1, -1):
        arr[0], arr[index] = arr[index], arr[0]
        length -= 1
        max_heapify(arr, 0, length)
        

heap_sort(numbers2)
# max_heapify(numbers, 0)
print(numbers2)

