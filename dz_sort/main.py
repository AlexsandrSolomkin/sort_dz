import random
import time


# def how_long(func, x):
#     start = time.time()
#     func(x)
#     print(f"Скорость работы: {time.time() - start}")

# ==============================================================================================

def swap(list_data, i, j):
    list_data[i], list_data[j] = list_data[j], list_data[i]

def siftDown(list_data, i, upper):
    while(True):
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < upper:
            if list_data[i] >= max(list_data[l], list_data[r]): break
            elif list_data[l] > list_data[r]:
                swap(list_data, i, l)
                i = l
            else:
                swap(list_data, i, r)
                i = r
        elif l < upper:
            if list_data[l] > list_data[i]:
                swap(list_data, i, l)
                i = l
            else: break
        elif r < upper:
            if list_data[r] > list_data[i]:
                swap(list_data, i, r)
                i = r
            else: break
        else: break


def heapsort(list_data):
    for j in range((len(list_data) - 2) // 2, -1, -1):
        siftDown(list_data, j, len(list_data))

    for end in range(len(list_data) - 1, 0, -1):
        swap(list_data, 0, end)
        siftDown(list_data, 0, end)

# ==============================================================================================

test_list = [random.randint(0, 100) for _ in range(10)]
print(test_list)
heapsort(test_list)
print(test_list)

# ==============================================================================================
