import sys
from collections import namedtuple, Counter, defaultdict

General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

def load_generals(filename):
    generals = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == 'EOF':
                break
            if not line:
                continue
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

def choose_general(generals, faction):
    candidates = [g for g in generals.values() if g.faction == faction]
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

def battle(g1, g2):
    print(f"\n戰鬥開始：{g1.name} vs {g2.name}")
    hp1, hp2 = g1.hp, g2.hp
    turn = 0
    while hp1 > 0 and hp2 > 0:
        turn += 1
        print(f"\n--- 第{turn}回合 ---")
        # 速度高者先攻
        if g1.spd >= g2.spd:
            attacker, defender = g1, g2
            hp_att, hp_def = hp1, hp2
        else:
            attacker, defender = g2, g1
            hp_att, hp_def = hp2, hp1
        # 攻擊
        damage = max(1, attacker.atk - defender.def_)
        hp_def -= damage
        print(f"{attacker.name} 攻擊 {defender.name}，造成 {damage} 傷害！")
        if hp_def <= 0:
            print(f"{defender.name} 戰敗！\n")
            break
        # 換手
        if attacker == g1:
            hp2 = hp_def
        else:
            hp1 = hp_def
        # 反擊
        damage = max(1, defender.atk - attacker.def_)
        hp_att -= damage
        print(f"{defender.name} 反擊 {attacker.name}，造成 {damage} 傷害！")
        if hp_att <= 0:
            print(f"{attacker.name} 戰敗！\n")
            break
        if attacker == g1:
            hp1 = hp_att
        else:
            hp2 = hp_att
        print(f"目前血量：{g1.name}({hp1})  {g2.name}({hp2})")
    print("戰鬥結束！")
    if hp1 > 0:
        print(f"勝利者：{g1.name}")
    else:
        print(f"勝利者：{g2.name}")

def main():
    print("三國武將 PK 版 - 赤壁戰役遊戲引擎")
    generals = load_generals("weeks/week-07/generals.txt")
    print("\n請選擇雙方勢力：")
    factions = list(sorted(set(g.faction for g in generals.values())))
    for idx, f in enumerate(factions, 1):
        print(f"  {idx}. {f}")
    f1 = factions[int(input("請選擇玩家1勢力(輸入編號): "))-1]
    f2 = factions[int(input("請選擇玩家2勢力(輸入編號): "))-1]
    g1 = choose_general(generals, f1)
    g2 = choose_general(generals, f2)
    battle(g1, g2)

if __name__ == "__main__":
    main()
