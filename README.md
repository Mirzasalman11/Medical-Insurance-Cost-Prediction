# Medical-Insurance-Cost-Prediction

This Python script predicts the medical insurance cost based on various health-related features. It utilizes a pre-trained model to make predictions.

## Dataset

- **Dataset Name**: Medical Insurance dataset
- **Data Source**: Upload on git.
- The dataset contains the following attributes:
  - Feature columns (6): Numerical and categorical values representing health-related features.
  - Target column: Numerical variable representing medical insurance cost.

## Project Structure

- **README.md**: Documentation of the project.
- **main.py**: Python script for making medical insurance cost predictions.
- **model.joblib**: Pre-trained model for medical insurance cost prediction.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Medical-Insurance-Cost-Prediction

2. Create a virtual environment (recommended) and install the required dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows, use: venv\Scripts\activate


## Usage

1. Clone this repository to your local machine.
2. Ensure you have the pre-trained model ('model.joblib') in the same directory as the script ('main.py').
3. Open a command prompt or terminal and navigate to the directory where the script is located.
4. Run the script with the required arguments:
    
    ```bash
    python main.py --age <age> --sex <sex> --bmi <bmi> --children <children> --smoker <smoker> --region <region>

## Example

    ```bash
    #python main.py --age 19, --sex 'female', --bmi 27.900, --children 3, --smoker 'yes', --region 'southwest'

## Model Training
The project uses a pre-trained model to predict medical insurance costs. The model is saved as 'model.joblib'.

## Results
The project provides predictions for medical insurance costs based on the input features.

## Future Improvements
There are several ways to improve the model and the project:

-Explore more advanced machine learning techniques.

-Fine-tune hyperparameters for better model performance.

-Gather more labeled data for improved accuracy.

## References

- Author: Mirza Salman
- Contact: salmansaluu661@gmail.com

Feel free to customize this README to include any additional information you want to provide about the project.

