
#include <stdio.h>
#include <string.h>

int main()
{
    char s[100],ch,temp[100];
    int len,i;
    printf("Enter a string:");
    fgets(s,100,stdin);
    len=strlen(s);
    printf("length:%d\n",len);
    printf("Enter the character you want to remove:");
    scanf("%c",&ch);
    
    
    for(i=0;i<len-1;i++)
    {
        if(s[i]==ch)
        {
            continue;
        }
        else
        {
            printf("%c",s[i]);
        }
    }
    


    return 0;
}