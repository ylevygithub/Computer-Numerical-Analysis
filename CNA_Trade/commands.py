#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## trade
## File description:
## commands functions
##

from action import makeBitcoinAction, makeEtherumAction

def getCandle(GAME, av):
    if len(av) < 4:
        return (print("invalid candle"));
    candles = av[3].split(';')
    for candle in candles:
        arr = candle.split(',')
        if arr[GAME.settings.candle_format.pair_it] == "BTC_ETH":
            GAME.btc_eth_candles.addCandle(GAME, arr)
        elif arr[GAME.settings.candle_format.pair_it] == "USDT_ETH":
            GAME.usdt_eth_candles.addCandle(GAME, arr)
        elif arr[GAME.settings.candle_format.pair_it] == "USDT_BTC":
            GAME.usdt_btc_candles.addCandle(GAME, arr)

def updateStacks(GAME, av):
    if len(av) < 4:
        return (print("update game stacks's len is not correct."))
    stacks = av[3].split(',')
    for stack in stacks:
        arr = stack.split(':')
        if arr[0] == "BTC":
            try:
                GAME.BTC = float(arr[1])
            except ValueError:
                pass
        if arr[0] == "ETH":
            try:
                GAME.ETH = float(arr[1])
            except ValueError:
                pass
        if arr[0] == "USDT":
            try:
                GAME.USDT = float(arr[1])
            except ValueError:
                pass

def printAction(GAME, av):
    BTC = makeBitcoinAction(GAME)
    if (BTC != 0):
        return (print(BTC))
    else:
        ETH = makeEtherumAction(GAME)
        if (ETH != 0):
            return (print(ETH))
        else:
            return (print("pass"))
