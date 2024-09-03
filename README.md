# NASA Nearest Earth Objects (1910-2024) Dataset

## Overview

This dataset contains comprehensive observations of Near-Earth Objects (NEOs) recorded by NASA from the years 1910 to 2024. NEOs are asteroids or comets with orbits that bring them close to Earth's vicinity. Some of these objects pose potential hazards to our planet, and NASA classifies them accordingly under the `is_hazardous` label.

With **338,199 records**, this dataset offers an extensive historical and predictive view of NEOs, providing crucial information that can help us understand which objects might pose a danger to Earth. Your task is to leverage this data to build a classification model that can predict whether a given NEO is hazardous or not. This is vital as accurate predictions could help in preparedness for potential asteroid impacts.

## Dataset Description

- **Total Records:** 338,199
- **Time Frame:** 1910 - 2024
- **Objective:** Predict whether a NEO is hazardous using various features in the dataset.

## Features

The dataset includes the following features:

1. **Object ID:** Unique identifier for each NEO.
2. **Name:** Name of the NEO.
3. **Diameter (km):** Estimated diameter of the NEO in kilometers.
4. **Magnitude:** Absolute magnitude (brightness) of the NEO.
5. **Miss Distance (au):** Minimum distance of the NEO from Earth in astronomical units (au).
6. **Orbit Class:** Classification of the NEO's orbit.
7. **Discovery Date:** Date when the NEO was first observed.
8. **Speed (km/s):** Velocity of the NEO in kilometers per second.
9. **Is Hazardous (Target):** Binary classification target where:
   - `1` indicates the NEO is hazardous.
   - `0` indicates the NEO is not hazardous.

## Goal

The primary goal is to accurately predict the `is_hazardous` label using supervised learning techniques. This binary classification task is critical as it directly relates to the potential threat posed by these NEOs.

## Tools and Techniques

To tackle this problem, you may consider the following approaches:

- **Data Preprocessing:** Handling missing values, feature scaling, and feature engineering.
- **Exploratory Data Analysis (EDA):** Understanding the distribution of features and their relationship with the target variable.
- **Model Selection:** Implementing various classification algorithms such as Logistic Regression, Decision Trees, Random Forests, Gradient Boosting, or even Neural Networks.
- **Model Evaluation:** Using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC to evaluate the performance of the models.

## Importance

Accurate prediction of hazardous NEOs is not just a computational challenge but a critical component in planetary defense. Your contributions could inform NASA's decision-making and preparedness for potential asteroid impacts, ensuring that humanity is better equipped to handle these celestial threats.

## How to Use

1. **Data Preparation:** Load the dataset and perform necessary preprocessing steps.
2. **Model Training:** Train your classification model using the training data.
3. **Model Evaluation:** Evaluate your model's performance on the test set using appropriate metrics.
4. **Prediction:** Use the trained model to predict the `is_hazardous` label for new NEO observations.

## Conclusion

This dataset offers a rich source of information for building predictive models that can play a pivotal role in ensuring Earth's safety from potential NEO impacts. We encourage you to apply your data science and machine learning skills to develop the most accurate predictive model possible.

Good luck, and let's ensure we're ready for any asteroid attack!

