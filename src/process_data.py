from rrg_db import DatabaseManager

db = DatabaseManager()
config = db.get_config()

dataBenchmark = db.get_data(config["compare_to"])
#     0      1        2             3           4          5           6            7
# (symbol, date, closeWeekly, priceRelative, rsRatio, rsRatioAvg, rsMomentum, rsMomentumAvg)


def calc_priceIncrease(nowPrice, prevPrice):
    return 100 * (nowPrice / prevPrice)


for symbol in config["symbols"]:
    print("Processing symbol:", symbol)

    # calculate priceRelative
    dataEtf = db.get_data(symbol)

    for idx, val in enumerate(dataEtf):
        priceRelative = calc_priceIncrease(val[2], dataBenchmark[idx][2])
        db.insert_price_relative(symbol, val[1], priceRelative)

    db.commit()

    # calculate rsRatio
    dataEtf = db.get_data(symbol)

    for idx, val in enumerate(dataEtf):
        try:
            rsRatio = calc_priceIncrease(
                val[3], dataEtf[idx + config["rs_ratio_avg"] - 1][3]
            )
            db.insert_rs_ratio(symbol, val[1], rsRatio)
        except IndexError:
            break

    db.commit()

    # calculate rsRatioAvg
    dataEtf = db.get_data(symbol)

    for idx, val in enumerate(dataEtf):
        if dataEtf[idx + config["rs_ratio_avg"] - 1][4] is None:
            break

        rsRatioAvg = 0
        slicedList = dataEtf[idx : idx + config["rs_ratio_avg"]]

        for slic in slicedList:
            rsRatioAvg += slic[4]

        rsRatioAvg /= len(slicedList)

        db.insert_rs_ratio_avg(symbol, val[1], rsRatioAvg)

    db.commit()

    # calculate rsMomentum
    dataEtf = db.get_data(symbol)

    for idx, val in enumerate(dataEtf):
        if dataEtf[idx + config["rs_momentum_avg"] - 1][5] is None:
            break

        rsMomentum = calc_priceIncrease(
            val[5], dataEtf[idx + config["rs_momentum_avg"] - 1][5]
        )
        db.insert_rs_momentum(symbol, val[1], rsMomentum)

    db.commit()

    # calculate rsMomentumAvg
    dataEtf = db.get_data(symbol)

    for idx, val in enumerate(dataEtf):
        if dataEtf[idx + config["rs_momentum_avg"] - 1][6] is None:
            break

        rsMomentumAvg = 0
        slicedList = dataEtf[idx : idx + config["rs_momentum_avg"]]

        for slic in slicedList:
            rsMomentumAvg += slic[6]

        rsMomentumAvg /= len(slicedList)

        db.insert_rs_momentum_avg(symbol, val[1], rsMomentumAvg)

    db.commit()
