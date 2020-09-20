import bisect
from heapq import merge as heapq_merge

class Arr:


    def __init__(self, content = None, ascending_order = True):

        self.array = []
        self.ascending_order = ascending_order

        if content:
            self.add_multiple(content)
    


    def add_one(self, item):

        if item:
            if type(item) == int or type(item) == float:
                if self.ascending_order:

                    bisect.insort_left(self.array, item)    # Using bisect because it faster
                else:

                    self.reverse_insort(item)   # bisect cant work with descending lists
            else:
                print(f"Error addind item to array, '{item}' is not a number!")
        else:
            print("No item!")

        return self.array


    def add_multiple(self, content):

        if content:
            for item in content:
                
                self.add_one(item)

        else:
            print("No content!")

        return self.array


    def dell_one(self, item):

        try:
            self.array.remove(item)

        except ValueError:
            print(f"No item '{item}' in array")

        return self.array


    def dell_multiple(self, content):

        if content:
            for item in content:

                self.dell_one(item)

        else:
            print("No content!")

        return self.array


    def clear(self):

        self.array = []

        return self.array


    def merge(self, content, to_list = False):

        if content:

            if content.ascending_order == self.ascending_order:

                array = list(heapq_merge(self.array, content.to_list()))
            else:
                array = list(heapq_merge(self.array, content.ch_order()))

            if to_list:

                return array
            else:
                self.array = array
                return self.array

        else:
            print("No content!")


    def ch_order(self):

        self.ascending_order = not self.ascending_order

        if self.ascending_order:
            self.array.sort()
        else:
            self.array.sort(reverse=True)

        return self.array



    def reverse_insort(self, item):

        start = 0
        end = len(self.array)

        while start < end:
            mid = (start+end)//2
            if item > self.array[mid]:
                end = mid
            else:
                start = mid+1

        self.array.insert(start, item)


    def to_list(self):
        return self.array

    def __str__(self):
        return str(self.array)
        

            


