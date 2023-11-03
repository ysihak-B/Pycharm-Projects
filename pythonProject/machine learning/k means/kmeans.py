import random
import math


class Kmeans:
    def __init__(self, filename, k):
        self.k = k
        self.filename = filename
        self.datapoints = {}
        self.clusters = {}
        self.centroids = []
        file = open(filename, 'r')
        lines = file.readlines()
        for line in lines:
            line = line.split(' ')
            key = line[0]
            x = int(line[1])
            y = int(line[2])
            point = (x, y)
            self.datapoints[key] = point

    def kmeans(self):
        # initialization step
        # randomly selecting k centroids form the given observations
        self.centroids = random.choices(list(self.datapoints.values()), weights=None, cum_weights=None, k=self.k)

        change = True
        while change:
            # assignment step: assigning each observation to the center which is closest to it
            for point in self.datapoints.values():
                sht_dis = math.inf
                index = 0
                for center in self.centroids:
                    dis = math.sqrt(((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2))
                    if dis < sht_dis:
                        sht_dis = dis
                        index = self.centroids.index(center)
                self.clusters[point] = index
            # update step: recalculating centroids
            for j in range(self.k):
                count = 0
                x = 0
                y = 0
                for cluster in self.clusters:
                    if self.clusters[cluster] == j:
                        x += int(cluster[0])
                        y += int(cluster[1])
                        count += 1
                if count == 0:
                    self.centroids = random.choices(list(self.datapoints.values()),
                                                    weights=None, cum_weights=None, k=self.k)
                else:
                    prev = self.centroids[j]
                    self.centroids[j] = (int(x / count), int(y / count))
                    if prev == self.centroids[j]:
                        change = False
                    else:
                        change = True
        return self.clusters
