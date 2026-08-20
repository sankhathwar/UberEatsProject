# Day 3 – Customer Feedback Analysis Using NLP

## Objective

Analyze customer reviews using Natural Language Processing (NLP) to classify sentiment and identify major customer dissatisfaction themes.

---

## 1. Dataset

The `reviews.csv` dataset contains customer feedback associated with orders.

### Columns Used

| Column | Description |
|---|---|
| review_id | Unique review identifier |
| order_id | Associated order |
| customer_id | Customer identifier |
| review_rating | Rating from 1 to 5 |
| review_text | Customer review |
| review_timestamp | Review timestamp |

---

## 2. Sentiment Label Creation

Sentiment labels were created from the review rating:

- Ratings 1–2 → Negative
- Rating 3 → Neutral
- Ratings 4–5 → Positive

This provided three classes for supervised sentiment classification.

---

## 3. Text Preprocessing

The review text was cleaned using:

- Lowercasing
- URL removal
- Punctuation removal
- Tokenization
- Stop-word removal
- Lemmatization

These steps reduce unnecessary variation in text and make the reviews suitable for traditional machine-learning models.

The original review text was retained separately for VADER because VADER can use punctuation, capitalization and other textual signals.

---

## 4. TF-IDF

TF-IDF was used to convert the cleaned review text into numerical features.

Both unigrams and bigrams were considered.

Examples:

- `delivery`
- `food quality`
- `late delivery`

A maximum of 5,000 features was used.

---

## 5. Sentiment Classification

### Model

Multinomial Naive Bayes was used with the TF-IDF features.

The dataset was split into:

- 80% training
- 20% testing

Stratified sampling was used to preserve the sentiment distribution.

### Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| TF-IDF + Naive Bayes | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| VADER | 0.5887 | 0.5731 | 0.5887 | 0.5801 |

---

## 6. Confusion Matrix

The Naive Bayes confusion matrix showed that all negative, neutral and positive test reviews were classified correctly.

There were no misclassified samples in the test set.

---

## 7. VADER Sentiment Analysis

VADER was applied to the original review text.

VADER is a lexicon and rule-based sentiment analyzer that is useful for short and informal text and can consider signals such as:

- Punctuation
- Capitalization
- Slang
- Emojis
- Sentiment intensity

VADER achieved an accuracy of 58.87% on this dataset.

---

## 8. Customer Dissatisfaction Themes

TF-IDF analysis of negative reviews identified the following important terms/themes:

1. Food
2. Experience
3. Disappointing experience
4. Disappointing
5. Delivery
6. Quality

These indicate that food quality, delivery performance and the overall customer experience are important areas of dissatisfaction.

---

## 9. Business Interpretation

The analysis suggests three major areas for operational improvement:

### Food Quality

Monitor restaurant food quality and identify restaurants associated with repeated negative feedback.

### Delivery

Investigate delays and delivery-related complaints, particularly in cases involving long delivery times.
## 10. Important Model Limitation

TF-IDF + Naive Bayes achieved 100% test accuracy.

However, this unusually high score should not automatically be interpreted as real-world model performance.

The dataset is synthetic and the generated reviews may contain strongly structured language patterns that make sentiment classification easier than it would be with naturally written customer reviews.

Therefore, the model should be validated on real customer feedback before being used in production.

---

## 11. Deliverables

- Cleaned review dataset
- NLP preprocessing pipeline
- TF-IDF representation
- Naive Bayes sentiment classifier
- Model evaluation metrics
- Confusion matrix
- VADER sentiment analysis
- Model comparison
- Negative-review keyword analysis
- Business recommendations
### Customer Experience

Track recurring negative experiences and identify common issues across restaurants and orders.

These insights can be combined with operational data such as delivery time, traffic, weather and restaurant preparation time for deeper root-cause analysis.

---


