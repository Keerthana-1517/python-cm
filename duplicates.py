def has_duplicates(lst):
    #use a set to track seen elements
    seen=set()
    for item in lst:
        if item in seen: #if the item is already in the set, it's a duplicate
           return True
        seen.add(item) #add the item to the set
    return False #no duplicates found
#Example usage:
print(has_duplicates([1,2,3,4,5])) #False
print(has_duplicates([1,2,3,4,2])) #True
print(has_duplicates([]))          #False(empty list has no duplicates)
print(has_duplicates([1]))         #False(single element has no duplicates)
