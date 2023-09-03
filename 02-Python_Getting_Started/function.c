#include <stdio.h>


int add(int a, int b){
    return a + b;
}

int main(){
    int i1 = 3, i2 = 5;
    printf("i1 + i2 = %i\n", i1 + i2);
    printf("add(i1, i2) = %i\n", add(i1, i2));

    return 0;
}
