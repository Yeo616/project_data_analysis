import streamlit as st
import matplotlib.pyplot as plt

def job_title_wordcloud():
    job_title=data['Job Title'][~pd.isnull(data['Job Title'])]
    wordCloud = WordCloud(width=450,height= 300).generate(' '.join(job_title))
    plt.figure(figsize=(19,9))
    plt.axis('off')
    plt.title(data['Job Title'].name,fontsize=20)
    plt.imshow(wordCloud)
    plt.show()