# Amazon Fine Foods Review Sentimental Analysis

## Abstract
This project utilizes Natural Language Processing (NLP) techniques to analyze user sentiment from the Amazon Fine Foods Review dataset. Techniques such as Simple Neural Networks, Convolutional Neural Networks (CNN), Long Short-Term Memory (LSTM) networks, and a hybrid CNN-LSTM approach are implemented to classify reviews into sentiment categories. The study reveals that the LSTM and CNN-LSTM models demonstrate superior accuracy in classifying user sentiments.

## Introduction
With the rise of online shopping, user-generated content like product reviews has become a goldmine for consumer sentiment analysis. This project taps into over 500,000 reviews from the Amazon Fine Foods Review dataset to explore relationships between textual reviews and user satisfaction, categorized into 'satisfied' and 'unsatisfied' sentiments. This effort aims to offer insights into consumer behavior and product quality through advanced text classification methods.

## Dataset
The Amazon Fine Foods Review dataset from Kaggle(https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews/data) includes over 500,000 user reviews, scored from 1 to 5. For this analysis, scores are simplified into two classes:

Unsatisfied (1-2)
Satisfied (4-5)
To address class imbalance, 10,000 records from each score category are selected to form a balanced training set.


## Conclusion:
In this project, we set out to analyze the Amazon Fine Foods Review dataset to classify user reviews based on their content. Our approach was grounded in the use of three Natural Language Processing (NLP) techniques—Simple Neural Networks, Convolutional Neural Networks (CNN), and Long Short-Term Memory (LSTM) networks. The rationale behind selecting these methods lies in their proven effectiveness in parsing and interpreting complex sequence data such as text. The LSTM network, particularly when enhanced with bi-directional capabilities and attention mechanisms, demonstrated the highest accuracy, reaching 82.64% post 70 epochs. However, the CNN-LSTM hybrid model outperformed this, achieving an accuracy of 84.03% within just two epochs, albeit with signs of overfitting after the fourth epoch. While more complex models like the CNN-LSTM can lead to rapid and significant improvements in accuracy, they also require careful tuning to avoid overfitting. This balance is crucial in the development of effective NLP systems for sentiment analysis.
Adding to our future trajectory, we envisage the adoption of more sophisticated embedding methodologies and attention mechanisms, with an eye toward the potential of transformer models. The transformer architecture, known for its exceptional ability to handle long-range dependencies within text, presents an exciting frontier for further enhancing the accuracy and depth of sentiment analysis. This evolution in model complexity will unlock new dimensions in NLP's application to voluminous and complex datasets.
