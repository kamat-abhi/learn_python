class Car:
    def __init__(self, brand, model):
        
        self.brand = brand
        self.model = model


my_car = Car("Toyota", "Corolla")
print(my_car.brand)  

from collections import defaultdict

class SubarraySumCounter:
    def __init__(self, nums):
        self.nums = nums

    def count_subarrays_with_sum(self, k):
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # To handle subarrays that start from index 0

        current_sum = 0
        count = 0

        for num in self.nums:
            current_sum += num
            count += prefix_sums.get(current_sum - k, 0)
            prefix_sums[current_sum] += 1

        return count
