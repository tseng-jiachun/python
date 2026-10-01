temps = [25.1, 26.3, 24.8, 27.0, 25.9, 23.7]
total = 0
avg = 0
biggest = temps[0]
smallest = temps[0]

for t in temps:
    total += t
    if t > biggest:
        biggest = t 
    if t < smallest:
        smallest = t

avg = total / len(temps)
print(f"總和: {total:.2f}")
print(f"平均: {avg:.2f}")
print(f"最大值: {biggest:.2f}")
print(f"最小值: {smallest:.2f}")