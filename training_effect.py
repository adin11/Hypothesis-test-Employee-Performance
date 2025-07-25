import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.express as px


# Function to load data
def load_data(filepath):
    return pd.read_csv(filepath)

# Function to split the data based on training
def split_groups(df):
    group_yes = df[df['TrainingAttended'] == 'Yes']['PerformanceScore']
    group_no = df[df['TrainingAttended'] == 'No']['PerformanceScore']
    return group_yes, group_no

# Function to perform Shapiro-Wilk normality test
def perform_shapiro_test(group_yes, group_no, sample_size=300):
    sample_size = min(len(group_yes), len(group_no), sample_size)
    shapiro_yes = stats.shapiro(group_yes.sample(sample_size, random_state=1))
    shapiro_no = stats.shapiro(group_no.sample(sample_size, random_state=1))
    return shapiro_yes, shapiro_no

# Function to perform Levene’s test for equal variances
def perform_levene_test(group_yes, group_no):
    return stats.levene(group_yes, group_no)

# Function to perform t-test
def perform_ttest(group_yes, group_no):
    return stats.ttest_ind(group_yes, group_no, equal_var=False)

# Function to plot box plot using Plotly
def plot_performance_box(df):
    fig = px.box(
        df,
        x='TrainingAttended',
        y='PerformanceScore',
        title='Performance Score by Training Attendance',
        labels={
            'TrainingAttended': 'Training Attended',
            'PerformanceScore': 'Performance Score'
        },
        color='TrainingAttended',
        points='all'
    )

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='white',
        margin=dict(l=40, r=40, t=80, b=60),
        showlegend=False
    )
    fig.show()

# Main function to orchestrate everything
def main():
    # Load data
    df = load_data('data_hypothesis.csv')
    
    # Split into two groups
    group_yes, group_no = split_groups(df)

    # Shapiro-Wilk normality test
    shapiro_yes, shapiro_no = perform_shapiro_test(group_yes, group_no)
    print("Shapiro Test (Training = Yes):", shapiro_yes)
    print("Shapiro Test (Training = No):", shapiro_no)

    # Levene’s test
    levene = perform_levene_test(group_yes, group_no)
    print("Levene’s Test:", levene)

    # T-test
    t_stat, p_val = perform_ttest(group_yes, group_no)
    print("T-test statistic:", t_stat)
    print("T-test p-value:", p_val)

    # Plot
    plot_performance_box(df)

# Entry point
if __name__ == "__main__":
    main()
