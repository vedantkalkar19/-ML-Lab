#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris, load_breast_cancer, load_digits, load_wine
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load datasets
datasets = [load_iris(), load_breast_cancer(), load_digits(), load_wine()]

# Define parameter grids for GridSearchCV
param_grid_rf = {'n_estimators': [50, 100, 200], 'max_depth': [3, 5, None]}
param_grid_ab = {'n_estimators': [50, 100, 200], 'learning_rate': [0.01, 0.1, 1.0]}

# Define ensemble learning models
models = [RandomForestClassifier(), AdaBoostClassifier()]

for i, dataset in enumerate(datasets):
    print(f'Dataset {i+1}: {dataset["DESCR"][:50]}...')
    X, y = dataset['data'], dataset['target']
    
    for j in range(4):
        print(f'Train-Test Split {j+1}:')
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=j)
        
        # Define preprocessing steps and ensemble learning pipeline
        steps = [('scaler', StandardScaler()), ('model', models[j%2])]
        pipeline = Pipeline(steps=steps)
        
        # Define parameter grid for GridSearchCV
        # Define parameter grid for GridSearchCV
        if j % 2 == 0:
            param_grid = {'model__n_estimators': [50, 100, 200], 'model__max_depth': [3, 5, None]}
        else:
            param_grid = {'model__n_estimators': [50, 100, 200], 'model__learning_rate': [0.01, 0.1, 1.0]}

            
        # Find best hyperparameters using GridSearchCV
        grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1, verbose=1)
        grid_search.fit(X_train, y_train)
        
        # Evaluate performance using cross-validation
        cv_scores = cross_val_score(grid_search.best_estimator_, X_train, y_train, cv=5, n_jobs=-1)
        print(f'CV Scores: {cv_scores}')
        print(f'CV Mean Score: {cv_scores.mean()}')
        
        # Evaluate performance on test set
        y_pred = grid_search.predict(X_test)
        test_score = accuracy_score(y_test, y_pred)
        print(f'Test Score: {test_score}')
        
        print('-'*50)


# In[ ]:


from sklearn.datasets import load_breast_cancer, load_iris, load_wine, load_digits
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Define the list of datasets
datasets = [load_breast_cancer(), load_iris(), load_wine(), load_digits()]

# Define the list of classifiers
classifiers = [
    RandomForestClassifier(),
    GradientBoostingClassifier(),
    LogisticRegression(solver='liblinear')
]

# Define the parameter grid for each classifier
param_grids = [
    {'model__n_estimators': [50, 100, 200], 'model__max_depth': [3, 5, None]},
    {'model__n_estimators': [50, 100, 200], 'model__learning_rate': [0.01, 0.1, 1.0]},
    {'model__penalty': ['l1', 'l2'], 'model__C': [0.1, 1, 10]}
]

# Loop over the datasets and classifiers
for i, dataset in enumerate(datasets):
    X, y = dataset.data, dataset.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    for j, clf in enumerate(classifiers):
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('model', clf)
        ])

        # Define parameter grid for GridSearchCV
        param_grid = param_grids[j]
        
        # Perform GridSearchCV to find the best hyperparameters
        grid_search = GridSearchCV(pipeline, param_grid=param_grid, cv=5)
        grid_search.fit(X_train, y_train)
        
        # Evaluate the model on the test set
        y_pred = grid_search.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        
        print(f"Dataset {i+1}, Classifier {j+1}, Best params: {grid_search.best_params_}, Test accuracy: {acc:.3f}")


# In[ ]:


from sklearn.datasets import load_breast_cancer, load_iris, load_wine, load_digits
from sklearn.decomposition import PCA, NMF, FastICA, KernelPCA, TruncatedSVD, SparsePCA
import matplotlib.pyplot as plt

# Define the list of datasets
datasets = [load_breast_cancer(), load_iris(), load_wine(), load_digits()]

# Define the list of dimensionality reduction techniques
drc = [
    PCA(n_components=2),
    NMF(n_components=2),
    FastICA(n_components=2),
    KernelPCA(n_components=2, kernel='rbf'),
    TruncatedSVD(n_components=2),
    SparsePCA(n_components=2, alpha=1)
]

# Loop over the datasets and dimensionality reduction techniques
for i, dataset in enumerate(datasets):
    X, y = dataset.data, dataset.target
    
    plt.figure(figsize=(20, 5))
    plt.suptitle(f"Dataset {i+1}: {dataset.DESCR.splitlines()[0]}")
    
    for j, dr in enumerate(drc):
        # Perform dimensionality reduction
        X_dr = dr.fit_transform(X)
        
        # Plot the reduced data
        plt.subplot(1, 6, j+1)
        plt.scatter(X_dr[:, 0], X_dr[:, 1], c=y, cmap='viridis')
        plt.title(type(dr).__name__)
        
    plt.show()


# In[ ]:




