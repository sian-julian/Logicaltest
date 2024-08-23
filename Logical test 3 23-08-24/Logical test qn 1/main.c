
#include <stdio.h>

int main()
{
    int a[100],i,n;
    int digitcount[150]={0};
    printf("Enter the size of the array:");
    scanf("%d",&n);
    printf("Enter the elements of the array:");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    
    for(i=0;i<n;i++)
    {
        digitcount[a[i]]++;
    }
    
    for(i=0;i<n;i++)
    {
        if(digitcount[a[i]]==1)
        {
            printf("%d",a[i]);
            break;
        }
    }

    return 0;
}


