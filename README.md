# Iris Classification
This project uses machine learning to classify different species of the Iris flower. It's a great introductory project for those interested in understanding basic principles of machine learning in Python.

# Project Overview
In this project I utilize the Iris flower dataset from scikit-learn's datasets module. The goal of the project is to train a model to distinguish between different species of Iris flowers based on certain features like petal length, petal width, sepal length, and sepal width.

# Technologies Used
- Python 3.9
- Scikit-learn
- Docker

# Getting Started
Here's a step-by-step guide on how to get this project up and running on your local machine for development and testing purposes.

# Prerequisites
Ensure that you have the following installed on your local machine:
Docker

# Installation and Running the Project
Clone the repository to your local machine:

```
git clone https://github.com/knbrlo/iris-classification.git
```

Navigate to your project directory and build the Docker image:
```
cd iris-classification
docker build -t iris-classification .
```

Run the Docker container:

```
docker run -p 3000:80 iris-classification
```

The application will be accessible at http://localhost:3000.

# Testing
Currently, there are no tests set up for this project. As the project grows, I will add unit tests and instructions on how to run them.

# Contributing
I appreciate any contributions you might want to make. Feel free to fork this repository, make your changes, and submit a pull request.

# License
This project is licensed under the MIT License.

# Acknowledgments
The Iris flower dataset is provided by scikit-learn's datasets module.