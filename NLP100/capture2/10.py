
filepath = 'hightemp.txt'
with open(filepath, mode='rt', encoding='utf-8') as f:
    s = f.readlines()
print(s[:3])
