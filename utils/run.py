"""
@ File Name     :   run.py
@ Time          :   2022/09/18
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   None
@ Function List :   func1() -- func desc1
@ Class List    :   Class1 -- class1 desc1
@ Details       :   None
"""

from getventusky import VentuskyDataCrawler
import json
import argparse
import numpy as np

DELTA_LON = 30
DELTA_LAT = 30
ROOT_PATH = "./data/"


def get_data(args):

    start_lon = float(args.longitude)
    start_lat = float(args.latitude)
    crawler = VentuskyDataCrawler()
    data_list = []
    for lon in np.linspace(
        start_lon, start_lon + DELTA_LON, DELTA_LON * 4, endpoint=False
    ):
        print(lon)
        for lat in np.linspace(
            start_lat, start_lat + DELTA_LAT, DELTA_LAT * 4, endpoint=False
        ):
            page_data = crawler.get_data(str(lon) + ";" + str(lat))
            if page_data == "ERROR":
                continue
            crawler.analy_data(page_data)
            data_dict = {
                "coord": [lon, lat],
                "max_temperature": crawler.temperature,
                "max_precipitation": crawler.precipitation,
            }
            data_list.append(data_dict)
    with open(ROOT_PATH + str(start_lon) + "_" + str(start_lat) + ".json", "w") as f:
        json.dump(data_list, f)
        print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--longitude", help="longitude 经度")
    parser.add_argument("--latitude", help="latitude 纬度")
    args = parser.parse_args()

    get_data(args)
