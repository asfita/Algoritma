import numpy as np
import random
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time

# Set seed for reproducibility
random.seed(40)
np.random.seed(40)

# Generate 50 random integers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(50)]

# Sorting methods
def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end_time = time.time()
    return arr, end_time - start_time

def insertion_sort(arr):
    start_time = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    end_time = time.time()
    return arr, end_time - start_time

def selection_sort(arr):
    start_time = time.time()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    end_time = time.time()
    return arr, end_time - start_time

# Naive Bayes Analysis
def naive_bayes_analysis(numbers):
    # Prepare features for Naive Bayes
    # We'll use sliding windows of 3 numbers as features
    X = []
    y = []
    
    for i in range(len(numbers) - 3):
        X.append(numbers[i:i+3])
        y.append(1 if numbers[i+3] > numbers[i+2] else 0)
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)
    
    # Train Naive Bayes Classifier
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    
    # Predict and evaluate
    y_pred = gnb.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy

# Main execution
def main():
    print("Original Numbers:", numbers)
    
    # Bubble Sort
    bubble_sorted, bubble_time = bubble_sort(numbers.copy())
    print("\nBubble Sort:")
    print("Sorted Array:", bubble_sorted)
    print("Execution Time:", bubble_time)
    
    # Insertion Sort
    insertion_sorted, insertion_time = insertion_sort(numbers.copy())
    print("\nInsertion Sort:")
    print("Sorted Array:", insertion_sorted)
    print("Execution Time:", insertion_time)
    
    # Selection Sort
    selection_sorted, selection_time = selection_sort(numbers.copy())
    print("\nSelection Sort:")
    print("Sorted Array:", selection_sorted)
    print("Execution Time:", selection_time)
    
    # Naive Bayes Analysis
    nb_accuracy = naive_bayes_analysis(numbers)
    print("\nNaive Bayes Analysis:")
    print("Prediction Accuracy:", nb_accuracy)

if __name__ == "__main__":
    main()