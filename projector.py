import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/c-129-project/main/Processed_data/star_with_gravity.csv")
bo = []
for i in df.Distance:
    if i <= 100:
        bo.append(True)
    else:
        bo.append(False)
is_dist = pd.Series(bo)
star_dist = df[is_dist]
star_dist.reset_index(inplace = True,drop = True)
gravbo = []
for i in star_dist.Gravity:
    if i <= 100:
        gravbo.append(True)
    else:
        gravbo.append(False)
is_Gravity = pd.Series(gravbo)
final_Stars = star_dist[is_Gravity]
final_Stars.reset_index(inplace = True,drop = True)
final_Stars.to_csv("filtstar.csv")