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

def plot_bid_bit(data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['bitso_bid_bit'],
        name = 'bitso_bid_bit', # Style name/legend entry with html tags
        connectgaps=True # override default to connect the gaps
    ))
    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['kraken_bid_bit'],
        name='kraken_bid_bit',
    ))

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['binance_bid_bit'],
        name='binance_bid_bit',
    ))

    return fig.show()


def plot_ask_bit(data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['bitso_ask_bit'],
        name = 'bitso_ask_bit', # Style name/legend entry with html tags
        connectgaps=True # override default to connect the gaps
    ))
    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['kraken_ask_bit'],
        name='kraken_ask_bit',
    ))

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['binance_ask_bit'],
        name='binance_ask_bit',
    ))

    return fig.show()


def plot_spread_bit(data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['bitso_ask_bit'],
        name = 'bitso_ask_bit',
    ))
    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['kraken_ask_bit'],
        name='kraken_ask_bit',
    ))

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['binance_ask_bit'],
        name='binance_ask_bit',
    ))

    return fig.show()




def plot_bid_eth(data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['bitso_bid_eth'],
        name = 'bitso_bid_eth', # Style name/legend entry with html tags
        connectgaps=True # override default to connect the gaps
    ))
    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['kraken_bid_eth'],
        name='kraken_bid_eth',
    ))

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['binance_bid_eth'],
        name='binance_bid_eth',
    ))

    return fig.show()


def plot_ask_eth(data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['bitso_ask_eth'],
        name = 'bitso_ask_eth', # Style name/legend entry with html tags
        connectgaps=True # override default to connect the gaps
    ))
    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['kraken_ask_eth'],
        name='kraken_ask_eth',
    ))

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['binance_ask_eth'],
        name='binance_ask_eth',
    ))

    return fig.show()


def plot_spread_eth(data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['bitso_ask_eth'],
        name = 'bitso_ask_eth',
    ))
    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['kraken_ask_eth'],
        name='kraken_ask_eth',
    ))

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['binance_ask_eth'],
        name='binance_ask_eth',
    ))

    return fig.show()


def plot_bid_ltc(data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['bitso_bid_ltc'],
        name = 'bitso_bid_ltc', # Style name/legend entry with html tags
        connectgaps=True # override default to connect the gaps
    ))
    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['kraken_bid_ltc'],
        name='kraken_bid_ltc',
    ))

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['binance_bid_ltc'],
        name='binance_bid_ltc',
    ))

    return fig.show()


def plot_ask_ltc(data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['bitso_ask_ltc'],
        name = 'bitso_ask_ltc', # Style name/legend entry with html tags
        connectgaps=True # override default to connect the gaps
    ))
    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['kraken_ask_ltc'],
        name='kraken_ask_ltc',
    ))

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['binance_ask_ltc'],
        name='binance_ask_ltc',
    ))

    return fig.show()


def plot_spread_ltc(data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['bitso_ask_ltc'],
        name = 'bitso_ask_ltc',
    ))
    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['kraken_ask_ltc'],
        name='kraken_ask_ltc',
    ))

    fig.add_trace(go.Scatter(
        x=data['timeframe'],
        y=data['binance_ask_ltc'],
        name='binance_ask_ltc',
    ))

    return fig.show()