from sklearn.linear_model import \
LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sensor_day.csv",dtype=str)

times,temps=[],[]
for i in range(len(df)):
    try:
        t=(float(df["temp"][i]))
    except ValueError:
        continue
    times.append(df["time"][i])
    temps.append(t)

clean = pd.DataFrame({"time":times,"temp":temps})

print("平均:",round(clean["temp"].mean(), 1))
print("最高:",clean["temp"].max())
print("最低:",clean["temp"].min())
clean["warm"]=clean["temp"]>28
print("超標:",int(clean["warm"].sum()),"筆")

hot=clean[clean["warm"]]
temp_f=clean["temp"]*9/5+32
X=np.array(range(len(clean))).reshape(-1,1)
y=np.array(clean["temp"])
model=LinearRegression().fit(X,y)
p=model.predict(len(X)+1)
print("明日預測:",round(p[0],1))
plt.plot(clean["time"],clean["temp"],marker="o",label="temp(°C)")
plt.plot(temp_f,color="yellow",marker="o",label="temp (°F)")
plt.axhline(28,color="orange",linestyle="--",label="limit")
plt.scatter(hot.index,hot["temp"],color="red",zorder=5,label="over")
plt.legend()
plt.grid()
plt.title("Temp of the day")
plt.savefig("report.png")
plt.show()