"""
    @script-author: amandeepsinghkhanna
    @script-description: Implementation of a K-Means clustering without any external modules.
"""
# importing the required modules:
from random import randint
from math import sqrt

# input dataset:
input_data = [
    [999.8782584, 1000.025132, 1000.233395, 1000.01924, 1001.87767],
    [999.6786528, 998.2874488, 998.8671357, 1001.141482, 999.4658219],
    [1000.206903, 1002.01986, 1000.752424, 1000.544795, 1000.311535],
    [999.1880532, 1000.080679, 1000.206278, 998.5206341, 998.7200636],
    [1000.892012, 1001.228377, 1000.270908, 999.5543396, 1001.457997],
    [999.2132189, 999.9011948, 1000.792213, 1001.820608, 999.8832664],
    [1001.454687, 998.9090088, 1000.784698, 1002.968736, 999.8434203],
    [1000.647153, 1001.033434, 999.5407802, 999.8713963, 998.7603223],
    [999.9784643, 999.6281201, 1001.500016, 1000.122358, 1000.204403],
    [1000.151161, 1000.699065, 999.0520405, 999.0642004, 998.9016283],
]
print("The input dataset is {}".format(input_data))

# setting the k value for clustering:
k = 3
print("The chosen K value is {}".format(k))

# setting the number of iterations:
iterations = 1

# generating cluster centeroids:
centeroid_indices = []
while len(centeroid_indices) != k:
    r_int = randint(0,len(input_data)-1)
    if r_int not in centeroid_indices:
        centeroid_indices.append(r_int)        
print("The randomly chosen centeroid_indices are - {}".format(centeroid_indices))

centeroid_rows = [input_data[i] for i in centeroid_indices]

# user-defined function to compute cluster averages:
def compute_avg(clusters):
    centeroids = []
    for cluster_label in clusters.keys():
        centeroid = []
        for col_index in range(len(clusters[cluster_label][0])):
            total = 0
            for row_val in clusters[cluster_label]:
                total += row_val[col_index]
            centeroid.append(total/len(row_val))
        centeroids.append(centeroid)
    return centeroids

# user-defined function to compute differences:
def compute_clusters(input_data, centeroids):
    clusters = {}
    for input_row in input_data:
        distances = []
        for centeroid_row in centeroids:
            distance = 0
            for column in range(len(input_row)):
                distance += (input_row[column] - centeroid_row[column])**2
            distances.append(sqrt(distance))
        if str(distances.index(min(distances))) in clusters.keys():
            clusters[str(distances.index(min(distances)))].append(input_row)
        else:
            clusters[str(distances.index(min(distances)))] = [input_row]
    return clusters

# user-defined function to implement knn:
def implement_knn(iterations, input_data, centeroids):
    for iteration_val in range(iterations):
            print("iteration {} of {}".format(iteration_val, iterations-1))
            clusters = compute_clusters(input_data, centeroid_rows)
            print(clusters)
            centeroids = compute_avg(clusters)
            print(centeroids)
    return {'cluster_info': clusters, 'centeroid_info': centeroids}

iterations = 10
implement_knn(iterations, input_data, centeroid_rows)