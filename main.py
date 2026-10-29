import statistics

def adc_to_v(adc):
    return adc / 4095 * 3.3

row=["2048","3000","1024","壞"]
volts=[]
for r in row:
    try:
        volts.append(adc_to_v(float(r)))
    except ValueError:
        print("跳過",r)
print(f"平均:{statistics.mean(volts):.2f} V")