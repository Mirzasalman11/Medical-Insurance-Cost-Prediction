import joblib
import pandas as pd
import argparse

# Load your encoder and model
loaded_model = joblib.load('C:/salman/ML/Medical Insurance Cost Prediction/model.joblib')


def predict_heart_disease(args):
    # Create a DataFrame from the input data
    input_df = pd.DataFrame([(args.age, args.sex, args.bmi, args.children, args.smoker, args.region)],
                            columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

    # Encoding steps
    # encoding 'sex' column
    input_df.replace({'sex': {'male': 0, 'female': 1}}, inplace=True)

    # encoding 'smoker' column
    input_df.replace({'smoker': {'yes': 0, 'no': 1}}, inplace=True)

    # encoding 'region' column
    input_df.replace({'region': {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}}, inplace=True)

    # Make predictions
    pred = loaded_model.predict(input_df)
    return pred[0]

if __name__ == "__main__":
    # Set up argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description='Heart Disease Prediction')
    parser.add_argument('--age', type=float, required=True)
    parser.add_argument('--sex', type=str, choices=['male', 'female'], required=True)
    parser.add_argument('--bmi', type=float, required=True)
    parser.add_argument('--children', type=int, required=True)
    parser.add_argument('--smoker', type=str, choices=['yes', 'no'], required=True)
    parser.add_argument('--region', type=str, choices=['southeast', 'southwest', 'northeast', 'northwest'], required=True)

    args = parser.parse_args()

    # Call the predict_heart_disease function with the parsed arguments
    prediction = predict_heart_disease(args)

print( f'charges is {prediction}')

