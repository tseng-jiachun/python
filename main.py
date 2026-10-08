sensor = [{"id":"A","temp":25.6},{"id":"B","temp":31.0},
          {"id":"C","temp":28.5},{"id":"D","temp":35.2}]

count = 0
for s in sensor:
    if s["temp"] > 30:
        print(f"超標: {s['id']} ({s['temp']})")
        count += 1
print("共", count, "顆超標")