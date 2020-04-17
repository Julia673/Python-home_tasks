#task 1

def abc():
    x = 1
    y = 2
    str1= "w3resource"
    print("Python Exercises")

print(abc.__code__.co_nlocals)

# task 2
def test(a):
        def add(b):
                nonlocal a
                a += 1
                return a+b
        return add
func= test(4)
print(func(4))

# task 3

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):

    return [num ** 2 for num in nums]

def remove_negatives(nums):

    return [num for num in nums if num > 0]

def choose_func(nums,func1, func2):
     count = 0
     for number in nums:
         if number<0:
             count = 1
     if count==0: 
        nums = square_nums(nums)
        return nums
     else :
        nums = remove_negatives(nums)
        return nums
         
print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))