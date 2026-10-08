sensor = [{"id":"A","temp":25},{"id":"B","temp":31},
          {"id":"C","temp":28},{"id":"D","temp":35}]

count = 0
for s in sensor:
    if s["temp"] > 30:
        print("超標:", s["id"])
        count += 1
print("共", count, "顆超標")