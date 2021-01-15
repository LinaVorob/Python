import json
with open('Firms.txt', encoding='utf-8') as f:
    firms = {}
    average_profit = []
    for el in f.readlines():
        el = el.split("   ")
        firms[el[0]] = float(el[2]) - float(el[3].strip())
        if firms[el[0]] > 0:
            average_profit.append(firms[el[0]])
with open('firms.json', 'w') as f_j:
    json.dump([firms, dict(average_profit=sum(average_profit) / len(average_profit))], f_j)
