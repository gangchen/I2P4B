#include <stdio.h>

int main(){

    float f1 = 24.4, f2 = 25.6;
    int i1 = 16, i2 =5;

    printf("f1 + f2 = %f\n", f1 + f2);
    printf("f1 / f2 = %f\n", f1 / f2);
    printf("f1 * f2 = %f\n", f1 * f2);
    printf("f1 - f2 = %f\n", f1 - f2);

    printf("i1 %% i2 = %i\n", i1 % i2);

    printf("f1 > f2 is %i\n", f1 > f2); // 0:FALSE
    printf("f1 < f2 is %i\n", f1 < f2); // 1:TRUE
    printf("2 == 2 is %i\n", 2 == 2); //TRUE
    printf("3 != 2 is %i\n", 3 != 2);

    printf("3 == 2 && 2 == 2 is %i\n", 3 == 2 && 2 == 2);
    printf("3 != 2 || 2 == 2 is %i\n", 3 != 2 && 2 == 2);

    //a puzzle
    printf("1.3 - 0.7 = %f\n", 1.3 - 0.7);
    printf("1.3 - 0.7 == 0.6 is %i\n", 1.3 -0.7 == 0.6); //FALSE?
    printf("1.3 - 0.7 != 0.6 is %i\n", 1.3 -0.7 != 0.6); //TRUE?


    return 0;
}
