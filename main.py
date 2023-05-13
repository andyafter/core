import os
import sys
import time
import socket
import requests
from pprint import pprint

import ccxt

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')


exchange = ccxt.kucoin({
    'apiKey':  os.environ.get('KUCOIN_API_KEY'),
    'secret': os.environ.get('KUCOIN_API_SECRET'),
    'password': os.environ.get('KUCOIN_API_PASSPHRASE'),
})

balance = exchange.fetch_balance()
print(balance)

symbol = 'BTC/USDC'
order_type = 'limit'
side = 'buy'
amount = 0.0001
order_price = 13500  # below the stopLossPrice and above the takeProfitPrice
stop_trigger_params = {
    'triggerPrice': '14000',
    'leverage': 2,  # defaults to 1
}
# stop_loss_params = {
#     'stopLossPrice': '15000',  # the price that triggers the order_price order
#     'leverage': 1,
# }
# take_profit_params = {
#     'takeProfitPrice': '17000',  # the price that triggers the order_price order
#     'leverage': 1,
# }

try:
    start_time = time.time()
    stop_trigger_order = exchange.create_order(symbol, order_type, side, amount, order_price, stop_trigger_params)
    elapsed_time = time.time() - start_time
    print("Time taken to place order: {} seconds".format(elapsed_time))
    # addr_info = socket.getaddrinfo("api.kucoin.com", None)
    # ip_address = addr_info[0][-1][0]

    # print(f'API is hosted at: {ip_address}')
    # print(addr_info)
    # stop_loss_order = exchange.create_order(symbol, order_type, side, amount, order_price, stop_loss_params)
    # take_profit_order = exchange.create_order(symbol, order_type, side, amount, order_price, take_profit_params)
    # pprint(stop_trigger_order)
    # pprint(stop_loss_order)
    # pprint(take_profit_order)
except Exception as err:
    print(err)