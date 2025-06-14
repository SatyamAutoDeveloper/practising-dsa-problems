
"""Solution1: This is Brute Force Solution and It is good incase of small array but For Big Length Array, its time complexity will be higher."""
#Time Complexity is O(n^2)
 
class TwoSum:
    def indices_of_two_sum(self, nums, target):
        indices = []
        indix = 0
        try:
            while indices == [] :
                for n in range(len(nums)):
                    if indix == n:
                        continue
                    else:
                        two_sum = nums[indix] + nums[n]
                        if two_sum == target:
                            indices.append(indix)
                            indices.append(n)
                            break
                indix = indix + 1
        except:
            raise IndexError("Two Numbers are not equal to Target")

        return indices


        
"""Solution2: Using Dict/Hash Table, It is efficient in time for big length array"""
class TwoSum:
    def indices_of_two_sum(self, nums, target):
        indices = []
        hash_table = {}
        for n in range(len(nums)):
            res = target - nums[n]
            hash_table[n] = nums[n]
            for key, val in hash_table.items():
                if val == res and key != n:
                    indices.extend([key, n])
                    break
        
        return indices

ts = TwoSum()
indices_arr = ts.indices_of_two_sum([3,0,4,5,1], 6)
print("Indexes of two sum ::", indices_arr)
