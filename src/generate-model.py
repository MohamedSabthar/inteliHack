import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz

grade_data = pd.read_csv('student_dataset.csv')      # loading data frame
x = grade_data.drop(columns=['Grade'])    # input data set
y = grade_data['Grade']                   # output data set


model = DecisionTreeClassifier()    # using decisionTreeClassifier to make model
print(model)
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.2)     # split data to testing and training
model.fit(x_train, y_train)         # passing training data to the model


prediction = model.predict(x_test)  # get the predicted output
score = accuracy_score(y_test,prediction)   # compare the prediction against original output
print(score)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # get directory root
model_dir = os.path.join(BASE_DIR, "model")  # get image directory path

export_graphviz(model, out_file=f'{model_dir}/graph.dot',
                feature_names=['Attendace', 'Gender', 'Term', 'Tuition', 'Class'],
                class_names=list(map(str, sorted(y.unique()))),
                label='all',
                rounded=True,
                filled=True)    # export decision tree

joblib.dump(model, f'{model_dir}/predict-marks.joblib')  # export model as predict-marks.joblib
