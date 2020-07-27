#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## trade
## File description:
## main
##

import sys
from settings import setCandleFormat, getSettings, Format, Settings
from candles_management import List
from commands import getCandle, updateStacks, printAction

class Trade():
    BTC = 0.0
    ETH = 0.0
    USDT = 0.0
    lastPeriod = 20

    def __init__(self, *args, **kwargs):
        self.settings = Settings()
        self.btc_eth_candles = List("BTC_ETH")
        self.usdt_eth_candles = List("USDT_ETH")
        self.usdt_btc_candles = List("USDT_BTC")

def getCommands(GAME, av):
    if (len(av) < 3):
        return
    if av[0] == "update" and av[1] == "game" and av[2] == "next_candles":
        return (getCandle(GAME, av))
    if av[0] == "update" and av[1] == "game" and av[2] == "stacks":
        return (updateStacks(GAME, av))
    if av[0] == "action" and av[1] == "order":
        if (av[2] != "2000"):
            return (print("no_moves"))
        else:
            return (printAction(GAME, av))

def Bot():
    GAME = Trade()
    while True:
        try:
            line = input()
        except (KeyboardInterrupt, EOFError):
            break
        av = line.split()
        if (GAME.settings.full is False):
            getSettings(GAME, av)
        else:
            getCommands(GAME, av)

def main():
    Bot()

if __name__ == "__main__":
    main()
