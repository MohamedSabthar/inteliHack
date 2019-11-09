import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # get directory root
model_dir = os.path.join(BASE_DIR, "model")  # get image directory path

# input output mapping
tf = {'Yes': 1, 'No': 0}
sec = {'A': 1, 'B': 2 ,'C': 3}
gen = {'Male': 1, 'Female': 0}

grade = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}

model = joblib.load(f'{model_dir}/predict-marks.joblib')     # load the model
print('''Input Data to predict 
      Input parameters ( No. of days attended, Semester/Term, Attending Private Classes, Group/Section of the Class ,Gender )
      No. of days attended      [0-60] (integer)
      Semester/Term             {1,2,3} (choose one form the set)
      Attending Private Classes Yes|No
      Section of the Class      {A,B,C}
      Gender                    Male|Female
      
      ''')

days, sem, tution, section, gender = input('Enter the input parameters Ex-(50 2 Yes A Female) : ').strip().split(' ')     # get the input parameters
days = int(days)
sem = int(sem)
prediction = model.predict([[days, sem, tf[tution], sec[section], gen[gender]]])  # passing the parameter for prediction

print(f'Expected grade for the parameters is "{grade[prediction[0]]}"')   # prediction output
