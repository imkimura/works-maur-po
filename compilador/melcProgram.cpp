#include <stdio.h>

main() {

    int A, S, NUM;

    A = 1;
    S = 0;
    while (A<=100)

    {
        scanf("%d", &NUM);
        if (NUM > 0)
            S = S + NUM;
        A = A + 1;

    }
    printf ("%d", S);
}