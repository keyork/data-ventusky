"""
@ File Name     :   getventusky.py
@ Time          :   2022/09/18
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   None
@ Function List :   func1() -- func desc1
@ Class List    :   Class1 -- class1 desc1
@ Details       :   None
"""

import requests
from bs4 import BeautifulSoup
from lxml import etree
import numpy as np


class VentuskyDataCrawler:
    def __init__(self):

        self.base_url = "https://www.ventusky.com/panel.php?link="
        self.url = None
        self.precipitation = None
        self.temperature = None

    def get_data(self, position):

        self.url = self.base_url + position
        req = requests.get(self.url)
        if req.status_code == 200:
            page_data = req.text
        else:
            page_data = "ERROR"
        return page_data

    def analy_data(self, contents):
        soup = BeautifulSoup(contents, "lxml")
        selector = etree.HTML(str(soup))
        precipitation = []
        for hour in range(24):
            precipitation.append(
                float(
                    selector.xpath(
                        '//*[@id="forecast"]/div[2]/table/tbody/tr/td['
                        + str(hour + 1)
                        + "]/span[2]"
                    )[0].text[0:-3]
                )
            )
        self.temperature = float(
            selector.xpath('//*[@id="meteogram"]/div[2]/div/div[1]/svg/g[6]/text[1]')[
                0
            ].text
        )
        self.precipitation = np.array(precipitation, dtype=float).max()


# if __name__ == "__main__":
#     crawler = VentuskyDataCrawler()
#     page_data = crawler.get_data("42.196;106.611")
#     crawler.analy_data(page_data)
#     print(crawler.precipitation)
#     print(crawler.temperature)
