import requests
import os
from lxml import etree

domain = "https://www.mass.gov/"
# https://www.mass.gov/info-details/archive-of-chapter-93-covid-19-data
# <a href="/doc/chapter-93-state-numbers-daily-report-october-22-2020/download">Chapter 93 State Numbers Daily Report - October 22, 2020</a>
def download(url):
    # url = "https://www.mass.gov/doc/chapter-93-state-numbers-daily-report-october-22-2020/download"
    file_name = url.split("/")[-2]
    res = requests.get(url=url)
    f = open("./temp/" + file_name + ".xlsx", "wb")
    f.write(res.content)
    f.close()


def get_lines_his():
    fname = "./temp/his.txt"
    if not os.path.isfile(fname):
        f = open(fname, "w")
        f.close()
        return None
    f = open(fname, "r")
    lines = f.readlines()
    f.close()
    if len(lines) == 0:
        return None
    return lines


def save_lines_his(new_file_name):
    f = open("./temp/his.txt", "a")
    f.writelines([new_file_name + "\n"])
    f.close()
    pass


if __name__ == "__main__":
    url = "https://www.mass.gov/doc/chapter-93-state-numbers-daily-report-october-22-2020/download"

    # download(url)
    # save_lines_his("test.txt")
