"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab 4.                                                                                     -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: danielperhez                                                                               -- #                                                                            -- #
# -- repository: https://github.com/danielperhez/Modulo4_MyST                                       -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

from symtable import Symbol
import ccxt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sympy import limit
import time
import plotly.express as px
import math
import plotly.graph_objects as go

def cxt(minutes):

    timeframe = []

    # Arrays Bitso
    bid_bitso_btc = []
    ask_bitso_btc = []
    vol_ask_bitso_btc = []
    vol_bid_bitso_btc = []
    spread_bitso_btc = []
    bid_bitso_eth = []
    ask_bitso_eth = []
    vol_ask_bitso_eth = []
    vol_bid_bitso_eth = []
    spread_bitso_eth = []
    bid_bitso_ltc = []
    ask_bitso_ltc = []
    vol_ask_bitso_ltc = []
    vol_bid_bitso_ltc = []
    spread_bitso_ltc = []

    # Arrays Kraken
    bid_kraken_btc = []
    ask_kraken_btc = []
    vol_ask_kraken_btc = []
    vol_bid_kraken_btc = []
    spread_kraken_btc = []
    bid_kraken_eth = []
    ask_kraken_eth = []
    vol_ask_kraken_eth = []
    vol_bid_kraken_eth = []
    spread_kraken_eth = []
    bid_kraken_ltc = []
    ask_kraken_ltc = []
    vol_ask_kraken_ltc = []
    vol_bid_kraken_ltc = []
    spread_kraken_ltc = []

    # Arrays Binance
    bid_binance_btc = []
    ask_binance_btc = []
    vol_ask_binance_btc = []
    vol_bid_binance_btc = []
    spread_binance_btc = []
    bid_binance_eth = []
    ask_binance_eth = []
    vol_ask_binance_eth = []
    vol_bid_binance_eth = []
    spread_binance_eth = []
    bid_binance_ltc = []
    ask_binance_ltc = []
    vol_ask_binance_ltc = []
    vol_bid_binance_ltc = []
    spread_binance_ltc = []


    for x in range(minutes):

        # seleccionamos los exchanges
        bitso = ccxt.bitso()
        kraken = ccxt.kraken()
        binance = ccxt.zonda()

        # seleccionamos los symbolos para Bitso, hacemos limit de Order Book
        limit = 30
        bi_btc_ob = bitso.fetch_order_book('BTC/USDT',limit=limit)
        bi_eth_ob = bitso.fetch_order_book('ETH/USD',limit=limit)
        bi_ltc_ob = bitso.fetch_order_book('LTC/MXN',limit=limit)

        # seleccionamos los symbolos para Kraken, hacemos limit de Order Book
        kr_btc_ob = kraken.fetch_order_book('BTC/USDT',limit=limit)
        kr_eth_ob = kraken.fetch_order_book('ETH/USD',limit=limit)
        kr_ltc_ob = kraken.fetch_order_book('LTC/USD',limit=limit)

        # seleccionamos los symbolos para Binance, hacemos limit de Order Book
        bin_btc_ob = binance.fetch_order_book('BTC/USDT',limit=limit)
        bin_eth_ob = binance.fetch_order_book('ETH/USDT',limit=limit)
        bin_ltc_ob = binance.fetch_order_book('LTC/USDT',limit=limit)

        # Información de Bitso
        bid_bit_btc = bi_btc_ob['bids'][0][0] if len(bi_btc_ob['bids']) > 0 else None
        ask_bit_btc = bi_btc_ob['asks'][0][0] if len(bi_btc_ob['asks']) > 0 else None
        spread_bit_btc = (ask_bit_btc - bid_bit_btc) if (ask_bit_btc and bid_bit_btc) else None
        vol_ask_bit_btc = bi_btc_ob['asks'][0][1] if len(bi_btc_ob['bids']) > 0 else None
        vol_bid_bit_btc = bi_btc_ob['bids'][0][1] if len(bi_btc_ob['asks']) > 0 else None

        bid_bit_eth = bi_eth_ob['bids'][0][0] if len(bi_eth_ob['bids']) > 0 else None
        ask_bit_eth = bi_eth_ob['asks'][0][0] if len(bi_eth_ob['asks']) > 0 else None
        spread_bit_eth = (ask_bit_eth - bid_bit_eth) if (ask_bit_eth and bid_bit_eth) else None
        vol_ask_bit_eth = bi_eth_ob['asks'][0][1] if len(bi_eth_ob['bids']) > 0 else None
        vol_bid_bit_eth = bi_eth_ob['bids'][0][1] if len(bi_eth_ob['asks']) > 0 else None

        bid_bit_ltc = bi_ltc_ob['bids'][0][0] if len(bi_ltc_ob['bids']) > 0 else None
        ask_bit_ltc = bi_ltc_ob['asks'][0][0] if len(bi_ltc_ob['asks']) > 0 else None
        spread_bit_ltc = (ask_bit_ltc - bid_bit_ltc) if (ask_bit_ltc and bid_bit_ltc) else None
        vol_ask_bit_ltc = bi_ltc_ob['asks'][0][1] if len(bi_ltc_ob['bids']) > 0 else None
        vol_bid_bit_ltc = bi_ltc_ob['bids'][0][1] if len(bi_ltc_ob['asks']) > 0 else None

        # Información de Kraken
        bid_kra_btc = kr_btc_ob['bids'][0][0] if len(kr_btc_ob['bids']) > 0 else None
        ask_kra_btc = kr_btc_ob['asks'][0][0] if len(kr_btc_ob['asks']) > 0 else None
        spread_kra_btc = (ask_kra_btc - bid_kra_btc) if (ask_kra_btc and bid_kra_btc) else None
        vol_ask_kra_btc = kr_btc_ob['asks'][0][1] if len(kr_btc_ob['bids']) > 0 else None
        vol_bid_kra_btc = kr_btc_ob['bids'][0][1] if len(kr_btc_ob['asks']) > 0 else None

        bid_kra_eth = kr_eth_ob['bids'][0][0] if len(kr_eth_ob['bids']) > 0 else None
        ask_kra_eth = kr_eth_ob['asks'][0][0] if len(kr_eth_ob['asks']) > 0 else None
        spread_kra_eth = (ask_kra_eth - bid_kra_eth) if (ask_kra_eth and bid_kra_eth) else None
        vol_ask_kra_eth = kr_eth_ob['asks'][0][1] if len(kr_eth_ob['bids']) > 0 else None
        vol_bid_kra_eth = kr_eth_ob['bids'][0][1] if len(kr_eth_ob['asks']) > 0 else None

        bid_kra_ltc = kr_ltc_ob['bids'][0][0] if len(kr_ltc_ob['bids']) > 0 else None
        ask_kra_ltc = kr_ltc_ob['asks'][0][0] if len(kr_ltc_ob['asks']) > 0 else None
        spread_kra_ltc = (ask_kra_ltc - bid_kra_ltc) if (ask_kra_ltc and bid_kra_ltc) else None
        vol_ask_kra_ltc = kr_ltc_ob['asks'][0][1] if len(kr_ltc_ob['bids']) > 0 else None
        vol_bid_kra_ltc = kr_ltc_ob['bids'][0][1] if len(kr_ltc_ob['asks']) > 0 else None

        # Información de Binance
        bid_bin_btc = bin_btc_ob['bids'][0][0] if len(bin_btc_ob['bids']) > 0 else None
        ask_bin_btc = bin_btc_ob['asks'][0][0] if len(bin_btc_ob['asks']) > 0 else None
        spread_bin_btc = (ask_bin_btc - bid_bin_btc) if (ask_bin_btc and bid_bin_btc) else None
        vol_ask_bin_btc = bin_btc_ob['asks'][0][1] if len(bin_btc_ob['bids']) > 0 else None
        vol_bid_bin_btc = bin_btc_ob['bids'][0][1] if len(bin_btc_ob['asks']) > 0 else None

        bid_bin_eth = bin_eth_ob['bids'][0][0] if len(bin_eth_ob['bids']) > 0 else None
        ask_bin_eth = bin_eth_ob['asks'][0][0] if len(bin_eth_ob['asks']) > 0 else None
        spread_bin_eth = (ask_bin_eth - bid_bin_eth) if (ask_bin_eth and bid_bin_eth) else None
        vol_ask_bin_eth = bin_eth_ob['asks'][0][1] if len(bin_eth_ob['bids']) > 0 else None
        vol_bid_bin_eth = bin_eth_ob['bids'][0][1] if len(bin_eth_ob['asks']) > 0 else None

        bid_bin_ltc = bin_ltc_ob['bids'][0][0] if len(bin_ltc_ob['bids']) > 0 else None
        ask_bin_ltc = bin_ltc_ob['asks'][0][0] if len(bin_ltc_ob['asks']) > 0 else None
        spread_bin_ltc = (ask_bin_ltc - bid_bin_ltc) if (ask_bin_ltc and bid_bin_ltc) else None
        vol_ask_bin_ltc = bin_ltc_ob['asks'][0][1] if len(bin_ltc_ob['bids']) > 0 else None
        vol_bid_bin_ltc = bin_ltc_ob['bids'][0][1] if len(bin_ltc_ob['asks']) > 0 else None

        # Timeframe utilizado para el ohlcv
        timeframe.append(bi_btc_ob['datetime'])

        # Arrays de la información de Bitso
        bid_bitso_btc.append(bid_bit_btc)
        ask_bitso_btc.append(ask_bit_btc)
        spread_bitso_btc.append(spread_bit_btc)
        vol_ask_bitso_btc.append(vol_ask_bit_btc)
        vol_bid_bitso_btc.append(vol_bid_bit_btc)

        bid_bitso_eth.append(bid_bit_eth)
        ask_bitso_eth.append(ask_bit_eth)
        spread_bitso_eth.append(spread_bit_eth)
        vol_ask_bitso_eth.append(vol_ask_bit_eth)
        vol_bid_bitso_eth.append(vol_bid_bit_eth)

        bid_bitso_ltc.append(bid_bit_ltc)
        ask_bitso_ltc.append(ask_bit_ltc)
        spread_bitso_ltc.append(spread_bit_ltc)
        vol_ask_bitso_ltc.append(vol_ask_bit_ltc)
        vol_bid_bitso_ltc.append(vol_bid_bit_ltc)

        # Arrays de la información de Kraken
        bid_kraken_btc.append(bid_kra_btc)
        ask_kraken_btc.append(ask_kra_btc)
        spread_kraken_btc.append(spread_kra_btc)
        vol_ask_kraken_btc.append(vol_ask_kra_btc)
        vol_bid_kraken_btc.append(vol_bid_kra_btc)

        bid_kraken_eth.append(bid_kra_eth)
        ask_kraken_eth.append(ask_kra_eth)
        spread_kraken_eth.append(spread_kra_eth)
        vol_ask_kraken_eth.append(vol_ask_kra_eth)
        vol_bid_kraken_eth.append(vol_bid_kra_eth)

        bid_kraken_ltc.append(bid_kra_ltc)
        ask_kraken_ltc.append(ask_kra_ltc)
        spread_kraken_ltc.append(spread_kra_ltc)
        vol_ask_kraken_ltc.append(vol_ask_kra_ltc)
        vol_bid_kraken_ltc.append(vol_bid_kra_ltc)

        # Arrays de la información de Binance
        bid_binance_btc.append(bid_bin_btc)
        ask_binance_btc.append(ask_bin_btc)
        spread_binance_btc.append(spread_bin_btc)
        vol_ask_binance_btc.append(vol_ask_bin_btc)
        vol_bid_binance_btc.append(vol_bid_bin_btc)

        bid_binance_eth.append(bid_bin_eth)
        ask_binance_eth.append(ask_bin_eth)
        spread_binance_eth.append(spread_bin_eth)
        vol_ask_binance_eth.append(vol_ask_bin_eth)
        vol_bid_binance_eth.append(vol_bid_bin_eth)

        bid_binance_ltc.append(bid_bin_ltc)
        ask_binance_ltc.append(ask_bin_ltc)
        spread_binance_ltc.append(spread_bin_ltc)
        vol_ask_binance_ltc.append(vol_ask_bin_ltc)
        vol_bid_binance_ltc.append(vol_bid_bin_ltc)

        time.sleep(40)

    # Fetch OHLCV bitso
    from_datetime = timeframe[0]
    since = bitso.parse8601(from_datetime)

    ohlc_bi_btc = pd.DataFrame(bitso.fetch_ohlcv('BTC/USDT',timeframe='1m',since=since, limit=60))
    frames_bi_btc = [pd.DataFrame(timeframe),ohlc_bi_btc.loc[:,1:5]]
    ohlcv_bi_btc = pd.concat(frames_bi_btc, axis=1)
    ohlcv_bi_btc.rename(columns = {0:'Time', 1:'open', 2:'high', 3:'low', 4:'close', 5:'volume'}, inplace = True)

    close_bi_btc = np.array(ohlcv_bi_btc['close'])

    ohlc_bi_eth = pd.DataFrame(bitso.fetch_ohlcv('ETH/USD',timeframe='1m',since=since, limit=60))
    frames_bi_eth = [pd.DataFrame(timeframe),ohlc_bi_eth.loc[:,1:5]]
    ohlcv_bi_eth = pd.concat(frames_bi_eth, axis=1)
    ohlcv_bi_eth.rename(columns = {0:'Time', 1:'open', 2:'high', 3:'low', 4:'close', 5:'volume'}, inplace = True)

    close_bi_eth = np.array(ohlcv_bi_eth['close'])

    ohlc_bi_ltc = pd.DataFrame(bitso.fetch_ohlcv('LTC/MXN',timeframe='1m',since=since, limit=60))
    frames_bi_ltc = [pd.DataFrame(timeframe),ohlc_bi_ltc.loc[:,1:5]]
    ohlcv_bi_ltc = pd.concat(frames_bi_ltc, axis=1)
    ohlcv_bi_ltc.rename(columns = {0:'Time', 1:'open', 2:'high', 3:'low', 4:'close', 5:'volume'}, inplace = True)

    close_bi_ltc = np.array(ohlcv_bi_ltc['close'])

    # Fetch OHLCV kraken
    limit_2 = 60
    from_datetime = timeframe[0]
    since = bitso.parse8601(from_datetime)

    ohlc_kr_btc = pd.DataFrame(kraken.fetch_ohlcv('BTC/USDT',timeframe='1m',since=since, limit=limit_2))
    frames_kr_btc = [pd.DataFrame(timeframe),ohlc_kr_btc.loc[:,1:5]]
    ohlcv_kr_btc = pd.concat(frames_kr_btc, axis=1)
    ohlcv_kr_btc.rename(columns = {0:'Time', 1:'open', 2:'high', 3:'low', 4:'close', 5:'volume'}, inplace = True)

    close_kr_btc = np.array(ohlcv_kr_btc['close'])

    ohlc_kr_eth = pd.DataFrame(kraken.fetch_ohlcv('ETH/USD',timeframe='1m',since=since, limit=limit_2))
    frames_kr_eth = [pd.DataFrame(timeframe),ohlc_kr_eth.loc[:,1:5]]
    ohlcv_kr_eth = pd.concat(frames_kr_eth, axis=1)
    ohlcv_kr_eth.rename(columns = {0:'Time', 1:'open', 2:'high', 3:'low', 4:'close', 5:'volume'}, inplace = True)

    close_kr_eth = np.array(ohlcv_kr_eth['close'])

    ohlc_kr_ltc = pd.DataFrame(kraken.fetch_ohlcv('LTC/USD',timeframe='1m',since=since, limit=limit_2))
    frames_kr_ltc = [pd.DataFrame(timeframe),ohlc_kr_ltc.loc[:,1:5]]
    ohlcv_kr_ltc = pd.concat(frames_kr_ltc, axis=1)
    ohlcv_kr_ltc.rename(columns = {0:'Time', 1:'open', 2:'high', 3:'low', 4:'close', 5:'volume'}, inplace = True)

    close_kr_ltc = np.array(ohlcv_kr_ltc['close'])

    # Fetch OHLCV Binance
    from_datetime = timeframe[0]
    since = bitso.parse8601(from_datetime)

    ohlc_bin_btc = pd.DataFrame(binance.fetch_ohlcv('BTC/USDT',timeframe='1m',since=since, limit=60))
    frames_bin_btc = [pd.DataFrame(timeframe),ohlc_kr_btc.loc[:,1:5]]
    ohlcv_bin_btc = pd.concat(frames_kr_btc, axis=1)
    ohlcv_bin_btc.rename(columns = {0:'Time', 1:'open', 2:'high', 3:'low', 4:'close', 5:'volume'}, inplace = True)

    close_bin_btc = np.array(ohlcv_kr_btc['close'])

    ohlc_bin_eth = pd.DataFrame(binance.fetch_ohlcv('ETH/USDT',timeframe='1m',since=since, limit=60))
    frames_bin_eth = [pd.DataFrame(timeframe),ohlc_kr_eth.loc[:,1:5]]
    ohlcv_bin_eth = pd.concat(frames_kr_eth, axis=1)
    ohlcv_bin_eth.rename(columns = {0:'Time', 1:'open', 2:'high', 3:'low', 4:'close', 5:'volume'}, inplace = True)

    close_bin_eth = np.array(ohlcv_kr_eth['close'])

    ohlc_bin_ltc = pd.DataFrame(binance.fetch_ohlcv('LTC/USDT',timeframe='1m',since=since, limit=60))
    frames_bin_ltc = [pd.DataFrame(timeframe),ohlc_kr_ltc.loc[:,1:5]]
    ohlcv_bin_ltc = pd.concat(frames_bin_ltc, axis=1)
    ohlcv_bin_ltc.rename(columns = {0:'Time', 1:'open', 2:'high', 3:'low', 4:'close', 5:'volume'}, inplace = True)

    close_bin_ltc = np.array(ohlcv_bin_ltc['close'])

    Exchanges = {}
    Exchanges["Bitso"] = {}
    Exchanges["Kraken"] = {}
    Exchanges["Binance"] = {}

    k = 0
    while k < len(timeframe):
        # Exchange Bitso
        Exchanges["Bitso"][timeframe[k]] = {}
        Exchanges["Bitso"][timeframe[k]]["BTC"]={}
        Exchanges["Bitso"][timeframe[k]]["BTC"]["Ask"] = ask_bitso_btc[k]
        Exchanges["Bitso"][timeframe[k]]["BTC"]["Bid"] = bid_bitso_btc[k]
        Exchanges["Bitso"][timeframe[k]]["BTC"]["Ask Volume"] = vol_ask_bitso_btc[k]
        Exchanges["Bitso"][timeframe[k]]["BTC"]["Bid Volume"] = vol_bid_bitso_btc[k]
        Exchanges["Bitso"][timeframe[k]]["BTC"]["Spread"] = spread_bitso_btc[k]
        Exchanges["Bitso"][timeframe[k]]["BTC"]["Close Price"] = close_bi_btc[k]

        Exchanges["Bitso"][timeframe[k]]["ETH"]={}
        Exchanges["Bitso"][timeframe[k]]["ETH"]["Ask"] = ask_bitso_eth[k]
        Exchanges["Bitso"][timeframe[k]]["ETH"]["Bid"] = bid_bitso_eth[k]
        Exchanges["Bitso"][timeframe[k]]["ETH"]["Ask Volume"] = vol_ask_bitso_eth[k]
        Exchanges["Bitso"][timeframe[k]]["ETH"]["Bid Volume"] = vol_bid_bitso_eth[k]
        Exchanges["Bitso"][timeframe[k]]["ETH"]["Spread"] = spread_bitso_eth[k]
        Exchanges["Bitso"][timeframe[k]]["ETH"]["Close Price"] = close_bi_eth[k]

        Exchanges["Bitso"][timeframe[k]]["LTC"]={}
        Exchanges["Bitso"][timeframe[k]]["LTC"]["Ask"] = ask_bitso_ltc[k]
        Exchanges["Bitso"][timeframe[k]]["LTC"]["Bid"] = bid_bitso_ltc[k]
        Exchanges["Bitso"][timeframe[k]]["LTC"]["Ask Volume"] = vol_ask_bitso_ltc[k]
        Exchanges["Bitso"][timeframe[k]]["LTC"]["Bid Volume"] = vol_bid_bitso_ltc[k]
        Exchanges["Bitso"][timeframe[k]]["LTC"]["Spread"] = spread_bitso_ltc[k]
        Exchanges["Bitso"][timeframe[k]]["LTC"]["Close Price"] = close_bi_ltc[k]

        # Exchange Kraken
        Exchanges["Kraken"][timeframe[k]] = {}
        Exchanges["Kraken"][timeframe[k]]["BTC"]={}
        Exchanges["Kraken"][timeframe[k]]["BTC"]["Ask"] = ask_kraken_btc[k]
        Exchanges["Kraken"][timeframe[k]]["BTC"]["Bid"] = bid_kraken_btc[k]
        Exchanges["Kraken"][timeframe[k]]["BTC"]["Ask Volume"] = vol_ask_kraken_btc[k]
        Exchanges["Kraken"][timeframe[k]]["BTC"]["Bid Volume"] = vol_bid_kraken_btc[k]
        Exchanges["Kraken"][timeframe[k]]["BTC"]["Spread"] = spread_kraken_btc[k]
        Exchanges["Kraken"][timeframe[k]]["BTC"]["Close Price"] = close_kr_btc[k]

        Exchanges["Kraken"][timeframe[k]]["ETH"]={}
        Exchanges["Kraken"][timeframe[k]]["ETH"]["Ask"] = ask_kraken_eth[k]
        Exchanges["Kraken"][timeframe[k]]["ETH"]["Bid"] = bid_kraken_eth[k]
        Exchanges["Kraken"][timeframe[k]]["ETH"]["Ask Volume"] = vol_ask_kraken_eth[k]
        Exchanges["Kraken"][timeframe[k]]["ETH"]["Bid Volume"] = vol_bid_kraken_eth[k]
        Exchanges["Kraken"][timeframe[k]]["ETH"]["Spread"] = spread_kraken_eth[k]
        Exchanges["Kraken"][timeframe[k]]["ETH"]["Close Price"] = close_kr_eth[k]

        Exchanges["Kraken"][timeframe[k]]["LTC"]={}
        Exchanges["Kraken"][timeframe[k]]["LTC"]["Ask"] = ask_kraken_ltc[k]
        Exchanges["Kraken"][timeframe[k]]["LTC"]["Bid"] = bid_kraken_ltc[k]
        Exchanges["Kraken"][timeframe[k]]["LTC"]["Ask Volume"] = vol_ask_kraken_ltc[k]
        Exchanges["Kraken"][timeframe[k]]["LTC"]["Bid Volume"] = vol_bid_kraken_ltc[k]
        Exchanges["Kraken"][timeframe[k]]["LTC"]["Spread"] = spread_kraken_ltc[k]
        Exchanges["Kraken"][timeframe[k]]["LTC"]["Close Price"] = close_kr_ltc[k]


        # Exchange Binance
        Exchanges["Binance"][timeframe[k]] = {}
        Exchanges["Binance"][timeframe[k]]["BTC"]={}
        Exchanges["Binance"][timeframe[k]]["BTC"]["Ask"] = ask_binance_btc[k]
        Exchanges["Binance"][timeframe[k]]["BTC"]["Bid"] = bid_binance_btc[k]
        Exchanges["Binance"][timeframe[k]]["BTC"]["Ask Volume"] = vol_ask_binance_btc[k]
        Exchanges["Binance"][timeframe[k]]["BTC"]["Bid Volume"] = vol_bid_binance_btc[k]
        Exchanges["Binance"][timeframe[k]]["BTC"]["Spread"] = spread_binance_btc[k]
        Exchanges["Binance"][timeframe[k]]["BTC"]["Close Price"] = close_bin_btc[k]

        Exchanges["Binance"][timeframe[k]]["ETH"]={}
        Exchanges["Binance"][timeframe[k]]["ETH"]["Ask"] = ask_binance_eth[k]
        Exchanges["Binance"][timeframe[k]]["ETH"]["Bid"] = bid_binance_eth[k]
        Exchanges["Binance"][timeframe[k]]["ETH"]["Ask Volume"] = vol_ask_binance_eth[k]
        Exchanges["Binance"][timeframe[k]]["ETH"]["Bid Volume"] = vol_bid_binance_eth[k]
        Exchanges["Binance"][timeframe[k]]["ETH"]["Spread"] = spread_binance_eth[k]
        Exchanges["Binance"][timeframe[k]]["ETH"]["Close Price"] = close_bin_eth[k]

        Exchanges["Binance"][timeframe[k]]["LTC"]={}
        Exchanges["Binance"][timeframe[k]]["LTC"]["Ask"] = ask_binance_ltc[k]
        Exchanges["Binance"][timeframe[k]]["LTC"]["Bid"] = bid_binance_ltc[k]
        Exchanges["Binance"][timeframe[k]]["LTC"]["Ask Volume"] = vol_ask_binance_ltc[k]
        Exchanges["Binance"][timeframe[k]]["LTC"]["Bid Volume"] = vol_bid_binance_ltc[k]
        Exchanges["Binance"][timeframe[k]]["LTC"]["Spread"] = spread_binance_ltc[k]
        Exchanges["Binance"][timeframe[k]]["LTC"]["Close Price"] = close_bin_ltc[k]

        k += 1

    dataframe = pd.DataFrame(columns={'exchange','timeStamp','level','ask_volume','bid_volume','total_volume','mid_price','vwap'})
    dataframe['bid_volume'] =  vol_bid_bitso_btc + vol_bid_bitso_eth + vol_bid_bitso_ltc + vol_bid_kraken_btc + vol_bid_kraken_eth + vol_bid_kraken_ltc + vol_bid_binance_btc + vol_bid_binance_eth + vol_bid_binance_ltc
    dataframe['ask_volume'] =  vol_ask_bitso_btc + vol_ask_bitso_eth + vol_ask_bitso_ltc + vol_ask_kraken_btc + vol_ask_kraken_eth + vol_ask_kraken_ltc + vol_ask_binance_btc + vol_ask_binance_eth + vol_ask_binance_ltc
    bitso_frame = ["bitso" for i in range(len(vol_bid_bitso_btc + vol_bid_bitso_eth + vol_bid_bitso_ltc))]
    kraken_frame = ["kraken" for i in range(len(vol_bid_bitso_btc + vol_bid_bitso_eth + vol_bid_bitso_ltc))]
    binance_frame = ["binance" for i in range(len(vol_bid_bitso_btc + vol_bid_bitso_eth + vol_bid_bitso_ltc))]
    dataframe['exchange'] = bitso_frame + kraken_frame + binance_frame
    dataframe['timeStamp'] = timeframe + timeframe + timeframe + timeframe + timeframe + timeframe + timeframe + timeframe + timeframe
    dataframe['total_volume'] = dataframe["ask_volume"] + dataframe["bid_volume"]
    dataframe['mid_price'] = print(len(list((ohlcv_bi_btc["open"][0:minutes] + ohlcv_bi_btc["close"][0:minutes]) / 2) + list((ohlcv_bi_eth["open"][0:minutes] + ohlcv_bi_eth["close"][0:minutes]) / 2) + list((ohlcv_bi_ltc["open"][0:minutes] + ohlcv_bi_ltc["close"][0:minutes]) / 2) + list((ohlcv_kr_btc["open"][0:minutes] + ohlcv_kr_btc["close"][0:minutes]) / 2) + list((ohlcv_kr_eth["open"][0:minutes] + ohlcv_kr_eth["close"][0:minutes]) / 2) + list((ohlcv_kr_ltc["open"][0:minutes] + ohlcv_kr_ltc["close"][0:15]) / 2) + list((ohlcv_bin_btc["open"][0:minutes] + ohlcv_bin_btc["close"][0:minutes]) / 2) + list((ohlcv_bin_eth["open"][0:minutes] + ohlcv_bin_eth["close"][0:minutes]) / 2) + list((ohlcv_bin_ltc["open"][0:minutes] + ohlcv_bin_ltc["close"][0:minutes]) / 2)))

    all_close = list(ohlcv_bi_btc["close"][0:minutes]) + list(ohlcv_bi_eth["close"][0:minutes]) + list(ohlcv_bi_ltc["close"][0:minutes]) + list(ohlcv_kr_btc["close"][0:minutes]) + list(ohlcv_kr_eth["close"][0:minutes]) + list(ohlcv_kr_ltc["close"][0:minutes]) + list(ohlcv_bin_btc["close"][0:minutes]) + list(ohlcv_bin_eth["close"][0:minutes][0:minutes]) + list(ohlcv_bin_ltc["close"][0:minutes])
    dataframe['level'] = all_close/dataframe['total_volume']
    vwap_sum = list(((ohlcv_bi_btc["high"] + ohlcv_bi_btc["low"] + ohlcv_bi_btc["close"])/3)*ohlcv_bi_btc["volume"]) + list(((ohlcv_bi_eth["high"] + ohlcv_bi_eth["low"] + ohlcv_bi_eth["close"])/3)*ohlcv_bi_eth["volume"]) + list(((ohlcv_bi_ltc["high"] + ohlcv_bi_ltc["low"] + ohlcv_bi_ltc["close"])/3)*ohlcv_bi_ltc["volume"]) + list(((ohlcv_kr_btc["high"] + ohlcv_kr_btc["low"] + ohlcv_kr_btc["close"])/3)*ohlcv_kr_btc["volume"]) + list(((ohlcv_kr_eth["high"] + ohlcv_kr_eth["low"] + ohlcv_kr_eth["close"])/3)*ohlcv_kr_eth["volume"]) + list(((ohlcv_kr_ltc["high"] + ohlcv_kr_ltc["low"] + ohlcv_kr_ltc["close"])/3)*ohlcv_kr_ltc["volume"]) + list(((ohlcv_bin_btc["high"] + ohlcv_bin_btc["low"] + ohlcv_bin_btc["close"])/3)*ohlcv_bin_btc["volume"]) + list(((ohlcv_bin_eth["high"] + ohlcv_bin_eth["low"] + ohlcv_bin_eth["close"])/3)*ohlcv_bin_eth["volume"]) + list(((ohlcv_bin_ltc["high"] + ohlcv_bin_ltc["low"] + ohlcv_bin_ltc["close"])/3)*ohlcv_bin_ltc["volume"])
    dataframe['vwap'] = vwap_sum/dataframe['total_volume']



    j = 0
    rolls_bi_btc = []
    rolls_bi_eth = []
    rolls_bi_ltc = []

    rolls_kr_btc = []
    rolls_kr_eth = []
    rolls_kr_ltc = []

    rolls_bin_btc = []
    rolls_bin_eth = []
    rolls_bin_ltc = []

    while j < len(close_bi_btc) - 9:

        # Rolls bitso
        a = np.cov(np.array([close_bi_btc[j:j+5],close_bi_btc[j+5:j+10]]))[0,1]
        if a > 0:
            a = 2*math.sqrt(a)
            rolls_bi_btc.append(a)

        else:
            rolls_bi_btc.append(0)

        a = np.cov(np.array([close_bi_eth[j:j+5],close_bi_eth[j+5:j+10]]))[0,1]
        if a > 0:
            a = 2*math.sqrt(a)
            rolls_bi_eth.append(a)

        else:
            rolls_bi_eth.append(0)

        a = np.cov(np.array([close_bi_ltc[j:j+5],close_bi_ltc[j+5:j+10]]))[0,1]
        if a > 0:
            a = 2*math.sqrt(a)
            rolls_bi_ltc.append(a)

        else:
            rolls_bi_ltc.append(0)

        # Rolls kraken
        a = np.cov(np.array([close_kr_btc[j:j+5],close_kr_btc[j+5:j+10]]))[0,1]
        if a > 0:
            a = 2*math.sqrt(a)
            rolls_kr_btc.append(a)

        else:
            rolls_kr_btc.append(0)

        a = np.cov(np.array([close_kr_eth[j:j+5],close_kr_eth[j+5:j+10]]))[0,1]
        if a > 0:
            a = 2*math.sqrt(a)
            rolls_kr_eth.append(a)

        else:
            rolls_kr_eth.append(0)

        a = np.cov(np.array([close_kr_ltc[j:j+5],close_kr_ltc[j+5:j+10]]))[0,1]
        if a > 0:
            a = 2*math.sqrt(a)
            rolls_kr_ltc.append(a)

        else:
            rolls_kr_ltc.append(0)

        # Rolls Binance
        a = np.cov(np.array([close_bin_btc[j:j+5],close_bin_btc[j+5:j+10]]))[0,1]
        if a > 0:
            a = 2*math.sqrt(a)
            rolls_bin_btc.append(a)

        else:
            rolls_bin_btc.append(0)

        a = np.cov(np.array([close_bin_eth[j:j+5],close_bin_eth[j+5:j+10]]))[0,1]
        if a > 0:
            a = 2*math.sqrt(a)
            rolls_bin_eth.append(a)

        else:
            rolls_bin_eth.append(0)

        a = np.cov(np.array([close_bin_ltc[j:j+5],close_bin_ltc[j+5:j+10]]))[0,1]
        if a > 0:
            a = 2*math.sqrt(a)
            rolls_bin_ltc.append(a)

        else:
            rolls_bin_ltc.append(0)

        j += 1


    rolls_total = pd.DataFrame()
    rolls_juntos = rolls_bi_btc + rolls_bi_eth + rolls_bi_ltc + rolls_kr_btc + rolls_kr_eth + rolls_kr_ltc + rolls_bin_btc + rolls_bin_eth + rolls_bin_ltc
    rolls_total["timestamp"] = timeframe[9:60] + timeframe[9:60] + timeframe[9:60] + timeframe[9:60] + timeframe[9:60] + timeframe[9:60] + timeframe[9:60] + timeframe[9:60] + timeframe[9:60]
    rolls_total["close"] = list(close_bi_btc)[9:60] + list(close_bi_eth)[9:60] + list(close_bi_ltc)[9:60] + list(close_kr_btc)[9:60] + list(close_kr_eth)[9:60] + list(close_kr_ltc)[9:60] + list(close_bin_btc)[9:60] + list(close_bin_eth)[9:60] + list(close_bin_ltc)[9:60]
    rolls_total["spread"] = list((spread_bitso_btc)[9:60]) + list(spread_bitso_eth[9:60]) + list(spread_bitso_ltc[9:60]) + list(spread_kraken_btc[9:60]) + list(spread_kraken_eth[9:60]) + list(spread_kraken_ltc[9:60]) + list(spread_binance_btc[9:60]) + list(spread_binance_eth[9:60]) + list(spread_binance_ltc[9:60])
    rolls_total["effective spread"] = rolls_juntos
    

    data = pd.DataFrame()
    data['timeframe'] = timeframe
    data['bitso_bid_bit'] =  bid_bitso_btc[0:60]
    data['bitso_ask_bit'] =  ask_bitso_btc[0:60]
    data['bitso_spread_bit'] =  spread_bitso_btc[0:60]
    data['bitso_bid_eth'] =  bid_bitso_eth[0:60]
    data['bitso_ask_eth'] =  ask_bitso_eth[0:60]
    data['bitso_spread_eth'] =  spread_bitso_eth[0:60]
    data['bitso_bid_ltc'] =  bid_bitso_ltc[0:60]
    data['bitso_ask_ltc'] =  ask_bitso_ltc[0:60]
    data['bitso_spread_ltc'] =  spread_bitso_ltc[0:60]

    data['kraken_bid_bit'] =  bid_kraken_btc[0:60]
    data['kraken_ask_bit'] =  ask_kraken_btc[0:60]
    data['kraken_spread_bit'] =  spread_kraken_btc[0:60]
    data['kraken_bid_eth'] =  bid_kraken_eth[0:60]
    data['kraken_ask_eth'] =  ask_kraken_eth[0:60]
    data['kraken_spread_eth'] =  spread_kraken_eth[0:60]
    data['kraken_bid_ltc'] =  bid_kraken_ltc[0:60]
    data['kraken_ask_ltc'] =  ask_kraken_ltc[0:60]
    data['kraken_spread_ltc'] =  spread_kraken_ltc[0:60]

    data['binance_bid_bit'] =  bid_binance_btc[0:60]
    data['binance_ask_bit'] =  ask_binance_btc[0:60]
    data['binance_spread_bit'] =  spread_binance_btc[0:60]
    data['binance_bid_eth'] =  bid_binance_eth[0:60]
    data['binance_ask_eth'] =  ask_binance_eth[0:60]
    data['binance_spread_eth'] =  spread_binance_eth[0:60]
    data['binance_bid_ltc'] =  bid_binance_ltc[0:60]
    data['binance_ask_ltc'] =  ask_binance_ltc[0:60]
    data['binance_spread_ltc'] =  spread_binance_ltc[0:60]

    return Exchanges,dataframe, rolls_total, data
