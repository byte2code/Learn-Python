
def simple_moving_average(data, period):
    sma_values = []
    for i in range(len(data)):
        if i < period - 1:
            continue
        else:
            sma = sum(data[i - period + 1 : i + 1]) / period
            sma_values.append(sma)
    return sma_values

data = [10, 15, 20, 25, 30, 35, 40, 45, 50]
period = 3 
sma = simple_moving_average(data, period)
print(f"Simple Moving Average with a {period}-period: {sma}")