
sensor = [{"id":"A","temp":25},{"id":"B","temp":31.0},
          {"id":"C","temp":28},{"id":"D","temp":35.2}]

count = 0
highest = sensor[0]
total = 0

for s in sensor:
    total += s["temp"]
    if s["temp"] > highest["temp"]:
        highest = s
    if s["temp"] > 30:
        count += 1
print(f"共{len(sensor)}顆，平均: {total/len(sensor):.2f}")
print(f"最高: {highest['id']} ({highest['temp']})")
print("超標(>30):", count)
