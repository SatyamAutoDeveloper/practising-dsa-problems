"""time complexity is O(n * m) and the space complexity is O(min(n, m))"""
"""Where n is list1 and m is list2"""

class MinIndexSumOf2Lists:
    def minIndexSumOf2Lists(self, list1, list2):
        str_list = []
        dict1 = dict()
        for i, val in enumerate(list1):
            if val in list2:
                idx_sum = list2.index(val) + i
                dict1[val] = idx_sum

        for k,v in dict1.items(): 
            if min(dict1.values()) == v:
                str_list.append(k)
        
        return str_list
        

mis = MinIndexSumOf2Lists()
print("Common Strings with Min Index Sum ::",mis.minIndexSumOf2Lists(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
#print("Common Strings with Min Index Sum ::",mis.minIndexSumOf2Lists(["happy","sad","good"], ["sad","happy","good"]))