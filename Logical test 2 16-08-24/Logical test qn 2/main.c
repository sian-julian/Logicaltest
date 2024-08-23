
#include <stdio.h>

int main()
{
    int i,j,k,n=5;
    
    for(i=0;i<1;i++)
    {
        for(j=0;j<n*2;j++)
        {
            printf("*");
        }
        printf("\n");
    }
    
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(j==i || j==n-i-1)
            {
                printf("* ");
            }
            else
            {
                printf("  ");
            }
        }
        printf("\n");
    }
    
    for(i=0;i<1;i++)
    {
        for(j=0;j<n*2;j++)
        {
            printf("*");
        }
    }

    return 0;
}