# Import necessary libraries
from sklearn import datasets  # to retrieve the iris Dataset
import pandas as pd  # to load the dataframe
from sklearn.preprocessing import StandardScaler  # to standardize the features
from sklearn.decomposition import PCA  # to apply PCA
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import TruncatedSVD

# Load the Dataset
iris = datasets.load_iris()
# convert the dataset into a pandas data frame
iris_data = pd.DataFrame(iris['data'], columns=iris['feature_names'])

# display the head, information and description of the dataset
print(iris_data.info())
print('*********************************************************************')
print(iris_data.describe())
print('*********************************************************************')
print(iris_data.head())
print('*********************************************************************')

# Standardize the features
# Create an object of StandardScaler which is present in sklearn.preprocessing
scalar = StandardScaler()
scaled_data = pd.DataFrame(scalar.fit_transform(iris_data))

# Applying SVD
U, sigma, V = np.linalg.svd(scaled_data)
# print component vectors U, sigma and V
print('component vector U')
print(U)
print('component vector sigma')
print(sigma)
print('component vector V')
print(V)

# Taking no. of Components/ Dimensions as 2
truncated = TruncatedSVD(n_components=2)
truncated_data = truncated.fit_transform(scaled_data)
# scatter plot to project the reduced data.
plt.title("Dimension Reduction using SVD")
plt.scatter(truncated_data[:, 0], truncated_data[:, 1], c='r')
plt.xlabel('PC1')
plt.ylabel('PC2')

plt.show()

# the iris dataset after reduction
truncated_data = pd.DataFrame(truncated_data, columns=['PC1', 'PC2'])
print('************************ Reduced data to 2-Dimensions **********************')
print(truncated_data)
