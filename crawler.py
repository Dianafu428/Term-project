import requests
import os
from lxml import etree

domain = "https://www.mass.gov/"
# https://www.mass.gov/info-details/archive-of-chapter-93-covid-19-data
# <a href="/doc/chapter-93-state-numbers-daily-report-october-22-2020/download">Chapter 93 State Numbers Daily Report - October 22, 2020</a>
def download(url):
    # down load the file
    # url = "https://www.mass.gov/doc/chapter-93-state-numbers-daily-report-october-22-2020/download"
    file_name = url.split("/")[-2]
    res = requests.get(url=url)
    f = open("./temp/" + file_name + ".xlsx", "wb")
    f.write(res.content)
    f.close()


def get_lines_his():
    """
    search to update info from local
    """
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
    """save the updated info into local file"""
    f = open("./temp/his.txt", "a")
    f.writelines([new_file_name + "\n"])
    f.close()
    pass


def try_download_file(url):
    lines = get_lines_his()
    file_name = url.split("/")[-2]
    if lines is None:
        download(url)
        save_lines_his(file_name)
        return False
    if file_name == lines[-1].replace("\n", ""):
        return False

    download(url)
    save_lines_his(file_name)
    return True


def search_web_page():
    """web page excel crawler"""

    # request data
    url = "https://www.mass.gov/info-details/archive-of-chapter-93-covid-19-data"
    res = requests.get(url)
    res.encoding = "utf-8"
    selector = etree.HTML(res.text)

    xlsx_url = selector.xpath(
        '//*[@id="main-content"]/div[2]/div/div/section[1]/div/div/ul/li[1]/ul/li[2]/a/@href'
    )
    # print(xlsx_url)
    if len(xlsx_url) == 0:
        return False

    return try_download_file(domain + xlsx_url[0])


def search_school():
    """Babson College COVID 19 Dashboard crawler"""

    res = requests.get(
        url="https://www.babson.edu/emergency-preparedness/return-to-campus/covid-dashboard/"
    )
    # res.encoding = 'utf-8'

    # put page info into different selector
    selector = etree.HTML(res.text)
    data1 = selector.xpath(
        '//*[@id="id-1251114"]/table/thead/tr[2]/td[3]/table/tbody/tr[2]/td[2]/span/text()'
    )
    data2 = selector.xpath(
        '//*[@id="id-1251114"]/table/thead/tr[2]/td[3]/table/tbody/tr[3]/td[2]/span/text()'
    )
    data3 = selector.xpath(
        '//*[@id="id-1251114"]/table/thead/tr[2]/td[3]/table/tbody/tr[4]/td[2]/span/text()'
    )
    days_7 = []
    days_7.append("Students: " + " ".join(" ".join(data1).split()))
    days_7.append("Employees: " + " ".join(" ".join(data2).split()))
    days_7.append("Service Providers: " + " ".join(" ".join(data3).split()))

    since_aug = []
    data1 = selector.xpath(
        '//*[@id="id-1248929"]/table/thead/tr[2]/td[3]/table/tbody/tr[2]/td[2]/span/text()'
    )
    data2 = selector.xpath(
        '//*[@id="id-1248929"]/table/thead/tr[2]/td[3]/table/tbody/tr[3]/td[2]/span/text()'
    )
    data3 = selector.xpath(
        '//*[@id="id-1248929"]/table/thead/tr[2]/td[3]/table/tbody/tr[4]/td[2]/span/text()'
    )
    since_aug.append("Students: " + " ".join(" ".join(data1).split()))
    since_aug.append("Employees: " + " ".join(" ".join(data2).split()))
    since_aug.append("Service Providers: " + " ".join(" ".join(data3).split()))

    print(days_7, since_aug)

    return days_7, since_aug


if __name__ == "__main__":
    url = "https://www.mass.gov/doc/chapter-93-state-numbers-daily-report-october-22-2020/download"

    # download(url)
    # save_lines_his("test.txt")
    # try_download_file(url)
    # search_web_page()
    # search_school()
    pass
