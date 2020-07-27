#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## trade
## File description:
## settings
##

class Settings():
    player_names = []
    your_bot = None
    timebank = 0
    time_per_move = 0
    candle_interval = 0
    candles_total = 0
    candles_given = 0
    initial_stack = 0
    transaction_fee_percent = 0.2
    candle_txt = ""
    counter = 0
    full = False
    def __init__(self, *args, **kwargs):
        self.candle_format = Format()

class Format():
    pair_it = 0
    date_it = 0
    high_it = 0
    low_it = 0
    open_it = 0
    close_it = 0
    volume_it = 0
    count = 0

def getSettings(GAME, av):
    if (av[0] != "settings") or (len(av) != 3):
        return (print("invalid settings"))
    if (av[1] == "player_names"):
        try:
            if (len(GAME.settings.player_names) == 0):
                GAME.settings.counter += 1
            GAME.settings.player_names.append(str(av[2]))
        except ValueError:
            return (print("invalid settings"))
    if (av[1] == "your_bot"):
        try:
            GAME.settings.your_bot.append(str(av[2]))
            GAME.settings.counter += 1
        except ValueError:
            return (print("invalid settings"))
    if (av[1] == "timebank"):
        try:
            GAME.settings.timebank = int(av[2])
            GAME.settings.counter += 1
        except ValueError:
            return (print("invalid settings"))
    if (av[1] == "time_per_move"):
        try:
            GAME.settings.time_per_move = int(av[2])
            GAME.settings.counter += 1
        except ValueError:
            return (print("invalid settings"))
    if (av[1] == "candle_interval"):
        try:
            GAME.settings.candle_interval = int(av[2])
            GAME.settings.counter += 1
        except ValueError:
            return (print("invalid settings"))
    if (av[1] == "candles_total"):
        try:
            GAME.settings.candles_total = int(av[2])
            GAME.settings.counter += 1
        except ValueError:
            return (print("invalid settings"))
    if (av[1] == "candles_given"):
        try:
            GAME.settings.candles_given = int(av[2])
            GAME.settings.counter += 1
        except ValueError:
            return (print("invalid settings"))
    if (av[1] == "initial_stack"):
        try:
            GAME.settings.initial_stack = int(av[2])
            GAME.settings.counter += 1
        except ValueError:
            return (print("invalid settings"))
    if (av[1] == "candle_format"):
        try:
            GAME.settings.candle_txt = str(av[2])
            GAME.settings.counter += 1
            arr = GAME.settings.candle_txt.split(',')
            setCandleFormat(GAME, arr)
        except ValueError:
            return (print("invalid settings"))
    if (GAME.settings.counter == 9):
        GAME.settings.full == True
        GAME.USDT = GAME.settings.initial_stack

def setCandleFormat(GAME, arr):
    for it, key in enumerate(arr):
        if key == "pair":
            GAME.settings.candle_format.pair_it = it
        if key == "date":
            GAME.settings.candle_format.date_it = it
        if key == "high":
            GAME.settings.candle_format.high_it = it
        if key == "low":
            GAME.settings.candle_format.low_it = it
        if key == "open":
            GAME.settings.candle_format.open_it = it
        if key == "close":
            GAME.settings.candle_format.close_it = it
        if key == "volume":
            GAME.settings.candle_format.volume_it = it
        GAME.settings.candle_format.count += 1
