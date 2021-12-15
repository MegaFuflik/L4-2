def is_monotonic(nums1):
    if nums1 == sorted(nums1): 
        return (True)
    else:
        if nums1 == sorted(nums1, reverse=True): 
            return (True)
        else:
            return (False)
            

if __name__ == "__main__":    
    print("example 1", is_monotonic([1,2,2,3]))
    print("example 2", is_monotonic([6,5,4,4]))
    print("example 3", is_monotonic([1,3,2]))
    print("example 4", is_monotonic([1,2,4,5]))
    print("example 5", is_monotonic([1,1,1]))