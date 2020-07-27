//
// EPITECH PROJECT, 2020
// Groundhog
// File description:
// verification functions
//

#include "Groundhog.hpp"

int CheckArg(char *arg)
{
    int end = strlen(arg);
    int i = 0;

    while (i < end) {
        if (arg[i] >= '0' && arg[i] <= '9')
            i++;
        else
            return (1);
    }
    return (0);
}

int CheckInput(string arg)
{
    int end = arg.length();
    int i = 0;

    while (i < end) {
        if (arg[0] == '-')
            i++;
        else if (arg[i] >= '0' && arg[i] <= '9' || arg[i] == '.')
            i++;
        else
            return (1);
    }
    return (0);
}

void ArgIsNotNum(string arg)
{
    if (CheckInput(arg) == 1 && (arg[0] != 'S'))
        throw MyException("ERROR : input is not num");
    if (arg[0] == '-' && arg[1] == '\0')
        throw MyException("ERROR : minus without any value");
}
