from rrg_db import DatabaseManager

dbM = DatabaseManager()
config = dbM.get_config()

dataSpy = dbM.get_data("spy")
#     0      1        2             3           4          5           6            7
# (symbol, date, closeWeekly, priceRelative, rsRatio, rsRatioAvg, rsMomentum, rsMomentumAvg)


def calc_priceIncrease(nowPrice, prevPrice):
    return 100 * (nowPrice / prevPrice)


for symbol in config["symbols"]:
    print("Processing symbol:", symbol)

    # calculate priceRelative
    dataEtf = dbM.get_data(symbol)

    for idx, val in enumerate(dataEtf):
        priceRelative = calc_priceIncrease(val[2], dataSpy[idx][2])
        dbM.insert_price_relative(symbol, val[1], priceRelative)

    dbM.commit()

    # calculate rsRatio
    dataEtf = dbM.get_data(symbol)

    for idx, val in enumerate(dataEtf):
        try:
            rsRatio = calc_priceIncrease(
                val[3], dataEtf[idx + config["rs_ratio_avg"] - 1][3]
            )
            dbM.insert_rs_ratio(symbol, val[1], rsRatio)
        except IndexError:
            break

    dbM.commit()

    # calculate rsRatioAvg
    dataEtf = dbM.get_data(symbol)

    for idx, val in enumerate(dataEtf):
        if dataEtf[idx + config["rs_ratio_avg"] - 1][4] is None:
            break

        rsRatioAvg = 0
        slicedList = dataEtf[idx : idx + config["rs_ratio_avg"]]

        for slic in slicedList:
            rsRatioAvg += slic[4]

        rsRatioAvg /= len(slicedList)

        dbM.insert_rs_ratio_avg(symbol, val[1], rsRatioAvg)

    dbM.commit()

    # calculate rsMomentum
    dataEtf = dbM.get_data(symbol)

    for idx, val in enumerate(dataEtf):
        if dataEtf[idx + config["rs_momentum_avg"] - 1][5] is None:
            break

        rsMomentum = calc_priceIncrease(
            val[5], dataEtf[idx + config["rs_momentum_avg"] - 1][5]
        )
        dbM.insert_rs_momentum(symbol, val[1], rsMomentum)

    dbM.commit()

    # calculate rsMomentumAvg
    dataEtf = dbM.get_data(symbol)

    for idx, val in enumerate(dataEtf):
        if dataEtf[idx + config["rs_momentum_avg"] - 1][6] is None:
            break

        rsMomentumAvg = 0
        slicedList = dataEtf[idx : idx + config["rs_momentum_avg"]]

        for slic in slicedList:
            rsMomentumAvg += slic[6]

        rsMomentumAvg /= len(slicedList)

        dbM.insert_rs_momentum_avg(symbol, val[1], rsMomentumAvg)

    dbM.commit()
