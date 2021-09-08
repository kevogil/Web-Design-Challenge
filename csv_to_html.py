import pandas as pd

df = pd.read_csv("WebVisualizations/Resources/cities.csv")
df.to_html("WebVisualizations/Resources/cities.html")