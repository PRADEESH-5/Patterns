#include<stdio.h>
#include<string.h>
void main(){
    char a[100];
    printf("Enter a string:");
    scanf("%s",a);
    int n=strlen(a);
    for(int i=0;i<n;i++){
        for(int j=0;j<=i;j++){
            printf("%c",a[j]);
        }
        printf("\n");
    }
}