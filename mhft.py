import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def load_mental_health_data():
    data = pd.read_csv('mental_health_data.csv')
    data.dropna(inplace=True)
    return data

def train_linear_regression_model(data):
    X = data[['year', 'country', 'sex', 'age', 'suicides_no']]
    y = data['suicides_no']
    X = pd.get_dummies(X)
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_mental_health_score(model, year, country, sex, age):
    user_inputs = pd.DataFrame({
        'year': [year],
        'country': [country],
        'sex': [sex],
        'age': [age],
        'suicides_no': [0]  
    })
    user_inputs = pd.get_dummies(user_inputs)
    predicted_score = model.predict(user_inputs)
    return predicted_score[0]

if __name__ == '__main__':
    data = load_mental_health_data()
    model = train_linear_regression_model(data)
    predicted_score = predict_mental_health_score(model, 2020, 'United States', 'male', '35-54 years')
    print(f"Predicted Mental Health Score: {predicted_score}")
