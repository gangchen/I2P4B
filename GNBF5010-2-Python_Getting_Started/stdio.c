#include <stdio.h>

int main(){

    char filename[30];
    scanf("%s",filename);

    FILE * f;
    f = fopen(filename, "r");
    if(f == NULL) {
        printf("ERROR\n");
        return 1;
    }

    char line[100];
    while(fgets(line, 100, f)!= NULL)
        printf("%s", line);

    fclose(f);
    return 0;
}
