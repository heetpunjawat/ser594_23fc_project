#### SER594: Machine Learning Evaluation
#### (title) MotoViz: Mapping Motorcycle Crash Data 
#### (author) Heet Punjawat
#### (date) 11/20/2023

## Evaluation Metrics
### Metric 1
**Name:** Accuracy
**Choice Justification:** Accuracy is a suitable metric for classification problems like predicting traffic accident severity, as it measures the overall correctness of predictions. In this project, the distribution of crashes across different types are not be heavily skewed, making accuracy a relevant metric.
**Interpretation:** The model achieved 100% accuracy, indicating that all predictions were correct.

### Metric 2
**Name:** F1-score
**Choice Justification:** F1-score is a good metric for datasets, providing a balance between precision and recall. F1-score is well-suited for multiclass problems, offering a comprehensive evaluation of the model's performance across all classes. It's appropriate for evaluating this model's ability to predict different severity classes.
**Interpretation:** The F1-score of 1.00 suggests a perfect balance between precision and recall for all severity classes.

## Alternative Models
### Alternative 1: Tuned Random Forest Model
**Construction:** This model was constructed by tuning hyperparameters (number of estimators and max depth) using a grid search.
**Evaluation:** The tuned random forest model performed equally well compared to the basic Random Forest Model, by computing accuracy and F1-score for each target column.

### Alternative 2: Gradient Boosting Model
**Construction:** The Gradient Boosting Model was constructed using the GradientBoostingClassifier from scikit-learn. The construction involves training an ensemble of weak learners sequentially, with each learner correcting the errors of its predecessor.
**Evaluation:** I was not able to evaluate the metrics properly for this model, but, The Gradient Boosting Model's performance can be evaluated similarly to the Random Forest Model, computing accuracy and F1-score for each target column.

### Alternative 3: Feature Subset Model
**Construction:** The Feature Subset Model involves selecting a subset of features to train the Random Forest Model. This can be achieved by choosing a subset of columns from the feature set X_train.
**Evaluation:** I was not able to evaluate the metrics properly for this model, but, The Feature Subset Model's performance can be evaluated similarly to the Random Forest Model, computing accuracy and F1-score for each target column.

## Best Model

**Model:** Random Forest Model
In summary, the Random Forest Model without hyperparameter tuning performed equally well as the tuned version for all severity classes. This model is considered the best-performing one for predicting traffic accident severity.
