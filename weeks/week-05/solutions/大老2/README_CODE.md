![Big Two Game](README.md)

# 大老2 Card Game - 完整實現

## 📋 項目結構

```
大老2/
├── game/                    # 遊戲核心模組
│   ├── __init__.py
│   ├── models.py           # Phase 1: 資料模型 (Card, Deck, Hand, Player)
│   ├── classifier.py       # Phase 2: 牌型分類 (HandClassifier)
│   ├── finder.py           # Phase 3: 牌型搜尋 (HandFinder)
│   ├── ai.py               # Phase 4: AI 策略 (AIStrategy)
│   ├── game.py             # Phase 5: 遊戲流程 (BigTwoGame)
│   └── ui/                 # Phase 6: GUI 介面
│       ├── __init__.py
│       ├── render.py       # 渲染器 (Renderer)
│       ├── input.py        # 輸入處理 (InputHandler)
│       └── app.py          # 主應用 (BigTwoApp)
├── tests/                  # 測試模組
│   ├── __init__.py
│   └── test_all.py         # 所有測試用例
├── main.py                 # 遊戲入口
└── README.md               # 說明文件
```

---

## 🎮 Phase 1-6 實現說明

### **Phase 1: 資料模型** (`game/models.py`)
核心卡牌數據結構實現：
- **Card**: 單張牌（排序、花色、顯示）
- **Deck**: 52張牌組（洗牌、發牌）
- **Hand**: 玩家手牌（繼承自 list，排序、查找3♣）
- **Player**: 玩家（名稱、是否AI、手牌、分數）

**關鍵特性**:
- Card 支持完整比較運算：`>`、`==`、`<`
- 花色排序：♠ > ♥ > ♦ > ♣
- 數字排序：2 > A > K > Q > J > T > 9 > 8 > 7 > 6 > 5 > 4 > 3

### **Phase 2: 牌型分類** (`game/classifier.py`)
識別和比較牌型：
- **CardType** (Enum): 8種牌型
  - 1: 單張
  - 2: 對子
  - 3: 三條
  - 4: 順子
  - 5: 同花
  - 6: 葫蘆 (3+2)
  - 7: 四條
  - 8: 同花順

- **HandClassifier** (靜態方法):
  - `classify()`: 識別牌型
  - `compare()`: 比較大小
  - `can_play()`: 檢查合法性

**牌型識別邏輯**:
- 支持特殊情況：A-2-3-4-5 順子
- 優先判斷：四條 > 葫蘆 > 同花 > 順子

### **Phase 3: 牌型搜尋** (`game/finder.py`)
尋找所有可能的合法出牌：
- **HandFinder** (靜態方法):
  - `find_singles()`: 查找單張
  - `find_pairs()`: 查找對子
  - `find_triples()`: 查找三條
  - `find_fives()`: 查找 5 張牌型
  - `get_all_valid_plays()`: 根據上家出牌，回傳所有合法出牌

**演算法**:
- 使用 `itertools.combinations` 找出所有組合
- 自動過濾無效牌型

### **Phase 4: AI 策略** (`game/ai.py`)
使用貪心演算法選擇最優出牌：
- **AIStrategy** (靜態方法):
  - `score_play()`: 評分出牌
    - 牌型分數 × 100
    - 數字分數 × 10
    - 剩1張 +10000
    - 剩≤3張 +500
    - 每張♠牌 +5
  - `select_best()`: 選擇分數最高的出牌

**AI 特點**:
- 優先出牌（快速結束）
- 偏好高級牌型
- 保留♠牌

### **Phase 5: 遊戲流程** (`game/game.py`)
主遊戲控制器：
- **BigTwoGame**:
  - `setup()`: 發牌、決定先手
  - `play()`: 處理出牌
  - `pass_()`: 處理過牌
  - `ai_turn()`: AI 自動回合
  - `check_winner()`: 檢查勝者

**遊戲規則**:
- 4位玩家
- 每人13張牌
- 最先出完牌者獲勝
- 3人過牌則清空桌面

### **Phase 6: GUI 介面** (`game/ui/`)
Pygame 圖形介面：

**render.py - Renderer**:
- 繪製卡牌（正面/背面）
- 繪製玩家手牌（重疊顯示）
- 繪製遊戲狀態（玩家信息、最後出牌）
- 繪製按鈕

**input.py - InputHandler**:
- 處理滑鼠點擊（選牌、按鈕）
- 處理鍵盤輸入（Enter=出牌, P=過牌）
- 驗證選牌

**app.py - BigTwoApp**:
- 主應用程序
- 遊戲循環
- 事件處理
- 遊戲繪製

---

## 🚀 使用方法

### 安裝依賴
```bash
pip install pygame
```

### 運行遊戲
```bash
python main.py
```

### 運行測試
```bash
python -m unittest tests.test_all -v
```

---

## 🎯 遊戲玩法

1. **目標**: 最先把手牌全部出完
2. **開始**: 持有3♣的玩家先出
3. **規則**:
   - 必須跟上家的牌型
   - 牌型必須更大
   - 無法跟牌可過牌
   - 3人過牌後重置桌面

4. **牌型排序** (由小到大):
   - 單張 < 對子 < 三條 < 順子 < 同花 < 葫蘆 < 四條 < 同花順

5. **數字排序** (由小到大):
   - 3 < 4 < 5 < 6 < 7 < 8 < 9 < T < J < Q < K < A < 2

---

## 🤖 AI 特點

- 使用貪心演算法
- 優先出牌（加速遊戲進行）
- 優先出高級牌型
- 保留♠牌作為王牌

---

## 📝 測試覆蓋

- Card 類：創建、表示、比較、哈希
- Deck 類：初始化、發牌、洗牌
- Hand 類：創建、查找、移除、排序
- Player 類：創建、拿牌、出牌
- Classifier：牌型識別、比較、合法性檢查
- Finder：單張、對子、三條、5張牌尋找
- AI：評分、最優選擇
- Game：設置、出牌、過牌、勝利檢查

---

## 🔧 開發檢查清單

- [x] 資料模型實現
- [x] 牌型分類完成
- [x] 牌型搜尋優化
- [x] AI 策略實現
- [x] 遊戲流程完成
- [x] GUI 介面開發
- [x] 單元測試覆蓋
- [x] 類型註解添加

---

## 📚 學習重點

### 物件導向設計
- 類別繼承（Hand 繼承 list）
- 靜態方法組織（HandClassifier, AIStrategy）
- Enum 使用（CardType）

### 演算法與資料結構
- 組合搜尋（combinations）
- 排序與比較邏輯
- 貪心演算法

### GUI 開發
- Pygame 基礎
- 事件處理
- 遊戲循環

### 軟體工程
- 模組化設計
- 測試驅動開發
- 代碼文檔化

---

## 🐛 已知限制

- GUI 目前為基礎版本，可進一步美化
- AI 策略可進一步優化（例如加入隨機性、計算記憶等）
- 尚未實現遊戲保存/加載功能
- 暫無計分系統

---

## 🎓 教學價值

本項目適合以下學習場景：

1. **初級 Python**
   - 類別設計
   - 列表操作
   - 字典使用

2. **進階 Python**
   - Enum 列舉
   - 靜態方法
   - 類型註解

3. **遊戲開發**
   - Pygame 基礎
   - 遊戲狀態管理
   - 事件循環

4. **軟體工程**
   - 模組化設計
   - 測試設計
   - 文檔編寫

---

**作者**: DevSecOpsLab-CSIE-NPU  
**日期**: 2026年4月  
**版本**: 1.0
