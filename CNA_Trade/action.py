#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## trade
## File description:
## action order
##

def makeBitcoinAction(GAME):
    closePrice = GAME.usdt_btc_candles.getLastCandle().closeValue
    action = GAME.usdt_btc_candles.makeAction(GAME)
    if action == "BUY" and GAME.USDT != 0:
        price = float(GAME.USDT / closePrice)
        GAME.USDT = 0.0
        GAME.BTC = price - (price * 0.2 / 100)
        finalPrice = str(price)
        return ("buy USDT_BTC " + finalPrice)
    elif action == "SELL" and GAME.BTC != 0:
        price = float(GAME.BTC / closePrice)
        GAME.BTC = 0.0
        GAME.USDT = price - (price * 0.2 / 100)
        finalPrice = str(price)
        return ("sell USDT_BTC " + finalPrice)
    else:
        return (0)

def makeEtherumAction(GAME):
    closePrice = GAME.usdt_eth_candles.getLastCandle().closeValue
    action = GAME.usdt_eth_candles.makeAction(GAME)
    if action == "BUY" and GAME.USDT != 0:
        price = float(GAME.USDT / closePrice)
        GAME.USDT = 0.0
        GAME.ETH = price - (price * 0.2 / 100)
        finalPrice = str(price)
        return ("buy USDT_ETH " + finalPrice)
    elif action == "SELL" and GAME.ETH != 0:
        price = float(GAME.ETH / closePrice)
        GAME.ETH = 0.0
        GAME.USDT = price - (price * 0.2 / 100)
        finalPrice = str(price)
        return ("sell USDT_ETH " + finalPrice)
    else:
        return (0)
