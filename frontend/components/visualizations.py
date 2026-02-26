import streamlit as st
from matplotlib import pyplot as plt
import pandas as pd

def plot_survival_rate(data):
    survival_counts = data['Survived'].value_counts()
    fig = plt.figure(figsize=(8, 5))
    plt.bar(survival_counts.index, survival_counts.values, color=['red', 'green'])
    plt.xticks([0, 1], ['Did not survive', 'Survived'])
    plt.title('Survival Rate on the Titanic')
    plt.xlabel('Survival')
    plt.ylabel('Count')
    plt.grid(axis='y')
    st.pyplot(fig)

def plot_age_distribution(data):
    fig = plt.figure(figsize=(10, 6))
    plt.hist(data['Age'].dropna(), bins=30, color='blue', alpha=0.7)
    plt.title('Age Distribution of Passengers')
    plt.xlabel('Age')
    plt.ylabel('Number of Passengers')
    plt.grid(axis='y')
    st.pyplot(fig)

def plot_class_distribution(data):
    class_counts = data['Pclass'].value_counts()
    fig = plt.figure(figsize=(8, 5))
    plt.bar(class_counts.index.astype(str), class_counts.values, color='orange')
    plt.title('Passenger Class Distribution')
    plt.xlabel('Class')
    plt.ylabel('Count')
    plt.grid(axis='y')
    st.pyplot(fig)