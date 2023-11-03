import matplotlib.pyplot as plt
import kmeans

k_means = kmeans.Kmeans('observations', 2)
point = k_means.datapoints.values()
clusters = k_means.kmeans()
print(k_means.centroids)
print(k_means.clusters)
plt.title("K means clustering")
plt.rcParams["figure.figsize"] = [7, 3]
plt.rcParams["figure.autolayout"] = True

plt.axis([0, 70, 0, 80])

for center in k_means.centroids:
    plt.plot(center[0], center[1], '*', color='black')
    plt.text(center[0], center[1] + 0.5, '({}, {})'.format(center[0], center[1]))
for data in clusters:
    if clusters[data] == 0:
        plt.plot(int(data[0]), int(data[1]), 'r*')
        # plt.text(int(data[0]), int(data[1]) + 0.5, '({}, {})'.format(int(data[0]), int(data[1])))
    elif clusters[data] == 1:
        plt.plot(int(data[0]), int(data[1]), 'b*')
        # plt.text(int(data[0]), int(data[1]) + 0.5, '({}, {})'.format(int(data[0]), int(data[1])))


plt.show()
