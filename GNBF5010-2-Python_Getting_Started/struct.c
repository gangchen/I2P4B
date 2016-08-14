#include <stdio.h>

typedef struct{
    int x, y;
    double value;
}point;


typedef struct{
    double score;
    char level;
}value;

typedef struct{
    int x, y;
    value v;
}point1;

void printPoint(point p){
    printf("X is %i\n", p.x);
    printf("Y is %i\n", p.y);
    printf("The value is %f\n", p.value);
}

void printPoint1(point1 p){
    printf("X is %i\n", p.x);
    printf("Y is %i\n", p.y);
    printf("The score is %f\n", p.v.score);
    printf("The level is %c\n", p.v.level);
}

int main(){
    point p1;
    p1.x = 2;
    p1.y = 3;
    p1.value = 3.1415926;
    printPoint(p1);

    point p2 = {2, 3, 3.14};
    printPoint(p2);

    point p3 = {.y=3, .x=2, .value=3.1415};
    printPoint(p3);

    point1 p4 = {.x=2, .y=3, .v={.score=76, .level='A'}};
    printPoint1(p4);

    return 0;
}
