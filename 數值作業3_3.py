# 資料：時間 T，距離 D，速度 V（英呎/秒）
T = [0, 3, 5, 8, 13]
D = [0, 200, 375, 620, 990]
V = [75, 77, 80, 74, 72]

def fact(n):
    return 1 if n <= 1 else n * fact(n-1)

# Hermite 插值函數與導數
def hermite_poly(T, D, V):
    n = len(T)
    z = [0]*(2*n)
    Q = [[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        z[2*i] = z[2*i+1] = T[i]
        Q[2*i][0] = Q[2*i+1][0] = D[i]
        Q[2*i+1][1] = V[i]
        if i > 0:
            Q[2*i][1] = (Q[2*i][0] - Q[2*i-1][0]) / (z[2*i] - z[2*i-1])
    for j in range(2, 2*n):
        for i in range(j, 2*n):
            Q[i][j] = (Q[i][j-1] - Q[i-1][j-1]) / (z[i] - z[i-j])
    return z, Q

def hermite_eval(z, Q, t):
    n = len(z)
    H = Q[0][0]
    dH = 0
    prod = 1
    for i in range(1, n):
        term = Q[i][i]
        H += term * prod
        dterm = 0
        for j in range(i):
            partial = 1
            for k in range(i):
                if k != j:
                    partial *= (t - z[k])
            dterm += partial
        dH += term * dterm
        prod *= (t - z[i-1])
    return H, dH

# 構造 Hermite 多項式
z, Q = hermite_poly(T, D, V)

# (a) t = 10 時的位置與速度
pos_10, vel_10 = hermite_eval(z, Q, 10)

# (b) 是否超過 55 mi/h = 80.67 ft/s？找第一次超過的時間
speed_limit = 80.67
exceed_time = None
for t in range(0, 14):
    _, v = hermite_eval(z, Q, t)
    if v > speed_limit:
        exceed_time = t
        break

# (c) 找速度最大值
max_v = -1
max_t = 0
for t in range(0, 14):
    _, v = hermite_eval(z, Q, t)
    if v > max_v:
        max_v = v
        max_t = t

# 顯示所有答案
print(f"(a) t = 10 時位置 ≈ {pos_10:.6f} ft，速度 ≈ {vel_10:.6f} ft/s")
if exceed_time:
    print(f"(b) 超過 55 mi/h 的時間為 t = {exceed_time} 秒")
else:
    print("(b) 車速未超過 55 mi/h")
print(f"(c) 車速最大值 ≈ {max_v:.6f} ft/s，發生在 t = {max_t} 秒")
