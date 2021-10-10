import shutil
columns = shutil.get_terminal_size().columns

#smallest drop!

def Selection():
	for i in range(n-1):
		minimum = i
		for j in range(i+1, n):
			if array[minimum] > array[j]:
				minimum = j
		array[i],array[minimum] = array[minimum],array[i]

	return array

if __name__=="__main__":
	print("SELECTION SORT".center(columns))
	while True:		
		array = input("\nInput numbers separated by commas: ").split(",")
		array = [int(x) for x in array]

		n = len(array)
		print(Selection())

		ask = input("\nWanna Continue? [y/n]: ").lower()
		if ask == "y":
			continue
		elif ask == "n":
			exit()




