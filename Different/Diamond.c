#include<stdio.h>
void main(){
    int n;
    printf("Enter value for n:");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        for(int j=n;j>i;j--){
            printf(" ");
        }
        for (int k=0;k<=i;k++){
            printf("* ");
        }
        printf("\n");
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<=i;j++){
            printf(" ");
        }
        for (int k=n;k>i;k--){
            printf("* ");
        }
        printf("\n");
    }
}