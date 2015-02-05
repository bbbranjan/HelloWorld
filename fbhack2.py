arr = [1,0,0,1,0,0, 1]
count_index = []
count_values = []
sum1 = 0
ct0 = ct1 = 0
sum1 = sum(arr)
diff = 0
for i in range(1,len(arr)):
    for j in range(0,i):
        arr_temp = arr[j:i]
        ct0 = ct1 = 0
        for k in range(0,len(arr_temp)):
            if (arr_temp[k] == 0):
                ct0 += 1
            else:
                ct1 +=1

        
        if(ct0 - ct1 > diff):
            diff = ct0 - ct1


result = sum1 + diff
print(result)
#return result
