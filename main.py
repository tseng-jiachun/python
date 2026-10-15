sensors = [{"id":"A","temp":25.3},
           {"id":"B","temp":31.0},
           {"id":"C","temp":28.5}]

with open("data.csv","w") as f:
    f.write("id,temp\n")
    for s in sensors:
        f.write(f"{s['id']},{s['temp']}\n")


with open("data.csv","r") as f:
    lines = f.readlines()

total=0
count=0
for line in lines[1:]:
    parts = line.strip().split(",")
    total += float(parts[1])
    count += 1
print(f"平均{total/count:.2f}")