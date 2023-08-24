#include <stdio.h>
#include <stdlib.h>
#include "holberton.h"


void mul(char *num1, char *num2)
{
    unsigned int n1, n2, mul;
    char result[1024];
    char *res;

    n1 = atoi(num1);
    n2 = atoi(num2);

    mul = n1 * n2;
    sprintf(result, "%u", mul);

    res = result;
    while (*res != '\0')
    {
        _putchar(*res);
        res++;
    }
    _putchar('\n');
}

void errorPrint()
{
    char err[] = "Error\n";
    char *er = err;
    int i = 0;

    while (*er != '\0')
    {
        _putchar(*er);
        er++;
        i++;
    }
}

int isDigit(char *n1, char *n2)
{
    int isdigit = 0;

    while (*n1 != '\0')
    {
        if (!((*n1 - '0') <= 9 && (*n1 - '0') >= 0))
            isdigit = 1;
        n1++;
    }
    while (*n2 != '\0')
    {
        if (!((*n2 - '0') <= 9 && (*n2 - '0') >= 0))
            isdigit = 1;
        n2++;
    }
    return isdigit;
}

int main(int argc, char *argv[])
{
    int isdigit;

    if (argc < 3)
    {
        errorPrint();
        exit(98);
    }

    isdigit = isDigit(argv[1], argv[2]);
    if (isdigit) {
        errorPrint();
        exit(98);
    }

    mul(argv[1], argv[2]);

    return (0);
}
