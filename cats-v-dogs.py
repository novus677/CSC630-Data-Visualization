import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt

alt.renderers.enable('mimetype')

df_test = pd.DataFrame({
    'state': ['Conneticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont', 'New Jersey', 'New York', 'Pennsylvania', 'Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin', 'Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Maryland', 'North Carolina', 'South Carolina', 'Virginia', 'West Virginia', 'Alabama', 'Kentucky', 'Mississippi', 'Tennessee', 'Arkansas', 'Louisiana', 'Oklahoma', 'Texas', 'Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming', 'California', 'Oregon', 'Washington'],
    'dog_percent': [24.0, 35.9, 28.9, 23.7, 25.8, 28.3, 29.1, 27.0, 38.9, 31.0, 49.4, 41.9, 37.9, 33.6, 36.3, 43.1, 35.5, 45.1, 47.1, 44.3, 32.1, 42.2, 22.5, 39.8, 36.7, 30.2, 41.3, 45.3, 35.6, 49.6, 46.9, 46.5, 51.0, 47.0, 51.6, 38.3, 47.7, 43.4, 43.0, 47.2, 58.3, 51.9, 36.8, 39.4, 36.2, 36.0, 40.1, 37.8, 42.8],
    'cat_percent': [26.7, 43.6, 23.5, 36.4, 16.7, 44.6, 18.9, 21.1, 28.9, 21.0, 37.5, 31.2, 30.7, 32.4, 35.6, 32.4, 26.5, 28.6, 30.9, 24.8, 26.6, 24.1, 16.4, 24.2, 20.4, 18.6, 26.5, 25.2, 23.9, 37.7, 26.1, 32.2, 29.1, 30.9, 34.8, 19.0, 28.4, 20.5, 26.4, 27.1, 33.3, 22.8, 23.1, 25.2, 24.7, 30.0, 22.9, 30.0, 30.5]
})

alt.Chart(df_test,title='Cat and Dog Ownerships by State').mark_point(color='green',filled=True).encode(
    alt.X('dog_percent:Q',scale=alt.Scale(zero=False),title='Percent of Households with Dogs'),
    alt.Y('cat_percent:Q',scale=alt.Scale(zero=False),title='Percent of Households with Cats'),
    alt.Tooltip('state:N')
).interactive()