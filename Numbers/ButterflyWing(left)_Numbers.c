#include<stdio.h>
void main(){
    int n,m=0,c=0;
    printf("Enter Number:");
    scanf("%d",&n);
    for(int i=0;i<=n;i++){
        m=c;
        for(int j=0;j<=i;j++){
            printf("%d",m);
            m--;
        }
        c+=1;
        printf("\n");
    }
    m=n;
    for (int i=n;i>=0;i--){
        for(int j=i;j>=0;j--){
            printf("%d",m);
            m--;
        }
        m+=i;
        printf("\n");
    }
}