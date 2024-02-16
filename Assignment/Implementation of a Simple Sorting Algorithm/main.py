# 95 / 100
# cause forgot about adding comments for a beginner to understand advance stuff

"""

Assignment Title: Implementation of a Simple Sorting Algorithm

Objective:

Implement a sorting algorithm in Python.
Compare the performance of the implemented algorithm with built-in sorting functions.

Requirements:

Choose one of the simple sorting algorithms: Bubble Sort, Selection Sort, or Insertion Sort.
Implement the chosen sorting algorithm in Python.

Create a function that generates a random list of integers. The function should take the length of the list as an argument.

Implement a function that takes an unsorted list as input and returns the sorted list using your implemented sorting algorithm.

Use the time module to measure the execution time of your sorting function for different input sizes (e.g., 100, 1000, 5000, 10000).

Compare the performance of your sorting algorithm with the built-in sorted function in Python. Measure the execution time for the same input sizes.

Create a plot using the matplotlib library to visualize the comparison of execution times for your sorting algorithm and the built-in sorting function.

"""

import time
import random
from matplotlib import pyplot as plt
from abc import ABCMeta, abstractstaticmethod

def Timed(function):
    """Decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        function(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        return execution_time
    return wrapper

class IAlgorithm(metaclass=ABCMeta):
    """Abstract base class for sorting algorithms."""

    @abstractstaticmethod
    def bubblesort(L: list):
        """ INTERFACE METHOD """

    def selectionsort(L: list):
        """ INTERFACE METHOD """

    def insertionsort(L: list):
        """ INTERFACE METHOD """

    def default_method(L: list):
        """ INTERFACE METHOD """

class Algorithm(IAlgorithm):
    """Implementation of sorting algorithms."""

    @staticmethod
    @Timed
    def bubblesort(L: list):
        for i in range(len(L)):
            for j in range(0, len(L)-i-1):
                if (L[j] >= L[j+1]):
                    L[j], L[j+1] = L[j+1], L[j]
        return ""

    @staticmethod
    @Timed
    def selectionsort(L: list):
        for i in range(len(L)):
            min_index = i
            for j in range(i + 1, len(L)):
                if L[j] < L[min_index]:
                    min_index = j

            L[i], L[min_index] = L[min_index], L[i]
        return ""

    @staticmethod
    @Timed
    def insertionsort(L: list):
        for i in range(len(L)-1):
            j = i
            while (L[j - 1] > L[j] and j > 0):
                L[j - 1], L[j] = L[j], L[j - 1]
                j-=1
        return ""
    
    @staticmethod
    @Timed
    def default_sort(L: list):
        L.sort()
        return ""
    
class AlgorithmFactory:

    @staticmethod
    def build_algorithm(algorithm_name, L):
        if (algorithm_name == "bubblesort"):
            return Algorithm.bubblesort(L)
        if (algorithm_name == "selectionsort"):
            return Algorithm.selectionsort(L)
        if (algorithm_name == "insertionsort"):
            return Algorithm.insertionsort(L)
        if (algorithm_name == "default"):
            return Algorithm.default_sort(L)
        
        print("Algorithm Not Supported!")
        return algorithm_name, ""

def plot_graph(execution_time_list, limit, algo_name, algo_name_index):
    """Plot the execution time comparison graph."""

    import numpy as np

    x = np.array(limit)
    split_execution_times = [execution_time_list[i:i + len(limit)] for i in range(0, len(execution_time_list), len(limit))]
    for index, sublist in enumerate(split_execution_times):
        y = np.array(sublist)
        if algo_name_index is not None:
            plt.plot(x, y, label=algo_name[algo_name_index])
        else:
            plt.plot(x, y, label=algo_name[index])
    plt.title("Implementation of a Simple Sorting Algorithm")
    plt.xlabel("Number of Elements in List")
    plt.ylabel("Time")
    plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)

if __name__ == "__main__":
    m_list, execution_time_list = [], []
    algorithms = ["bubblesort", "selectionsort", "insertionsort", "default"]
    algo = input("Enter name of Algorithm to test or all for comparing all Algorithms: ").lower().replace(" ", "")
    limit = [100, 1000, 5000, 10000]

    for i in range(1, len(limit)+1):
        
        print(f"Test #{i}")
    
        for j in range(random.randint(0, limit[i-1])):
            m_list.append(j)

        if algo == "all":
            for algo_name in algorithms:
                execution_time = AlgorithmFactory.build_algorithm(algo_name, m_list)
                execution_time_list.append(execution_time)
        else:
            execution_time = AlgorithmFactory.build_algorithm(algo, m_list)
            execution_time_list.append(execution_time)

    plot_graph(execution_time_list=execution_time_list, limit=limit, algo_name=algorithms, algo_name_index=algorithms.index(algo) if algo in algorithms else None)
    plt.show()