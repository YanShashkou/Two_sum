def two_sum(nums, target):
    hash = {

    }

    for i in range(len(nums)):
        need =  target - nums[i]
        if need in hash:
            print (hash[need],i)
        else:
            hash[nums[i]] = i


two_sum([3,2,4],6)