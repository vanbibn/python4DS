# Remove non-significant predictors
df_new = df_clean.drop(["cylinders","horsepower"], axis=1)

# 3) Prepare the following dataframes.

from sklearn.model_selection import train_test_split

# a) Create a dataframe called "response_new" including only the column "mpg".
response_new = df_new[['mpg']]

# b) Create a dataframe called "features_new" with the remaining columns.
features_new = df_new.iloc[:,1:]


# c) Prepare a dataframe named "features_train_new": random 80% rows of the dataframe "features_new"
# d) Prepare a dataframe named "features_test_new": random 20% rows of the dataframe "features_new"
# e) Prepare a dataframe named "response_train_new": random 80% rows of the dataframe "response_new"
# f) Prepare a dataframe named "response_test_new": random 20% rows of the dataframe "response_new"

result_list_new = train_test_split(features_new, response_new, test_size=0.2, random_state=64)

features_train_new, features_test_new, response_train_new, response_test_new = result_list_new

print("full df_new:", df_new.shape)
print("features_train_new:", features_train_new.shape)
print("features_test_new:", features_test_new.shape)
print("response_train_new:", response_train_new.shape)
print("response_test_new:", response_test_new.shape)

# 4) Create a multiple linear regressoin model from scikit learn package. 
# Train the model using the train data created above.

from sklearn.linear_model import LinearRegression
mlr_new = LinearRegression()
mlr_new.fit(features_train_new, response_train_new)

# 5) Produce predictions over the test data.

response_pred_new = mlr_new.predict(features_test_new)


# 6) Evaluate the model performance over the test data by tabulating metrics of Mean Absolute Error, Mean Squared Error and Root Mean Squared Error.

import matplotlib.pyplot as plt
plt.figure(figsize=(7, 6))
plt.scatter(response_test_new, response_pred_new)
plt.ylabel('Predicted MPG', size = 12)
plt.xlabel('Actual MPG', size = 12)
plt.show()