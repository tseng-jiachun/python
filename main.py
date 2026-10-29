import pandas as pd

df=pd.read_csv("sensors.csv")

print(f"共 {len(df)} 筆,平均: {df["temp"].mean():.1f} 度")
hot=df[df["temp"]>30]
print(f"超標(>30): {len(hot)} 筆")

