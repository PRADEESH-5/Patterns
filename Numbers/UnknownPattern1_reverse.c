#include<stdio.h>
void main(){
    int n;
    printf("Enter Number:");
    scanf("%d",&n);
    int m=n;
    for (int i=n;i>=0;i--){
        for(int j=i;j>=0;j--){
            printf("%d",m);
            m--;
        }
        m+=i;
        printf("\n");
    }
}