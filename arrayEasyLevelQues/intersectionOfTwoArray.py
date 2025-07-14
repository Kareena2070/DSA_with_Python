# Intersection of two sorted arrays
a = [1, 2, 2, 3, 3, 4, 5, 6]
b = [2, 3, 3, 5, 6, 6, 7]


# brute froce solution 

def intersection(a, b):
    n1 = len(a)
    n2 = len(b)
    ans = []
    visted = [0] * n2
    for i in range(n1):
        for j in range(n2):
            if a[i] ==b[j] and visted[j] ==0:
                ans.append(a[i])
                visted[j] =1
                break
            if b[j]>a[i]:
                break
    return ans

print(intersection(a, b))


# Time complexity 
# as here 2 loop running one outer and one inner so time complexity O(n1*n2)
# space complexity is O(n2) beacuse each index in of both loop 
