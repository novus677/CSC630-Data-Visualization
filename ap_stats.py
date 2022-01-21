import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt

stats = pd.read_csv('AP statistics 2021.csv')

score5 = alt.Chart(stats).mark_bar().encode(
    alt.X('Exam:N', sort=list(stats['Exam']),title='AP Exam'),
    alt.Y('Score - 5:Q', title='Fraction of 5s'),
    alt.Color('Category:N')
)

score1 = alt.Chart(stats).mark_bar().encode(
    alt.X('Exam:N', sort=list(stats['Exam']),title='AP Exam'),
    alt.Y('Score - 1:Q',title='Fraction of 1s'),
    alt.Color('Category:N')
)

score5 | score1