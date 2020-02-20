
#import subprocess

def printArray(arr):
	n = len(arr) 
	f = open("README.md", "w")
	for i in range(n): 
		print (arr[i]) 
		f.write(arr[i] + "\n")
	print(" ")
	f.close()
	#output = subprocess.run(['git', 'add README.md'])
	#output = subprocess.run(['git', 'commit -F "README.md updated"'])

def partition(arr,low,high): 
	i = ( low-1 )         # index of smaller element 
	pivot = arr[high]     # pivot 
  
	for j in range(low , high): 
		# If current element is smaller than or equal to pivot 
		if   len(arr[j]) <= len(pivot): 
          
			# increment index of smaller element 
			i = i+1 
			arr[i],arr[j] = arr[j],arr[i] 
  
	arr[i+1],arr[high] = arr[high],arr[i+1] 
	printArray(arr)
	return ( i+1 ) 
  
def quickSort(arr,low,high): 
	if low < high: 
  
		# pi is partitioning index, arr[p] is now at right place 
		pi = partition(arr,low,high) 
  
		# Separately sort elements before partition and after partition 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

arr = ["*****", "***", "************", "*************", "**", "*", "****", "*************************", "*********", "*****", "*********", "*******", "**"] 
n = len(arr) 
quickSort(arr,0,n-1) 
