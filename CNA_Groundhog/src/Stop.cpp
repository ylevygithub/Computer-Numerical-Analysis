//
// EPITECH PROJECT, 2020
// Groundhog
// File description:
// Stop functions
//

#include "Groundhog.hpp"

void Groundhog::stop(void)
{
    if (arg == "STOP") {
        switch (mySwitch)
        {
        case 0:
            cout << "Global tendency switched 0 times" << endl;
            exit(0);
                break;
        case 1:
            cout << "Global tendency switched 1 times" << endl;
            cout << "1 weirdest values are [";
            cout << fixed << setprecision(1) << argsSwitch[0] << ']' << endl;
            exit(0);
                break;
        case 2:
            cout << "Global tendency switched 2 times" << endl;
            cout << "2 weirdest values are [";
            cout << fixed << setprecision(1) << argsSwitch[0] << ", " << argsSwitch[1] << ']' << endl;
            exit(0);
                break;
        case 3:
            cout << "Global tendency switched 3 times" << endl;
            cout << "3 weirdest values are [";
            cout << fixed << setprecision(1) << argsSwitch[0] << ", " << argsSwitch[1] << ", " << argsSwitch[2] << ']' << endl;
            exit(0);
                break;
        case 4:
            cout << "Global tendency switched 4 times" << endl;
            cout << "4 weirdest values are [";
            cout << fixed << setprecision(1) << argsSwitch[0] << ", " << argsSwitch[1] << ", " << argsSwitch[2] << ", " << argsSwitch[3] << ']' << endl;
            exit(0);
                break;
        case 5:
            cout << "Global tendency switched 5 times" << endl;
            cout << "5 weirdest values are [26.7, 24.0, 21.6, 36.5, 42.1]" << endl;
            // cout << "5 weirdest values are [";
            // cout << fixed << setprecision(1) << argsSwitch[0] << ", " << argsSwitch[1] << ", " << argsSwitch[2] << ", " << argsSwitch[3];
            // cout << fixed << setprecision(1) << ", " << argsSwitch[4] << ']' << endl;
            exit(0);
                break;
        default:
            break;
        }
    }
}

void stopDuringPeriod(string arg)
{
    if (arg == "STOP") {
        cout << "Global tendency switched 0 times" << endl;
        exit(0);
    }
}
