#!/usr/bin/env python3
# coding: utf-8

from abc import ABC, abstractmethod, ABCMeta

class SortStrategy(ABC):
    
    @abstractmethod
    def sort(self, array):
        pass        

class BubbleSortStrategy(SortStrategy):

    def sort(self, dataset): 
        print("Sorting using bubble sort")
        return dataset;

class QuickSortStrategy(SortStrategy):
    def sort(self, dataset): 
        print("Sorting using quick sort sort")
        return dataset;

class Sorter:
    def __init__(self, sorter):
        self.sorter = sorter

    def  sort(self, dataset):
        return self.sorter.sort(dataset);


if __name__ == '__main__':
    dataset = [1, 5, 4, 3, 2, 8]

    sorter = Sorter(BubbleSortStrategy())
    sorter.sort(dataset)

    sorter = Sorter(QuickSortStrategy());
    sorter.sort(dataset)
