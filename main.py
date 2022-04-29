"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab 4.                                                                                     -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: danielperhez                                                                               -- #                                                                            -- #
# -- repository: https://github.com/danielperhez/Modulo4_MyST                                       -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import functions
import visualizations

def crypto_exchanges(minutes):
    avance_1,avance_2,rolls,data = functions.cxt(minutes)
    return avance_1,avance_2,rolls,data

def plot_bid_bit_1(data):
    a = visualizations.plot_bid_bit(data)
    return a

def plot_ask_bit_1(data):
    a = visualizations.plot_ask_bit(data)
    return a

def plot_spread_bit_1(data):
    a = visualizations.plot_spread_bit(data)
    return a



def plot_bid_eth_1(data):
    a = visualizations.plot_bid_eth(data)
    return a

def plot_ask_eth_1(data):
    a = visualizations.plot_ask_eth(data)
    return a

def plot_spread_eth_1(data):
    a = visualizations.plot_spread_eth(data)
    return a



def plot_bid_ltc_1(data):
    a = visualizations.plot_bid_ltc(data)
    return a

def plot_ask_ltc_1(data):
    a = visualizations.plot_ask_ltc(data)
    return a

def plot_spread_ltc_1(data):
    a = visualizations.plot_spread_ltc(data)
    return a
