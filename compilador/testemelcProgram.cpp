#include <stdio.h>

main () {

    int A, S, NUM ;

    A = 1 ;
    S = 0 ;

    scanf ( "%d", &NUM ) ;
    
    if ( NUM > 0 )
        S = S + A ;
    A = A + 1 ;

    printf ( "%d", S ) ;
}