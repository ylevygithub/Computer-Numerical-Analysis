//
// EPITECH PROJECT, 2020
// Groundhog
// File description:
// Display functions
//

#include "Groundhog.hpp"

void Groundhog::EndPeriodDisplay(void)
{
    cin >> arg;
    stop();
    ArgIsNotNum(arg);
    recordInputs.push_back(stod(arg));
    cout << lastNan;
    AllSet();
    cout << fixed << setprecision(2) <<  standardDeviation << endl;
}

void Groundhog::AfterPeriodDisplay(void)
{
    cin >> arg;
    stop();
    ArgIsNotNum(arg);
    AncienAverage = average;
    ancienR = r;
    nDaysTemp = recordInputs[0];
    recordInputs.erase(recordInputs.begin());
    recordInputs.push_back(stod(arg));
    AllSet();
    tempIncreaseAvg();
    relativeEvolTemp();
    cout << fixed << setprecision(2) <<  standardDeviation;
    if (verifNeg != 0) {
        cout << "\ta switch occurs";
        verifNeg = 0;
        mySwitch++;
        argsSwitch.push_back(stod(arg));
    }
    cout << endl;
}
