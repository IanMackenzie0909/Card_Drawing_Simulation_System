import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def simulate_one_person():
    prob = 0.02
    draws = 0
    while True:
        draws += 1
        if np.random.random() < prob:
            return draws
        if draws >= 90:
            return draws
        if draws >= 50:
            prob += 0.005

def simulate_many_people(num_people):
    results = []
    for _ in range(num_people):
        draws = []
        for _ in range(50):  # 每個人抽50張SSR卡
            draws.append(simulate_one_person())
        results.append(np.mean(draws))  # 計算每個人的平均抽卡數
    return results

# 模擬一萬個人
simulations = simulate_many_people(10000)

# 使用Pandas DataFrame
df_simulations = pd.DataFrame(simulations, columns=['average_draws'])

# 計算統計數據
average_draws_mean = df_simulations['average_draws'].mean()
average_draws_median = df_simulations['average_draws'].median()
average_draws_2p5 = df_simulations['average_draws'].quantile(0.025)
average_draws_97p5 = df_simulations['average_draws'].quantile(0.975)

# 繪製平均抽卡數的分布圖
df_simulations['average_draws'].plot(kind='hist', bins=np.arange(30, 70, 1), density=True, alpha=0.75)
plt.xlabel('Average number of draws')
plt.ylabel('Density')
plt.title('Distribution of average draws per person')
plt.show()

# 模擬所有抽卡數（一次生成所有數據）
all_draws = [simulate_one_person() for _ in range(500000)]  # 50 * 10000

# 使用Pandas DataFrame
df_all_draws = pd.DataFrame(all_draws, columns=['draws'])

# 計算所有抽卡數的統計數據
all_draws_mean = df_all_draws['draws'].mean()
all_draws_median = df_all_draws['draws'].median()
all_draws_2p5 = df_all_draws['draws'].quantile(0.025)
all_draws_97p5 = df_all_draws['draws'].quantile(0.975)

# 繪製所有抽卡數的分布圖
df_all_draws['draws'].plot(kind='hist', bins=np.arange(30, 100, 1), density=True, alpha=0.75)
plt.xlabel('Number of draws')
plt.ylabel('Density')
plt.title('Distribution of all draws')
plt.show()

# 輸出結果
print("平均抽卡數的統計結果：")
print("平均值：", average_draws_mean)
print("中位數：", average_draws_median)
print("第2.5百分位：", average_draws_2p5)
print("第97.5百分位：", average_draws_97p5)

print("\n所有抽卡數的統計結果：")
print("平均值：", all_draws_mean)
print("中位數：", all_draws_median)
print("第2.5百分位：", all_draws_2p5)
print("第97.5百分位：", all_draws_97p5)