
# R19. 轉換+聚合：生成器表達式（1.19）
# 本範例示範如何用生成器表達式進行轉換與聚合運算


nums = [1, 2, 3]  # 一個整數列表
sum(x * x for x in nums)  # 用生成器表達式計算每個元素的平方和，結果為 1+4+9=14


s = ('ACME', 50, 123.45)  # 一個 tuple，包含字串與數字
','.join(str(x) for x in s)  # 將 tuple 內所有元素轉成字串後用逗號連接，結果為 'ACME,50,123.45'


portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]  # 股票投資組合，每個元素是字典
min(s['shares'] for s in portfolio)  # 找出 shares 欄位的最小值，結果為 20
min(portfolio, key=lambda s: s['shares'])  # 找出 shares 欄位最小的那個字典，結果為 {'name': 'AOL', 'shares': 20}
