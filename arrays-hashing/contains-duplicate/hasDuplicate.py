def hasDuplicate(nums):
    mySet = set()

    for num in nums:
        # If num is in the set, return True
        if num in mySet:
            return True
        # Otherwise add num to set, then proceed to next element
        else:
            mySet.add(num)

    return False