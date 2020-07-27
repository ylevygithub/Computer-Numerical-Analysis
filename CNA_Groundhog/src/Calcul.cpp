//
// EPITECH PROJECT, 2020
// Groundhog
// File description:
// calcules
//

#include "Groundhog.hpp"

double Groundhog::Sum(void)
{
    sum = 0;

    for (auto i = recordInputs.begin(); i != recordInputs.end(); i++)
        sum = sum + *i;
    return (sum);
}

double Groundhog::Average(void)
{
    average = 0;
    average = sum / period;
    return (average);
}

double Groundhog::SumOfSquares(void)
{
    sumOfSquares = 0;

    for (auto i = recordInputs.begin(); i != recordInputs.end(); i++)
        sumOfSquares = sumOfSquares + pow((*i - average), 2);
    return (sumOfSquares);
}

double Groundhog::Variance(void)
{
    variance = 0;
    variance = sumOfSquares / period;
    return (variance);
}

double Groundhog::StandardDeviation(void)
{
    standardDeviation = 0;
    standardDeviation = sqrt(variance);
    return (standardDeviation);
}

void Groundhog::AllSet(void)
{
    sum = Sum();
    average = Average();
    sumOfSquares = SumOfSquares();
    variance = Variance();
    standardDeviation = StandardDeviation();
}

void Groundhog::tempIncreaseAvg(void)
{
    g = average - AncienAverage;

    if (g < 0)
        g = 0.00;
    cout << "g=" << g << '\t';
}

void Groundhog::relativeEvolTemp(void)
{
    r = (recordInputs[period-1] / nDaysTemp) * 100 - 100;

    if ((r < 0 && ancienR == 0) || (r < 0 && ancienR > 0) || (r > 0 && ancienR < 0))
        verifNeg++;
    else if ((r < 0 && ancienR < 0) || (r > 0 && ancienR > 0))
        verifNeg = 0;
    cout << "r=";
    cout << fixed << setprecision(0) << r;
    cout << '%' << '\t' <<  "s=";
}
