# Asfita Saldarisya Nadjun_F55123072
# Quiz 1

import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    steps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            steps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return arr, steps, swaps

# Quick Sort
def quick_sort(arr):
    steps = 0
    swaps = 0

    def partition(low, high):
        nonlocal steps, swaps
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            steps += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i+1], arr[high] = arr[high], arr[i+1]
        swaps += 1
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi-1)
            quicksort_recursive(pi+1, high)

    quicksort_recursive(0, len(arr)-1)
    return arr, steps, swaps

# Test data
A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
B = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]

# Bubble Sort on A
start_time = time.time()
sorted_A_bubble, steps_A_bubble, swaps_A_bubble = bubble_sort(A.copy())
time_A_bubble = (time.time() - start_time) * 1000

# Bubble Sort on B
start_time = time.time()
sorted_B_bubble, steps_B_bubble, swaps_B_bubble = bubble_sort(B.copy())
time_B_bubble = (time.time() - start_time) * 1000

# Quick Sort on A
start_time = time.time()
sorted_A_quick, steps_A_quick, swaps_A_quick = quick_sort(A.copy())
time_A_quick = (time.time() - start_time) * 1000

# Quick Sort on B
start_time = time.time()
sorted_B_quick, steps_B_quick, swaps_B_quick = quick_sort(B.copy())
time_B_quick = (time.time() - start_time) * 1000

# Display results
print("Bubble Sort:")
print(f"Input A: {A}")
print(f"Output A: {sorted_A_bubble}")
print(f"Time: {time_A_bubble:.10f} ms\n Steps: {steps_A_bubble}\n Swaps: {swaps_A_bubble}\n")
print(f"Input B: {B}")
print(f"Output B: {sorted_B_bubble}")
print(f"Time: {time_B_bubble:.10f} ms\n Steps: {steps_B_bubble}\n Swaps: {swaps_B_bubble}\n")

print("\nQuick Sort:")
print(f"Input A: {A}")
print(f"Output A: {sorted_A_quick}")
print(f"Time: {time_A_quick:.10f} ms\n Steps: {steps_A_quick}\n Swaps: {swaps_A_quick}\n")
print(f"Input B: {B}")
print(f"Output B: {sorted_B_quick}")
print(f"Time: {time_B_quick:.10f} ms\n Steps: {steps_B_quick}\n Swaps: {swaps_B_quick}\n")

# Analysis
print("Analysis:")
if time_A_bubble < time_A_quick:
    print("Bubble Sort is faster for list A.")
else:
    print("Quick Sort is faster for list A.")

if time_B_bubble < time_B_quick:
    print("Bubble Sort is faster for list B.")
else:
    print("Quick Sort is faster for list B.")

#Analisis Untuk Jawaban nomor 2:
#Kinerja algoritma Bubble Sort dan Quick Sort berbeda tergantung pada struktur daftar (list) yang diurutkan. Pada list A, yang disusun secara terbalik, Quick Sort jauh lebih cepat karena pendekatan divide-and-conquer-nya, yang meminimalkan jumlah perbandingan dan pertukaran (swap) dengan membagi daftar secara efisien. Sebaliknya, Bubble Sort memproses daftar secara berurutan dan membutuhkan banyak iterasi untuk menyelesaikan pengurutan, sehingga kurang efisien dalam kasus ini.
#Pada list B, yang sudah sebagian terurut, Bubble Sort lebih unggul dibandingkan Quick Sort. Bubble Sort memanfaatkan urutan yang hampir teratur ini, sehingga membutuhkan lebih sedikit pertukaran dan iterasi untuk mencapai hasil akhir. Sementara itu, Quick Sort tetap melibatkan pembagian (partitioning) dan pemanggilan rekursif, yang bisa menjadi kurang efisien untuk input yang kecil atau hampir terurut.
#Pada list B, yang sudah sebagian terurut, Bubble Sort lebih unggul dibandingkan Quick Sort. Bubble Sort memanfaatkan urutan yang hampir teratur ini, sehingga membutuhkan lebih sedikit pertukaran dan iterasi untuk mencapai hasil akhir. Sementara itu, Quick Sort tetap melibatkan pembagian (partitioning) dan pemanggilan rekursif, yang bisa menjadi kurang efisien untuk input yang kecil atau hampir terurut.