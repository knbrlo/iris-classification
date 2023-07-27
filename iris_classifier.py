from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

# Split the data into a training set and test set
# Random state at 42 is always the right number :)
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

# Train a classifier using the training data.
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Test the classifier with the test data and print accuracy.
predictions = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

