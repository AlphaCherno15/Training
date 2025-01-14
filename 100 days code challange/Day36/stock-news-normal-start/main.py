import requests, json, datetime as dt
STOCK_LIST = {"tesla":"TSLA",
              }
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
KEY1 = "XMPXXBLW77WQ9I49"
KEY2 = "P7FEEGDXXECOBSTM"
def get_stock(stock):
    param = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_LIST[stock],
        "outputsize": "compact",
        "datatype": "json",
        "apikey": KEY1,
    }
    tsla_stock = requests.get(STOCK_ENDPOINT, params=param)
    tsla_stock.raise_for_status()
    return tsla_stock.json()
def get_news(news):
    param = {
        "q": news,
        "searchIn": "description",
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": "1c5a322ed48b46e39bae5f45f649dffb",
    }
    news = requests.get(NEWS_ENDPOINT, params=param)
    news.raise_for_status()
    return news.json()["articles"][:3]

def create_stock_file():
    try:
        with open(f"{company}_data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        dt = get_stock(company)
        with open(f"{company}_data.json", "w") as data_file:
            json.dump(dt, data_file, indent=4)
            data = dt
    finally:
        return data
def create_article_file():
    news = get_news(company)
    with open("article.json", "w") as data_file:
        json.dump(news, data_file, indent=4)
        data = news
    return data

def check():
    price = [float(price["4. close"]) for (day, price) in tsla_data["Time Series (Daily)"].items()]
    yesterday_closing = price[0]
    day_before_closing = price[1]
    x = abs(yesterday_closing  - day_before_closing)
    if x > yesterday_closing * 0.05:
        create_article_file()
    else:
        print("no significant change")

company = "tesla"
tsla_data = create_stock_file()
today = dt.date.today()
check()
create_article_file()






    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

