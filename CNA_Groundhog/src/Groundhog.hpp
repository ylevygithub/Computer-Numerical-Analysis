//
// EPITECH PROJECT, 2020
// Groundhog.hpp
// File description:
// Groundhog.hpp
//

#ifndef GROUNDHOG_HPP_
#define GROUNDHOG_HPP_

#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
#include <iomanip>
#include "Exception.hpp"
using namespace std;

class Groundhog
{
    public:
        string arg;
    private :
        vector<double> recordInputs;
        int period;
        string nan = "g=nan\tr=nan%\ts=nan";
        string lastNan = "g=nan\tr=nan%\ts=";
        double sum = 0;
        double AncienAverage;
        double average = 0;
        double sumOfSquares = 0;
        double variance;
        double nDaysTemp;
        double standardDeviation;
        int mySwitch = 0;
        double g;
        double r;
        double ancienR = 0;
        int verifNeg = 0;
        vector<double> argsSwitch;
    public :
        ~Groundhog() {}
        Groundhog() {}
        void Ground(string arg);
        double Sum(void);
        double Average(void);
        double SumOfSquares(void);
        double Variance(void);
        double StandardDeviation(void);
        void AllSet(void);
        void relativeEvolTemp(void);
        void tempIncreaseAvg(void);
        void EndPeriodDisplay(void);
        void AfterPeriodDisplay(void);
        void stop();
};

/************main.cpp************/
void PrintUsage(int ac, char **av);
/************Stop.cpp************/
void stopDuringPeriod(string arg);
/************Verif.cpp***********/
int CheckArg(char *arg);
int CheckInput(string arg);
void ArgIsNotNum(string arg);


#endif
