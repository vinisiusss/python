def bub(nums):
    swapped = True
    while swapped:
        swapped = False

        for i in range(len(nums)- 1):
            if nums[i]>nums[i+1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

bube=[3,4,5,10,2,5,8,4]
bub(bube)
print(bube)
