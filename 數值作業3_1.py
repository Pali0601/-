# 已知資料點
x_vals = [0.698, 0.733, 0.750, 0.768, 0.803]
y_vals = [0.7661, 0.7432, 0.7317, 0.7193, 0.6946]
x = 0.750

# 階乘函數
def fact(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f

# Lagrange 插值函數
def lagrange(x_vals, y_vals, x, deg):
    result = 0
    for i in range(deg+1):
        term = y_vals[i]
        for j in range(deg+1):
            if i != j:
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        result += term
    return result

# 誤差上限估計
def error_bound(x_vals, x, deg):
    prod = 1
    for i in range(deg+1):
        prod *= abs(x - x_vals[i])
    return prod / fact(deg+1)  # 假設最高導數最大為1

# 執行結果輸出
for d in range(1, 5):
    y_approx = lagrange(x_vals, y_vals, x, d)
    err = error_bound(x_vals, x, d)
    print(f"Degree {d}:  Approx = {round(y_approx, 6)},  Error Bound = {round(err, 6)}")
