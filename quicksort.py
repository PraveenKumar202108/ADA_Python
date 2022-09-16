def partion(arr, start, end):
 
  # choosing last element of array as the pivot
  p = arr[end]
  i = start - 1
 
  # comparing each element with pivot
  for j in range(start, end):
    if arr[j] <= p:
      # swaping
      i = i + 1
      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i + 1], arr[end]) = (arr[end], arr[i + 1])
 
  # return the position from where partition is executed
  return i + 1
 
#main quicksort function
def QuickSort(arr, start, end):
  if start < end:
    pivot = partion(arr, start, end)
    QuickSort(arr, start, pivot - 1)
    QuickSort(arr, pivot + 1, end)
 
#the list
nums=[21,56,843,43,65,76,78,3434,1,34,5,7,8]

# Displaying array before sorting
print("Array before Sorting :")
print(nums)
 
#using sort function
n = len(nums)
QuickSort(nums, 0, n - 1)

#Display array after sorting
print('Sorted array :')
print(nums)