"""
Analyze the excel data
"""

import xlrd
import crawler


def get_table():
    # get local historical data
    lines = crawler.get_lines_his()

    if lines is None:
        return []

    # newest excel
    file_name = lines[-1].replace("\n", "") + ".xlsx"
    book = xlrd.open_workbook("./temp/" + file_name)
    sheet_test = book.sheet_by_index(0)

    sheet_pos_24 = book.sheet_by_index(2)
    sheet_tested = book.sheet_by_index(1)
    sheet_pos = book.sheet_by_index(3)

    start_index = 27
    end_index = 378
    infos = []

    for i in range(start_index, end_index + 1):
        row_values_test = sheet_test.row_values(i)
        data = {}
        infos.append(data)
        data["city"] = row_values_test[0]
        for j in range(1, 14 + 1):
            value = row_values_test[-j]
            if value == "<5":
                value = 5
            # past 4 days data
            data["last14test"] = int(data.get("last14test", 0) + value)

        row_values_pos_24 = sheet_pos_24.row_values(i)

        for j in range(1, 14 + 1):
            value = row_values_pos_24[-j]
            if value == "<5":
                value = 5
            # past 14 days' positive cases
            data["last14pos"] = int(data.get("last14pos", 0) + value)

        if data["last14test"] == 0:
            data["rate_pos"] = 0
        else:
            # % of past 14 days' positive cases
            data["rate_pos"] = (
                str("%.4f" % (data["last14pos"] / data["last14test"] * 100)) + "%"
            )

        row_values_tested = sheet_tested.row_values(i)

        if row_values_tested[2] == "<5":
            row_values_tested[2] = 5

        if row_values_tested[1] == "<5":
            row_values_tested[1] = 5

        test_sum = row_values_tested[2] + row_values_tested[1]

        # count total tests that have been done
        data["test_sum"] = int(test_sum) + data["last14test"]

        row_values_pos = sheet_pos.row_values(i)

        # print(row_values_pos[2])
        # print(row_values_pos[1])

        if row_values_pos[2] == "<5":
            row_values_pos[2] = 5
        if row_values_pos[1] == "<5":
            row_values_pos[1] = 5

        pos_sum = row_values_pos[2] + row_values_pos[1]

        # count total positive cases
        data["pos_sum"] = int(pos_sum) + data["last14pos"]
        if data["pos_sum"] == 0:
            data["Positive_Rate_per_100000"] = 0
        else:
            # % of positive cases
            data["Positive_Rate_per_100000"] = "%.2f" % (
                data["pos_sum"] / data["test_sum"] * 100000
            )

    return infos


def get_infos():
    return crawler.search_school()


if __name__ == "__main__":
    #data = get_table("chapter-93-state-numbers-daily-report-october-22-2020.xlsx")
    #print(data)
    pass
