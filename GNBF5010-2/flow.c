#include <stdio.h>

int main(){

    int a = 2, b = 3;

    printf("IF-ELSE:\n");
    if(a > b){
        printf("a is bigger than b\n");
    }else{
        printf("a is not bigger than b\n");
    }

    printf("\n");
    printf("SWITCH:\n");
    switch(a){
        case 1: printf("a == 1\n");break;
        case 2: printf("a == 2\n");break;
        case 3: printf("a == 3\n");break;
        default:
            printf("a is nothing\n");
    }

    printf("\n");

    printf("FOR loop:\n");
    int i = 0;
    for(i = 0; i < 10; i++){
        printf("%i\n", i);
    }

    printf("\n");

    printf("WHILE loop:\n");
    int j = 0;
    while(j < 10){
        printf("%i\n", j);
        j++;
    }

    return 0;
}
