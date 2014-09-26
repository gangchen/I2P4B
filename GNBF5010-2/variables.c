/*
Source codes to demonstrate variables in C
AUTHOR: Gang CHEN
*/

#include <stdio.h>

int main(){
    char ch1 = 'A';
    printf("The character is %c\n", ch1);
    printf("The integer is %i\n", ch1);

    printf("\n");

    int int1 = 65;
    printf("The integer is %i\n", int1);
    printf("The ASCII character is %c\n", int1);

    printf("\n");

    float f1 = 65;
    printf("The float number is %f\n", f1);
    printf("The ASCII character is %c\n", f1);
    float f2 = 29292929292965.0e100;
    printf("The float number is %f\n", f1);

    printf("\n");

    double d1 = 29292929292965.0e100;
    printf("The double float number is %f\n", d1);

    printf("\n");

    int intarray1[3] = {1,2,3};
    printf("The first number is %i\n", intarray1[0]);
    printf("The second number is %i\n", intarray1[1]);

    printf("\n");

    char s1[4] = {'a', 'b', 'c', 'd'};
    printf("The first char is %c\n", s1[0]);
    printf("The second char is %c\n", s1[1]);
    printf("The third char is %c\n", s1[2]);
    printf("The forth char is %c\n", s1[3]);
    printf("The string is %s\n", s1);

    char s2[4] = "ABCD";
    printf("The first char is %c\n", s2[0]);
    printf("The second char is %c\n", s2[1]);
    printf("The third char is %c\n", s2[2]);
    printf("The forth char is %c\n", s2[3]);
    printf("The string is %s\n", s2);

    printf("\n");

    int intarray2[4] = {2,4,6,8};
    int *p1 = &intarray2[1];
    printf("The value of pointer is %i\n",*p1);
    // what is the difference between the following two statements?
    printf("%i\n", *(p1+1));
    printf("%i\n", *p1+1);


    return 0;
}
