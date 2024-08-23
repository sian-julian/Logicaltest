
#include <stdio.h>

int main()
{
    int arr[500],n,j,i,temp;
    int b[500];
    printf("Enter the size:");
    scanf("%d",&n);
    printf("Enter the elements of the array:");
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i=i+2)
    {
        b[i]=arr[i];
    }
    
    
    printf("Array elements at even indices:\n");
    for(i=0;i<n;i=i+2)
    {
        printf("%d\n",b[i]);
    }

    return 0;
}