import json
import sys
import requests
import time
import csv


apikey='jIEHPVdf8227Vj0QfSs7H5wIrowhRVWi9wvTGjVp'


url = "https://yfapi.net/v6/finance/quote"


quote = sys.argv[1]
querystring = {"symbols":quote}
headers = {
'x-api-key': apikey
}

response = requests.request("GET", url, headers=headers, params=querystring)

stock_json = response.json()


if stock_json['quoteResponse']['result'][0]["triggerable"]==False:
    print("Please reenter the ticker")
else:
    mkt_time = stock_json['quoteResponse']['result'][0]["regularMarketTime"]
    mkt_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(mkt_time))
    price = stock_json['quoteResponse']['result'][0]["regularMarketPrice"]
    name = stock_json['quoteResponse']['result'][0]["shortName"]


    print(name,
        "Current Price:$" + str(price),
            "Market Time:" + mkt_time)

    ticker = stock_json['quoteResponse']['result'][0]["symbol"]
    file_out = [str(ticker) + ',' + str(mkt_time) + ',' + str(price)]

    with open('Quiz.csv','a') as csv_file:
        output_data = csv.writer(csv_file, delimiter = '\t')
        output_data.writerow(file_out)
        csv_file.close()
