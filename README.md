# House Sales Project

This repository contains the work for the House Sales Data Analysis and Prediction Project, completed as part of a Data Analyst course. The project involves analyzing and predicting house prices in King County, USA, using a dataset with various features such as square footage, number of bedrooms, and number of floors.

## Project Structure

The project is organized into the following folders:

- **data**: Contains the dataset files used for the project.
- **notebooks**: Contains the Jupyter notebooks for various tasks and steps.
- **.venv**: The virtual environment for Python dependencies.

## Tasks Completed

1. **Data Loading**:
   - Loaded the cleaned dataset from a CSV file.
   
2. **Data Cleaning**:
   - Dropped irrelevant columns (`id`, `Unnamed: 0`) and handled missing values.

3. **Exploratory Data Analysis (EDA)**:
   - Displayed data types of each column using the `dtypes` attribute.
   - Generated a statistical summary of the data using the `describe()` method.
   - Counted the number of houses with unique floor values using the `value_counts()` method.
   - Created visualizations using Seaborn:
     - Boxplot to analyze waterfront views and price outliers.
     - Regplot to analyze the correlation between `sqft_above` and price.

4. **Modeling**:
   - Built a Linear Regression model to predict house prices based on features like `sqft_living`.
   - Built another Linear Regression model using multiple features and evaluated the R² score.
   - Created a pipeline for scaling data, applying polynomial features, and fitting a Linear Regression model.
   - Applied Ridge regression with regularization and evaluated the model performance.
   - Performed a second-order polynomial transformation and used Ridge regression to improve predictions.

## Requirements

To run the code in this repository, you need to install the following Python packages:

```bash
pip install -r requirements.txt
