# discussion sections: 13, drop 2
# homeworks: 14, drop 2
# lecture exercise: 26, drop 4
# midterms: 2
# projects: 3
# final project: 1

# get the data into program
# extract information from a CSV file with all the assignment types and scores
# return a data dictionary, where the keys are assignment groups and values are lists of scores
def get_data():
    pass

# identify and drop the lowest grades for discussion, homework, lecture
# takes a list of scores and drops the lowest number specified
def drop_lowest(list_of_scores, num_to_drop):
    pass

#take the list for all the scores in a single assignment group and returns the group total
def compute_group_total(list_of_scores):
    pass

# adds up total points across categories
# convert from points to percentage
# convert to letter grade
def compute_grade(total_score):
    pass

def test_functions():
    #test drop_lowest
    list1 = [10,9,8,7,6]
    expected_return1 = [10,9,8]
    expected_return1 = [10]

    #test compute_group_total
    list2= [1,1,1,1]
    expected_return3 = 4

    passed = 0
    failed = 0

    if drop_lowest(list1,2)==expected_return1:
        #test passed
        passed += 1
    else:
        #test tailed
        failed += 1
        print("failed test 1")

    if drop_lowest(list1,4)==expected_return2:
        #test passed
        passed += 1
    else:
        #test tailed
        failed += 1
        print("failed test 2")

    if compute_group_total(list2) == expected_return3:
        passed += 1
    else:
        failed += 1
        print("failed test 3")


data_dict = get_data()
# homework_scores = drop_lowest(data_dict['homeworks'],2)
# lecture_scores = drop_lowest(data_dict['lectures'],4)
# discussion_scores = drop_lowest(data_dict['discussion'],2)
# etc for each assignment types
# use compute_group_total for each group, and append those values to a list
# use compute_group_total on the list of group totals to calculate the total_score
# grade = compute_grade(total_score)
# print(grade)
