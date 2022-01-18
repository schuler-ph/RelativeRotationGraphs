from rrg_db import DatabaseManager

dbM = DatabaseManager()

symbol = "xlk"

dataSpy = dbM.get_data("spy")
dataEtf = dbM.get_data(symbol)

#     0      1        2             3           4          5           6            7
# (symbol, date, closeWeekly, priceRelative, rsRatio, rsRatioAvg, rsMomentum, rsMomentumAvg)

def calc_priceRelative(dataSpy, dataEtf):
    return 100 * (dataEtf / dataSpy)

for idx, val in enumerate(dataSpy):
    priceRelative = calc_priceRelative(val[2], dataEtf[idx][2])
    dbM.insert_price_relative(symbol, val[1], priceRelative)

dbM.commit()
dataEtf = dbM.get_data(symbol)

print(len(dataEtf))
print(dataEtf[0][1])
