import requests
import websocket
from websocket import create_connection

import json

class VitexRestApi:  
    def __init__(self, key = None, signature = None):
        self.base_url = "https://api.vitex.net"
        self.key = key
        self.signature = signature      
    
    # Private REST API
    def place_order_test(self, symbol = None, amount = None, price = None, side = None):
        url = self.base_url + "/api/v2/order/test"
        params = {'symbol':symbol, 'amount':amount, 'price':price, 'side':side, 'timestamp':self.get_server_time(), 'key':self.key, 'signature':self.signature}
        res = requests.post(url, params)
        return res.json();

    def place_order(self, symbol = None, amount = None, price = None, side = None):
        url = self.base_url + "/api/v2/order"
        params = {'symbol':symbol, 'amount':amount, 'price':price, 'side':side, 'timestamp':self.get_server_time(), 'key':self.key, 'signature':self.signature}
        res = requests.post(url, params)
        return res.json();

    def cancel_order(self, symbol = None, orderId = None):
        url = self.base_url + "/api/v2/order"
        params = {'symbol':symbol, 'orderId':orderId, 'timestamp':self.get_server_time(), 'key':self.key, 'signature':self.signature}
        res = requests.delete(url, params)
        return res.json();

    def cancel_all_order(self, symbol = None):
        url = self.base_url + "/api/v2/order"
        params = {'symbol':symbol, 'timestamp':self.get_server_time(), 'key':self.key, 'signature':self.signature}
        res = requests.delete(url, params)
        return res.json();

    # Public REST API
    def get_order_limit(self):
        url = self.base_url + "/api/v2/limit"
        res = requests.get(url)
        return res.json();

    def get_all_tokens(self, category = None, tokenSymbolLike = None, offset = None, limit = None):
        url = self.base_url + "/api/v2/tokens"
        params = {'category':category, 'tokenSymbolLike':tokenSymbolLike, 'offset':offset, 'limit':limit}
        res = requests.get(url)
        return res.json();

    def get_token_detail(self, tokenSymbol = None, tokenId = None):
        url = self.base_url + "/api/v2/token/detail"
        params = {'tokenSymbol':tokenSymbol,'tokenId':tokenId} 
        res = requests.get(url, params)
        return res.json();

    def get_listed_tokens(self, quoteTokenSymbol = None):
        url = self.base_url + "/api/v2/token/mapped"
        params = {'quoteTokenSymbol':quoteTokenSymbol} 
        res = requests.get(url, params)
        return res.json();

    def get_unlisted_tokens(self, quoteTokenSymbol = None):
        url = self.base_url + "/api/v2/token/unmapped"
        params = {'quoteTokenSymbol':quoteTokenSymbol} 
        res = requests.get(url, params)
        return res.json();

    def get_trading_pair(self, symbol = None):
        url = self.base_url + "/api/v2/market"
        params = {'symbol':symbol} 
        res = requests.get(url, params)
        return res.json();

    def get_all_trading_pairs(self, offset = None, limit = None):
        url = self.base_url + "/api/v2/markets"
        params = {'offset':offset, 'limit':limit} 
        res = requests.get(url, params)
        return res.json();

    def get_order(self, address = None, orderId = None):
        url = self.base_url + "/api/v2/order"
        params = {'address':address, 'orderId':orderId} 
        res = requests.get(url, params)
        return res.json();

    def get_open_order(self, address = None, symbol = None, quoteTokenSymbol = None, tradeTokenSymbol = None, offset = None, limit = None, total = None):
        url = self.base_url + "/api/v2/orders/open"
        params = {'address':address, 'symbol':symbol, 'quoteTokenSymbol':quoteTokenSymbol, 'tradeTokenSymbol':tradeTokenSymbol, 'offset':offset, 'limit':limit, 'total':total} 
        res = requests.get(url, params)
        return res.json();

    def get_orders(self, address = None, symbol = None, quoteTokenSymbol = None, tradeTokenSymbol = None, startTime = None, endTime = None, side = None, status = None, offset = None, limit = None, total = None):
        url = self.base_url + "/api/v2/orders"
        params = {'address':address, 'symbol':symbol, 'quoteTokenSymbol':quoteTokenSymbol, 'tradeTokenSymbol':tradeTokenSymbol, 'startTime':startTime, 'endTime':endTime, 'side':side, 'status':status, 'offset':offset, 'limit':limit, 'total':total} 
        res = requests.get(url, params)
        return res.json();

    def get_24hr_ticker_price_changes(self, symbol = None, quoteTokenSymbol = None):
        url = self.base_url + "/api/v2/ticker/24hr"
        params = {'symbol':symbol, 'quoteTokenSymbol':quoteTokenSymbol} 
        res = requests.get(url, params)
        return res.json();

    def get_order_book_ticker(self, symbol = None):
        url = self.base_url + "/api/v2/ticker/bookTicker"
        params = {'symbol':symbol} 
        res = requests.get(url, params)
        return res.json();   

    def get_trade_summary(self, symbol = None, limit = None):
        url = self.base_url + "/api/v2/trades"
        params = {'symbol':symbol,'limit':limit} 
        res = requests.get(url, params)
        return res.json();   

    def get_trade_records(self, symbol = None, orderId = None, startTime = None, endTime = None, side = None, offset = None, limit = None, total = None):
        url = self.base_url + "/api/v2/trades/all"
        params = {'symbol':symbol,'orderId':orderId,'startTime':startTime,'endTime':endTime,'side':side,'offset':offset,'limit':limit,'total':total} 
        res = requests.get(url, params)
        return res.json();  

    def get_order_book_depth(self, symbol = None, limit = None, precision = None):
        url = self.base_url + "/api/v2/depth"
        params = {'symbol':symbol,'limit':limit} 
        res = requests.get(url, params)
        return res.json();   

    def get_klines_candlestick_bars(self, symbol = None, interval = None, limit = None, startTime = None, endTime = None):
        url = self.base_url + "/api/v2/klines"
        params = {'symbol':symbol,'interval':interval,'limit':limit,'startTime':startTime,'endTime':endTime} 
        res = requests.get(url, params)
        return res.json();   

    def get_deposit_withdrawal_records(self, address = None, tokenId = None, offset = None, limit = None):
        url = self.base_url + "/api/v2/deposit-withdraw"
        params = {'address':address,'tokenId':tokenId,'offset':offset,'limit':limit} 
        res = requests.get(url, params)
        return res.json();   

    def get_exchante_rate(self, tokenSymbols = None, tokenIds = None):
        url = self.base_url + "/api/v2/exchange-rate"
        params = {'tokenSymbols':tokenSymbols,'tokenIds':tokenIds} 
        res = requests.get(url, params)
        return res.json();   

    def get_usd_cny_rate(self):
        url = self.base_url + "/api/v2/usd-cny"
        res = requests.get(url)
        return res.json();   

    def get_exchante_balance(self, address = None):
        url = self.base_url + "/api/v2/balance"
        params = {'address':address} 
        res = requests.get(url,params)
        return res.json();   

    def get_trade_mining_info(self):
        url = self.base_url + "/api/v2/trade_fee_info"
        res = requests.get(url)
        return res.json();   

    def get_server_time(self):
        url = self.base_url + "/api/v2/time"
        res = requests.get(url)
        return res.json();   

    def get_server_time_stamp(self):
        url = self.base_url + "/api/v2/timestamp"
        res = requests.get(url)
        return res.json();   

class VitexWebSocket: 
    def __init__(self, clientId, opType, topics):
        self.dest_uri = "wss://api.vitex.net/ws"
        self.msg = '{"clientId":"' + clientId + '",  "opType":"' + opType + '",  "topics":"' + topics + '"}'
        return;

    def response(self):
        ws = create_connection(self.dest_uri)
        ws.send(self.msg)
        result =  ws.recv()
        ws.close()
        return result;
