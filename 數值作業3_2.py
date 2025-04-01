# 反插值法：使用 y 去估計對應的 x 值

# 已知資料點 (x, y) = (x, e^(-x))
x_vals = [0.3, 0.4, 0.5, 0.6]
y_vals = [0.740818, 0.670320, 0.606531, 0.548812]

# 我們要求 x 使得 x = e^(-x)，等於說是 y = x
# 所以我們想找 y 值為多少時，反推 x，也就是解 f(x) = x

# 用一次反插值初步估計
def inverse_lagrange(x_vals, y_vals, y_target):
    n = len(x_vals)
    result = 0
    for i in range(n):
        term = x_vals[i]
        for j in range(n):
            if i != j:
                term *= (y_target - y_vals[j]) / (y_vals[i] - y_vals[j])
        result += term
    return result

# 初始猜測：x = 0.6 時 y = 0.548812 -> 所以先從 y=0.6 開始
# 然後進行反覆修正

guess = 0.6
for _ in range(5):  # 做 5 次反覆
    guess = inverse_lagrange(x_vals, y_vals, guess)

print(f"近似解 x ≈ {guess:.10f}")
