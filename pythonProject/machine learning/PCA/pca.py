# Import necessary libraries
from sklearn import datasets  # to retrieve the iris Dataset
import pandas as pd  # to load the dataframe
from sklearn.preprocessing import StandardScaler  # to standardize the features
from sklearn.decomposition import PCA  # to apply PCA
import matplotlib.pyplot as plt

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
scaled_data = pd.DataFrame(scalar.fit_transform(iris_data))  # scaling the data scaled_data

# Applying PCA
# Taking no. of Principal Components/ Dimensions as 2
pca = PCA(n_components=2)
data_pca = pca.fit_transform(scaled_data)
print('covariance matrix')
print(pca.get_covariance())
print('eigen vectors of the 2-D')
print(pca.components_)
print('eigen values of the 2-D')
print(pca.explained_variance_)

# scatter plot to project the reduced data.
plt.title("Dimension Reduction using PCA")
plt.scatter(data_pca[:, 0], data_pca[:, 1])
plt.xlabel('PC1')
plt.ylabel('PC2')

plt.show()

# the iris dataset after reduction
data_pca = pd.DataFrame(data_pca, columns=['PC1', 'PC2'])
print('************************ Reduced data to 2-Dimensions **********************')
print(data_pca)