grade_book = 	[[100, 80, 93, 89],
			 	 [85, 80, 90, 83],
			 	 [70, 91, 88, 82]]
			 
averages = []
for row in grade_book:
	total = 0
	for grade in row:
		total += grade 
	average = total / 4.0
	averages.append(average)
print(averages)

#________

total = 0
counter = 0
Newaverages = []
for row in grade_book:
	for grade in row:
		total += grade 
		counter += 1
	average = total / float(counter)
	Newaverages.append(average)
print(Newaverages[-1])
	
	
		
		
			 