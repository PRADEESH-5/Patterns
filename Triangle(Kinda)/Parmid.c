#include<stdio.h>
void main(){
    int n;
    printf("Enter Rows:");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        for(int j=i;j<n;j++){
            printf(" ");
        }
        for(int k=0;k<=i;k++){
            printf("* ");
        }
        printf("\n");
    }
}