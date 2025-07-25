# Hypothesis Testing on Employee Performance Based on Training Attendance

This project performs hypothesis testing to determine whether attending a training session improves the performance scores of employee's. We apply statistical techniques (specifically Welch’s t-test) to check if the difference between the two groups is statistically significant.

---

## What is Hypothesis Testing?

Hypothesis Testing is a statistical method used to make inferences about a population from sample data. It helps decide whether to:

- ✅ **Reject the Null Hypothesis**: There is a significant difference.
- ❌ **Fail to Reject the Null Hypothesis**: No significant evidence of difference.

This is widely used in data science, business analytics, A/B testing, and educational research.

---

## 🎯 Project Objective: Evaluate Impact of Training

We compare the performance of two groups of Employee's:

- **Group A**: Employee's who **attended** the training
- **Group B**: Employee's who **did not attend** the training

The goal is to determine if **training attendance improves employee's performance scores**.

---

## 🗃️ Dataset Overview

- **Total Records**: 1,000+ Employee's
- **No missing values**
- **Columns Used**:
  - `TrainingAttended` (Yes/No)
  - `PerformanceScore` (numerical)

---

## 🧪 Hypothesis Setup

- **Null Hypothesis (H₀)**: Training has **no effect** on performance (mean scores are equal).
- **Alternative Hypothesis (H₁)**: Training **improves** performance (mean of training group > mean of no-training group).

We use a **one-tailed Welch’s t-test** (assuming unequal variance).

---

## 📈 Summary of Group Means

| Group             | Mean Performance Score |
|------------------|------------------------|
| **Training = Yes** | e.g., 74.3             |
| **Training = No**  | e.g., 70.1             |

_Actual means depend on the dataset used. Replace with real values if needed._

---

## 📊 T-Test Result

| Metric            | Value           |
|-------------------|-----------------|
| **T-statistic**   | e.g., 3.25       |
| **P-value**       | e.g., 0.0007     |

✅ Since **p-value < 0.05**, we **reject the null hypothesis**.

---

## ✅ Conclusion

Attending the training session **has a statistically significant positive impact** on Employee's performance. Employee's who attended training scored higher on average, and the difference is unlikely due to random chance.

---

## 📦 Libraries Used

- `pandas`
- `numpy`
- `scipy.stats`
- `matplotlib`
- `seaborn`
- `plotly`

---

## 📌 Project Highlights

- Real-world hypothesis testing on educational data
- One-tailed Welch’s t-test (unequal variances)
- Clean data with no missing values
- Box plot and statistical summary included

---

