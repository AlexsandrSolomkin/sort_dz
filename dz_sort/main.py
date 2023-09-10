import random
import time

def how_long(func, x):
    start = time.time()
    func(x)
    print(f"Скорость работы: {time.time() - start}")

# def sorting_pyramid(list_data: list):
def heapify(list_data: list, heap_size: int, root_index: int) -> list:
    largest = root_index # инициализируем наибольший элемент как корень
    left_child = 2 * root_index + 1 # левый = 2 * 2 * root_index + 1
    right_child = 2 * root_index + 2 # правый = 2 * 2 * root_index + 2

    # Если левый дочерний элемент больше корня
    if (left_child < heap_size and list_data[left_child] > list_data[largest]):
        largest = left_child

    # Если правый дочерний элемент больше, чем самый большой элемент на данный момент
    if (right_child < heap_size and list_data[right_child] > list_data[largest]):
        largest = right_child
    
    # Если самый большой элемент не корень
    if (largest != root_index):
        temp = list_data[root_index]
        list_data[root_index] = list_data[largest]
        list_data[largest] = temp
    
    # Рукурсивно преобразуем в двоичную кучу затронутое поддерево
    heapify(list_data, heap_size, largest)