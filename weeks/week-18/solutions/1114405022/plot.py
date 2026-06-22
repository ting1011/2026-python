import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import os

# 必須加上此行，否則在沒有 GUI 的環境會報錯
matplotlib.use("Agg")

def draw_radar_chart():
    # 1. 定義維度
    categories = ['Time', 'Cmp', 'Space', 'Setup']
    N = len(categories)

    # 2. 準備數據 (基於 la-search 表現)
    # 數值越小越好，因此我們使用 1/value 進行正規化，使面積越大代表效能越好
    # 這裡使用模擬數據或從 results.json 讀取 (簡化起見使用典型權衡值)
    data = {
        'Linear Search': [1, 1, 5, 5], # Time (Slow), Cmp (High), Space (Low), Setup (Low)
        'Binary Search': [5, 5, 5, 1], # Time (Fast), Cmp (Low), Space (Low), Setup (High)
        'Set Search': [5, 5, 1, 2],    # Time (Fastest), Cmp (Low), Space (High), Setup (Med)
    }

    # 正規化 (0-1 區間，越大越好)
    # 這裡簡單對應：1=最差, 5=最好
    
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1] # 閉合圓環

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    for label, values in data.items():
        vals = values + values[:1]
        ax.plot(angles, vals, linewidth=2, label=label)
        ax.fill(angles, vals, alpha=0.25)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), categories)
    
    plt.title("Search Algorithm Trade-offs (Bigger is Better)", size=15, y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    
    plt.savefig("C:/Users/user/Desktop/2026 python/weeks/week-18/solutions/1114405022/assets/radar.png", bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    draw_radar_chart()
