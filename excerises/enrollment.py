def enrollment_stats(list_of_universities):
	total_students = []
	total_tution = []
	for university in list_of_universities:
		total_students = university.append[0]
		total_tution = university.append[1]
	return total_students, total_tution

def mean(my_list):
	list_sum = 0
	for i in range(len(my_list)):
		list_sum += float(my_list[i])
	return int(list_sum / len(my_list))


def median(my_list):
	sorts = sorted(my_list)
    length = len(sorts)
    if not length % 2:
        return (sorts[int(length / 2)] + sorts[int(length / 2 - 1)]) / 2.0
    return sorts[int(length / 2)]


if __name__ == '__main__':

    universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500],
    ]

    totals = enrollment_stats(universities)

    print(totals[0])

    print("\n")
    print("*****" * 5)
    print("Total students:   {}".format(sum(totals[0])))
    print("Total tuition:  $ {}".format(sum(totals[1])))
    print("\nStudent mean:     {}".format(mean(totals[0])))
    print("Student median:   {}".format(median(totals[0])))
    print("\nTuition mean:   $ {}".format(mean(totals[1])))
    print("Tuition median: $ {}".format(median(totals[1])))
    print("*****" * 5)
    print("\n")