# Malaria-outbreak-prediction-using-ML-models-ARIMA-and-Regression.

AIM: 
To provide an enhanced prediction for malaria outbreaks in a region by using efficient machine learning models that output the probability estimates for malaria occurrence in a region based on the geographical data and statistical records.

IMPLEMENTATION:
The dataset is formed by collecting the most prominent factors pertaining to epidemic outbreaks such as maximum and minimum temperature, rainfall etc and also number of death cases reported.
The data are collected from various Government databases on Meteorological information.
The data is cleaned i.e. missing values are filled, values are normalized, all features are transformed to same metrics for the ease of evaluation.
The data is given as input to Support Vector Machine (SVM) based classification and the output is visualized in the form of Confusion Matrix.
Confusion Matrix is used to evaluate the quality of the output of a classifier here in our case SVM’s output. 
The diagonal elements represent the number of points for which the predicted label is equal to the true label, while off-diagonal elements are those that are mislabeled by the classifier. The higher the diagonal values of the confusion matrix the better, indicating many correct predictions by the model.
To improve the output of the SVM classifier, we have used Genetic Algorithm for selecting the best features that contribute in making the predictions accurate.
The Genetic Algorithm is used to create the population and the fittest population is chosen based on the fitness score calculated. The fittest population that survives with the highest fitness score after many generations will give you the features that will contribute in improving the output of the SVM classifier.

EVALUATION METRIC:
The final output was evaluated based on predictive(classification accuracy), robustness of the model, speed and scalability of the system.
