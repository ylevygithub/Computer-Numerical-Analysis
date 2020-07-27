//
// EPITECH PROJECT, 2020
// Groundhog
// File description:
// Groundhog function
//

#include "Groundhog.hpp"

void Groundhog::Ground(string arg)
{
    int i = 0;
    period = stoi(arg);

    if (period == 0)
        throw MyException("ERROR : period cannot be equal 0");
    if (!cin)
        throw MyException("ERROR : time out avoided");
    while (cin) {
        for (; i < (period - 1); i++) {
            cin >> arg;
            if (!cin)
                throw MyException("ERROR : time out avoided");
            stopDuringPeriod(arg);
            ArgIsNotNum(arg);
            recordInputs.push_back(stod(arg));
            cout << nan << endl;
        }
        i++;
        if (!cin)
            throw MyException("ERROR : time out avoided");
        if (i++ == period && cin)
            EndPeriodDisplay();
        AfterPeriodDisplay();
    }
    if (!cin)
        throw MyException("ERROR : time out avoided");
}
