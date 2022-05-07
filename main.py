import requests
import time

# Global variables
# bitcoin api
api_key = "*****"

# telegram bot
bot_key = "*****"

# telegram chat id
chat_id = "*****"

# limit of bitcoin
BTC_limit = 47100
# limit of yearn.finance
# YFI_limit = 31250
YFI_limit = 38000

# variation of the cryptocurrency
variation = 300

# 20 minutes
time_interval = 20 * 30


def get_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers).json()
    crypto = []
    for elt in response["data"]:
        if elt["name"] == "yearn.finance" or elt["name"] == "Bitcoin":
            crypto.append(elt)

    BTC_price = crypto[0]["quote"]["USD"]["price"]
    # print(BTC_price)
    YFI_price = crypto[1]["quote"]["USD"]["price"]
    # print(YFI_price)

    return BTC_price, YFI_price


def send_update(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)


def main():
    while True:
        price = get_price()
        message = ""

        print(price)
        if price[0] < BTC_limit - variation:
            # print(price)
            message = message + f"le prix du bitcoin a diminuer. prix : {round(price[0], 3)} $,\net la limite était : {BTC_limit} $\ndonc la différence est de : {round(price[0]-BTC_limit, 3)} $\nbonne idée d'acheter maintenant\n\n"
            # send_update(chat_id, f"se3r el bitcoin wety w ba2a : {price} $,\nmomken teshteri naw\n \n")
        if price[0] > BTC_limit + variation:
            # print(price)
            message = message + f"le prix du bitcoin a augmenter. prix : {round(price[0], 3)} $,\net la limite était : {BTC_limit} $\ndonc la différence est de : {round(price[0]-BTC_limit, 3)} $\nbonne idée de vendre maintenant\n\n"
            # send_update(chat_id, f"se3r el bitcoin 3ely w ba2a : {price} $, momken tebi3 naw")

        if price[1] < YFI_limit + variation:
            # print(price)
            message = message + f"le prix du yearn finance a diminuer. prix : {round(price[1], 3)} $,\net la limite était : {YFI_limit} $\ndonc la différence est de : {round(price[1]-YFI_limit, 3)} $\nbonne idée d'acheter maintenant\n\n"
        if price[1] > YFI_limit + variation:
            # print(price)
            message = message + f"le prix du yearn finance a augmenter. prix : {round(price[1], 3)} $,\net la limite était : {YFI_limit} $\ndonc la différence est de : {round(price[1]-YFI_limit, 3)} $\nbonne idée de vendre maintenant\n\n "

        if message != "":
            send_update(chat_id, message)

        time.sleep(time_interval)


main()
