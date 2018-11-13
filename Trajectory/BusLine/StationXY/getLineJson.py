import pandas as pd
import json
import random


def SplitLine(stationFilePath, OutPath1, OutPath2, NewstationFilePath):
    # read to dataframe
    station_df = pd.read_csv(stationFilePath)

    stationDic = {}
    stationNoName = []
    station_df["线路ID"] = station_df["线路ID"].apply(
        lambda x: x[0:x.find("(")])

    stationID = station_df["线路ID"].unique()

    random.shuffle(stationID)

    count = 0
    for i in stationID:
        temp = (station_df.loc[station_df["线路ID"] == i])

        XYlist = temp[["经度", "纬度"]].values.tolist()

        XYFlat_list = [item for sublist in XYlist for item in sublist]

        stationDic[i] = XYFlat_list

        stationNoName.append(XYFlat_list)

        count += 1
        if count > 500:
            break


    fp = open(OutPath1, 'w', encoding='utf-8')
    json.dump(stationDic, fp, ensure_ascii=False, indent=4)

    fp = open(OutPath2, 'w', encoding='utf-8')
    json.dump(stationNoName, fp, ensure_ascii=False, indent=4)

    station_df.to_csv(NewstationFilePath, index=False)


if __name__ == "__main__":

    # 上行为0，下行为2
    for i in range(0, 2):
        stationFilePath = "E:\\SODA_use\\BusStationXY\\allBus_" + \
            str(i) + ".csv"
        NewstationFilePath = "E:\\SODA_use\\BusStationXY\\newallBus_" + \
            str(i) + ".csv"
        OutPath1 = "E:\\SODA_use\\BusStationXY\\jsonBus_" + str(i) + ".json"
        OutPath2 = "E:\\SODA_use\\BusStationXY\\jsonBusNoName_" + \
            str(i) + ".json"

        SplitLine(stationFilePath, OutPath1, OutPath2, NewstationFilePath)
