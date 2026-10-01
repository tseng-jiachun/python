temps =[25.1, 26.3, 24.8, 27.0]

biggest = temps[0]
for t in temps:
    if t > biggest:
        biggest = t
print("最大:", biggest)