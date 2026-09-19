import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体（防止中文乱码）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# === 第一步：构造模拟NBA球员数据（后续替换为真实爬取数据）===
data = {
    '球员': ['库里', '詹姆斯', '杜兰特', '东契奇', '字母哥', '哈登', '伦纳德', '约基奇', '塔图姆', '利拉德'],
    '位置': ['PG', 'SF', 'SF', 'PG', 'PF', 'PG', 'SF', 'C', 'SF', 'PG'],
    '场均得分': [29.4, 28.9, 27.1, 33.9, 30.4, 24.7, 23.7, 26.1, 30.1, 24.3],
    '场均篮板': [4.6, 8.3, 6.1, 9.2, 11.5, 7.3, 6.9, 11.8, 8.1, 4.4],
    '场均助攻': [6.3, 8.7, 5.1, 9.8, 6.5, 11.2, 3.1, 9.0, 4.9, 7.0],
    '投篮命中率': [0.48, 0.54, 0.52, 0.49, 0.55, 0.43, 0.51, 0.58, 0.47, 0.43]
}

df = pd.DataFrame(data)

# === 第二步：数据概览 ===
print("=== 数据前5行 ===")
print(df.head())
print("\n=== 基本统计 ===")
print(df.describe())

# === 第三步：可视化1 - 球员得分对比 ===
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='球员', y='场均得分', hue='位置', palette='viridis')
plt.title('NBA球员场均得分对比')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/player_points.png', dpi=150)
plt.close()

# === 第四步：可视化2 - 得分vs篮板散点图 ===
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='场均篮板', y='场均得分', hue='位置', s=150)
for i, row in df.iterrows():
    plt.text(row['场均篮板']+0.1, row['场均得分'], row['球员'], fontsize=9)
plt.title('球员得分-篮板分布')
plt.tight_layout()
plt.savefig('charts/pts_vs_rebounds.png', dpi=150)
plt.close()

# === 第五步：可视化3 - 各位置场均数据对比 ===
position_stats = df.groupby('位置')[['场均得分', '场均篮板', '场均助攻']].mean()
position_stats.plot(kind='bar', figsize=(10, 6))
plt.title('各位置场均数据对比')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('charts/position_comparison.png', dpi=150)
plt.close()

print("\n✅ 分析完成！图表已保存到 charts/ 文件夹")