
# 匯入系統模組與隨機模組
print("測試輸出")
import sys
import random
# 匯入 collections 內的 namedtuple, Counter, defaultdict
from collections import namedtuple, Counter, defaultdict


# 定義 General 資料結構，代表一位武將
General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])


# 讀取 generals.txt，回傳所有武將的字典
def load_generals(filename):
    import os
    generals = {}
    print(f"[DEBUG] generals.txt 路徑: {os.path.abspath(filename)}")
    # 若 generals.txt 不存在，自動產生範例檔案
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("""蜀 劉備 100 18 16 75 False\n蜀 關羽 100 28 14 85 False\n蜀 諸葛亮 80 15 12 60 True\n吳 孫權 95 20 15 78 False\n吳 周瑜 85 18 14 85 True\n吳 黃蓋 100 26 15 75 False\n魏 曹操 120 28 16 80 False\n魏 夏侯惇 105 27 14 82 False\n魏 郭嘉 75 16 11 68 True\nEOF\n""")
        print(f"[DEBUG] 已自動產生 generals.txt 檔案於 {os.path.abspath(filename)}")
    # 讀取 generals.txt 內容
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == 'EOF':
                break
            if not line:
                continue
            # 解析每一行資料
            parts = line.split()
            faction, name, hp, atk, def_, spd, is_leader = parts
            general = General(
                faction=faction,
                name=name,
                hp=int(hp),
                atk=int(atk),
                def_=int(def_),
                spd=int(spd),
                is_leader=(is_leader == 'True')
            )
            generals[name] = general
    return generals


# 讓玩家或電腦選擇指定勢力的武將
def choose_general(generals, faction, auto=False):
    # 篩選出指定勢力的所有武將
    candidates = [g for g in generals.values() if g.faction == faction]
    if auto:
        # 自動模式下隨機選擇一位武將
        chosen = random.choice(candidates)
        print(f"自動選擇 {faction} 武將：{chosen.name}")
        return chosen
    # 玩家手動選擇武將
    print(f"可選擇的{faction}武將：")
    for idx, g in enumerate(candidates, 1):
        print(f"  {idx}. {g.name} (HP:{g.hp} 攻:{g.atk} 防:{g.def_} 速:{g.spd}{' 軍師' if g.is_leader else ''})")
    while True:
        try:
            choice = int(input(f"請選擇{faction}武將(輸入編號): "))
            if 1 <= choice <= len(candidates):
                return candidates[choice-1]
        except Exception:
            pass
        print("輸入錯誤，請重新輸入。")


# 進行兩位武將的戰鬥，回合制直到一方陣亡
def battle(g1, g2, verbose=True, show_hp=True):
    if verbose:
        print(f"\n戰鬥開始：{g1.name} vs {g2.name}")
    # 初始化雙方血量
    hp1, hp2 = g1.hp, g2.hp
    turn = 0
    # 速度高者先攻
    if g1.spd >= g2.spd:
        attacker, defender = g1, g2
        hp_att, hp_def = hp1, hp2
    else:
        attacker, defender = g2, g1
        hp_att, hp_def = hp2, hp1
    # ANSI 控制碼，讓陣亡角色顯示灰色
    ANSI_GRAY = '\033[90m'
    ANSI_RESET = '\033[0m'
    dead = {g1.name: False, g2.name: False}
    # 進入回合制戰鬥
    while hp_att > 0 and hp_def > 0:
        turn += 1
        if verbose:
            print(f"\n--- 第{turn}回合 ---")
            if show_hp:
                name_disp = defender.name if not dead[defender.name] else f"{ANSI_GRAY}{defender.name}{ANSI_RESET}"
                print(f"攻擊前：{name_disp} HP={hp_def}")
        # 計算傷害，最少為 1
        damage = max(1, attacker.atk - defender.def_)
        hp_def -= damage
        if verbose:
            name_att = attacker.name if not dead[attacker.name] else f"{ANSI_GRAY}{attacker.name}{ANSI_RESET}"
            name_def = defender.name if not dead[defender.name] else f"{ANSI_GRAY}{defender.name}{ANSI_RESET}"
            print(f"{name_att} 攻擊 {name_def}，造成 {damage} 傷害！")
            if show_hp:
                name_disp = defender.name if not dead[defender.name] else f"{ANSI_GRAY}{defender.name}{ANSI_RESET}"
                print(f"攻擊後：{name_disp} HP={max(0, hp_def)}")
        # 判斷是否陣亡
        if hp_def <= 0:
            dead[defender.name] = True
            if verbose:
                print(f"{ANSI_GRAY}{defender.name} 戰敗！{ANSI_RESET}\n")
            break
        # 換手，攻守互換
        attacker, defender = defender, attacker
        hp_att, hp_def = hp_def, hp_att
    if verbose:
        print("戰鬥結束！")
        winner = attacker.name if hp_att > 0 else defender.name
        loser = defender.name if hp_att > 0 else attacker.name
        print(f"勝利者：{winner}")
        print(f"{ANSI_GRAY}{loser}（已陣亡）{ANSI_RESET}")
    # 回傳勝利者名字
    return attacker.name if hp_att > 0 else defender.name




# 遊戲主程式，負責流程控制
def main():
    print("[DEBUG] main start")
    print("[DEBUG] 程式啟動")
    print("三國武將 PK 版 - 赤壁戰役遊戲引擎")
    # 讀取武將資料
    generals = load_generals("generals.txt")
    # 判斷是否自動模式
    auto = '--auto' in sys.argv
    n_battles = 1
    # 支援 --auto=N 批次模擬
    for arg in sys.argv:
        if arg.startswith('--auto') and len(arg.split("=")) == 2:
            try:
                n_battles = int(arg.split("=")[1])
                if n_battles > 1000:
                    print("自動批次模擬場數過多，已自動限制為 1000 場。")
                    n_battles = 1000
                auto = True
            except Exception:
                pass
    # 取得所有勢力
    factions = list(sorted(set(g.faction for g in generals.values())))
    show_hp = True
    if '--no-hp' in sys.argv:
        show_hp = False
    # 批次自動模擬多場對戰
    if auto and n_battles > 1:
        print(f"自動批次模擬 {n_battles} 場對戰...")
        win_count = Counter()
        for i in range(n_battles):
            f1, f2 = random.sample(factions, 2)
            g1 = choose_general(generals, f1, auto=True)
            g2 = choose_general(generals, f2, auto=True)
            winner = battle(g1, g2, verbose=False, show_hp=show_hp)
            win_count[winner] += 1
        print("\n=== 批次模擬結果 ===")
        for name, cnt in win_count.most_common():
            print(f"{name} 勝場數：{cnt}")
    # 單場自動對戰
    elif auto:
        f1, f2 = random.sample(factions, 2)
        print(f"自動選擇玩家1勢力：{f1}")
        print(f"自動選擇玩家2勢力：{f2}")
        g1 = choose_general(generals, f1, auto=True)
        g2 = choose_general(generals, f2, auto=True)
        # 自動模式下強制顯示所有輸出
        battle(g1, g2, show_hp=show_hp)
    # 玩家互動模式
    else:
        print("\n請選擇雙方勢力：")
        for idx, f in enumerate(factions, 1):
            print(f"  {idx}. {f}")
        f1 = factions[int(input("請選擇玩家1勢力(輸入編號): "))-1]
        f2 = factions[int(input("請選擇玩家2勢力(輸入編號): "))-1]
        g1 = choose_general(generals, f1)
        g2 = choose_general(generals, f2)
        battle(g1, g2, show_hp=show_hp)
    print("[DEBUG] main end")

if __name__ == "__main__":
    main()
