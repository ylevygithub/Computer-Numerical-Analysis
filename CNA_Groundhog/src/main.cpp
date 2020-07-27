//
// EPITECH PROJECT, 2020
// groundhog
// File description:
// main.cpp
//

#include "Groundhog.hpp"

void PrintUsage(int ac, char **av)
{
    if (ac != 2) {
        cerr << "Need one argument. No less no more." << endl;
        exit(84);
    }
    if (strcmp(av[1], "-h") == 0) {
        cout << "SYNOPSIS\n\t./groundhog period\n" << endl;
        cout << "\nDESCRIPTION\n\tperiod\t\tthe number of days defining a period" << endl;
        exit(0);
    }
    if (CheckArg(av[1]) == 1 && strcmp(av[1], "-h") != 0) {
        cerr << "The period needs to be a number" << endl;
        exit(84);
    }
}

int main(int ac, char **av)
{
    PrintUsage(ac, av);
    try {
        Groundhog ground;
        ground.Ground(av[1]);
    }
    catch (MyException &msg) {
        cerr << msg.what() << endl;
        return (84);
    }
    return (0);
}
