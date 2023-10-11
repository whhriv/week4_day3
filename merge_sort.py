lllist = [18, 7, 21, 50, 36]

def mergesort(lst):
    if len(lst)>1:
        #find midway point of list
        midway = len(lst) // 2
        #split list into left and right
        print('splitting...', lst)
        left_half = lst[:midway]
        right_half = lst[midway:]
        
        #call merge-sort on the left half
        mergesort(left_half)
        mergesort(right_half)
        #merge the left and right half lists back into original list
        
        #index pointers for our lists
        # 3 pointers left, right, main
        l = 0 #left pointer
        r = 0 #right pointer
        m = 0 #main pointer
        
        #while we still have values in left and right
        while l < len(left_half) and r < len(right_half):
            #if the element we are pointing to in the left half is less than the element in the right half
            if left_half[l] < right_half[r]:
                lst[m] = left_half[l]
                #move left half pointer right one spot
                l += 1
            else:
                #place right half value in original list
                lst[m] = right_half[r]
                #move right half pointer one spot
                r += 1
            #either way, always increase main index pointer
            m += 1
            
        #if one of the halfs finish, add the other half to the original list
        while l < len(left_half):
            lst[m] = left_half[l]
            m += 1
        while r < len(right_half):
            lst[m] = right_half[r]
            r += 1
            m += 1
    print('merging...', lst)
    return lst
mergesort(lllist)