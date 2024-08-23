
#include <stdio.h>

int main()
{
    int a[100],i,len,n,temp,sum=0;
    printf("Enter the size of the array:");
    scanf("%d",&n);
    if(n==2)
    {
        printf("Enter the elments of the array:");
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        
        for(i=0;i<n;i++)
        {
            if(a[i]>a[i+1])
            {
                temp=a[i];
                break;
            }
            else
            {
                temp=a[i+1];
            }
        }
        printf("the Max amount of money:%d",temp);
    }
    else
    {
        printf("Enter the elements of the array:");
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        
        for(i=0;i<n;i=i+2)
        {
            sum=sum+a[i];
        }
        
        printf("The max amount of money:%d",sum);
    }
    

    return 0;
}