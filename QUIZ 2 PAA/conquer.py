import numpy as np
import random
import time
import sys
sys.setrecursionlimit(10000)

class SortingAnalysis:
    def __init__(self, seed=40, size=50, min_val=1, max_val=100):
        np.random.seed(seed)
        random.seed(seed)
        
        # Generate data random
        self.data = np.random.randint(min_val, max_val+1, size).tolist()
        
    def bubble_sort(self, arr):
        """
        Implementasi Bubble Sort
        Best Case: O(n) - Ketika data sudah terurut
        """
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            
            if not swapped:
                break
        return arr

    def insertion_sort(self, arr):
        """
        Implementasi Insertion Sort
        Best Case: O(n) - Ketika data hampir terurut
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def merge_sort(self, arr):
        """
        Implementasi Merge Sort
        Best Case: O(n log n) - Konsisten untuk semua kondisi
        """
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        
        return self._merge(left, right)

    def _merge(self, left, right):
        """
        Proses merger untuk Merge Sort
        """
        result = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result

    def quick_sort(self, arr):
        """
        Implementasi Quick Sort
        Best Case: O(n log n) - Ketika pivot tepat di tengah
        """
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def analisis_sorting(self):
        """
        Melakukan analisis untuk berbagai metode sorting
        """
        sorting_methods = {
            'Bubble Sort': self.bubble_sort,
            'Insertion Sort': self.insertion_sort,
            'Merge Sort': self.merge_sort,
            'Quick Sort': self.quick_sort
        }
        
        print("\n📊 Analisis Sorting Methods 📊")
        print("-" * 50)
        print(f"Data Awal: {self.data}\n")
        
        for nama_metode, metode in sorting_methods.items():
            # Salin data untuk menghindari modifikasi asli
            data_copy = self.data.copy()
            
            # Ukur waktu eksekusi
            start_time = time.time()
            sorted_data = metode(data_copy)
            end_time = time.time()
            
            # Analisis best case
            print(f"\n{nama_metode}:")
            print(f"Waktu Eksekusi: {(end_time - start_time) * 1000:.4f} ms")
            print(f"Hasil Terurut: {sorted_data}")
            
            # Verifikasi pengurutan
            if sorted_data == sorted(self.data):
                print("Pengurutan Benar: ✓")
            else:
                print("Pengurutan Salah: ✗")
            
            # Penjelasan best case
            if nama_metode == 'Bubble Sort':
                print("Best Case: O(n) - Ketika data sudah terurut")
            elif nama_metode == 'Insertion Sort':
                print("Best Case: O(n) - Ketika data hampir terurut")
            elif nama_metode == 'Merge Sort':
                print("Best Case: O(n log n) - Selalu sama untuk semua kondisi input")
            elif nama_metode == 'Quick Sort':
                print("Best Case: O(n log n) - Ketika pivot tepat di tengah")

def main():
    # Inisialisasi dan jalankan analisis
    sorter = SortingAnalysis(seed=40, size=50, min_val=1, max_val=100)
    sorter.analisis_sorting()

if __name__ == '__main__':
    main()
