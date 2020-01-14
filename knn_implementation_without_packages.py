"""
    @script-author: amandeepsinghkhanna
    @script-description: Implementation of KNN algorithm without using any exteranl package/module.
    @script-python-version: Python 3.x
"""
# importing the required modules/packages:
import math # for mathematical functions.

# importing the training dataset:
train_data = [
    [40, 174, 63, 5.70, 69],
    [50, 126, 73, 5.00, 66],
    [32, 140, 72, 5.30, 85],
    [48, 123, 64, 6.10, 88],
    [28, 132, 74, 4.60, 83],
    [27, 178, 74, 5.20, 82],
    [26, 148, 77, 6.00, 88],
    [23, 120, 68, 5.80, 75],
    [38, 177, 73, 4.50, 70],
    [29, 101, 72, 6.30, 88]
]
print("The training dataset is {}".format(train_data)) # printing the training dataset

# importing the test dataset
test_data = [
   [50, 130, 70, 5.00],
   [45, 110, 68, 5.50],
   [30, 100, 50, 6.00]
]
print("The test dataset is {}".format(test_data))

# setting the value of k:
k = 1
print("The k value is {}".format(k))


for test_row in test_data: # for each row of test_data
    distance_column = []   # declaring an empty list for capturing the distances of each training row.
    for train_row in train_data: # for each row in train_data
        distance = 0 # initiallizing distance as zero.
        for column in range(len(train_row)-1): # for each element in each row in train_data
            difference = (train_row[column]-test_row[column])**2 # computing the difference and squaring it.
            distance = distance + difference # incrementing the value of distance.
        distance = math.sqrt(distance) # taking square root of the distances.
        distance_column.append(distance) # adding the computed distance to the distance_column list.
    distance_column_copy = distance_column.copy() # creating a copy of the distance_column to preserve the original indices.
    distance_column_copy.sort() # sorting the indices in the ascending order.
    distance_indices = [distance_column.index(index_val) for index_val in distance_column_copy]
    distance_indices = distance_indices[0:k]
    prediction = sum([train_data[i][len(train_data[i])-1] for i in distance_indices])/k
    print("The prediction for the test_row - {} is {}".format(test_row, prediction))
    # print(test_row)
    # print(prediction)