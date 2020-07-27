#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## trade
## File description:
## candles_management
##

class Stat():
    upChange = 0
    downChange = 0
    upEMA = 0
    downEMA = 0
    relativeStrengthIndex = 0

class CandleValue():
    dateValue = 0
    highValue = 0
    lowValue = 0
    openValue = 0
    closeValue = 0
    volumeValue = 0

class List():
    def __init__(self, pair):
        self.pair = pair
        self.candles = []
        self.stat = []

    def addCandle(self, GAME, arr):
        candle = CandleValue()
        stat = Stat()
        for it, value in enumerate(arr):
            if GAME.settings.candle_format.date_it == it:
                try:
                    candle.dateValue = float(value)
                except ValueError:
                    return
            if GAME.settings.candle_format.high_it == it:
                try:
                    candle.highValue = float(value)
                except ValueError:
                    return
            if GAME.settings.candle_format.low_it == it:
                try:
                    candle.lowValue = float(value)
                except ValueError:
                    return
            if GAME.settings.candle_format.open_it == it:
                try:
                    candle.openValue = float(value)
                except ValueError:
                    return
            if GAME.settings.candle_format.close_it == it:
                try:
                    candle.closeValue = float(value)
                except ValueError:
                    return
            if GAME.settings.candle_format.volume_it == it:
                try:
                    candle.volumeValue = float(value)
                except ValueError:
                    return
        self.candles.append(candle)
        self.fillStat(GAME, stat)

    def fillStat(self, GAME, stat):
        if self.getCandleCount() > 1:
            self.formuleUpDownChange(GAME, stat)
        if self.getCandleCount() > GAME.lastPeriod:
            self.formuleRSI(GAME, stat)
        self.stat.append(stat)

    def getCandleCount(self):
        return len(self.candles)

    def getLastCandle(self):
        if len(self.candles) < 1:
            return None
        else:
            return self.candles[-1]

    def getLastStat(self):
        if len(self.stat) < 1:
            return None
        return self.stat[-1]

#**************************Formule UpDownChanges*****************************
    def formuleUpDownChange(self, GAME, stat):
        it = self.getCandleCount() - 2
        last = self.getLastCandle()
        prev = self.candles[it]
        if last.closeValue > prev.closeValue:
            stat.upChange = last.closeValue - prev.closeValue
            stat.downChange = 0
        elif last.closeValue < prev.closeValue:
            stat.downChange = prev.closeValue - last.closeValue
            stat.upChange = 0
        else:
            stat.upChange = 0
            stat.downChange = 0

#**************************Formule UpDownChanges*****************************
#**************************Formule RSI*****************************
    def formuleEMAup(self, GAME, stat):#formule EMA a la hausse
        prev_stat = self.getLastStat()#la derniere stat des stats enregistrés
        last_stat = stat #reprend la stat en parametre donc celle en cours
        Alpha = 2 / (1 + GAME.lastPeriod)#ALPHA = 2/(1+20)
        EMA = float(last_stat.upChange * Alpha + prev_stat.upEMA * (1 - Alpha))
        #EMA = (dernier changement a la hausse * ALPHA + avant dernier EMA a la hausse * (1 - ALPHA))
        return (EMA)

    def formuleEMAdown(self, GAME, stat):#formule EMA a la baisse
        prev_stat = self.getLastStat()#la derniere stat des stats enregistrés
        last_stat = stat#reprend la stat en parametre donc celle en cours
        Alpha = 2 / (1 + GAME.lastPeriod)#ALPHA = 2/(1+20)
        EMA = float(last_stat.downChange * Alpha + prev_stat.downEMA * (1 - Alpha))
        #EMA = (dernier changement a la baisse * ALPHA + avant dernier EMA a la baisse * (1 - ALPHA))
        return (EMA)

    def formuleRSI(self, GAME, stat):#RSI = Indicateur qui permet de determiner 2choses. 1)Voir la puissance d'une tendance
        #2)Indiquer si le marché est en surachat ou en survente.
        #Formule = 100 - (100 / (1 + moyenne a la hausse/moyenne a la baisse))
        #Un RSI indique un chiffre compris entre 0 et 100. Un RSI a 50 indique que le marché trouve un point d'équilibre
        #sur L'unité de temps(la mienne est mise a 20). Lorsque le RSI est > 70, le marché est dit suracheté et est candidat
        #a une correction baissière. Lorsque le RSI est < 30, le marché est dit survendu et est candidat a une correction
        #a la hausse.
        stat.upEMA = self.formuleEMAup(GAME, stat)#EMA a la hausse
        stat.downEMA = self.formuleEMAdown(GAME, stat)#EMA a la baisse
        stat.relativeStrengthIndex = 100 - (100 / (1 + stat.upEMA / stat.downEMA))
        # stat.relativeStrengthIndex = stat.upEMA / (stat.upEMA + abs(stat.downEMA)) * 100 #a revoir
#**************************Formule RSI*****************************
#**************************Action orders *****************************
    def makeAction(self, GAME):
        RSI = self.getLastStat().relativeStrengthIndex
        if (self.getCandleCount() < GAME.lastPeriod):#si le nbre de candles < 20, on ne peut ni buy ni sell car le calcul du RSI est impossible
            return "PASS"
        elif (RSI <= 30):#Si le rsi est <= 30, ca veut dire que les prix chutes et qu'il faut donc acheter
            return "BUY"
        elif (RSI >= 70):
            return "SELL"
        else:
            return "PASS"
#**************************Action orders *****************************
