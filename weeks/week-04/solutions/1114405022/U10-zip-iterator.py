
# U10. zip 為何只能用一次（1.8）
# 本範例說明 zip 產生的是 iterator，只能消耗一次


prices = {'A': 2.0, 'B': 1.0}  # 一個字典，key 是商品名稱，value 是價格
z = zip(prices.values(), prices.keys())  # zip 產生一個 iterator，將 value 和 key 配對


min(z)  # OK，這裡會消耗掉 z 這個 iterator
# max(z)  # 會失敗，因為 z 已經被消耗完，iterator 只能用一次
