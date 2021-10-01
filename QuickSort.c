#include<stdio.h>
int quick(int a[],int, int);
int partition(int a[],int, int);
void swap(int*,int*);
int main()
{
    int n;
    printf("Enter the size of array");
    scanf("%d",&n);
    int a[n];
    int i,lb=0,ub=n-1,loc;
    printf("enter the data of array to be sorted");
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    quick(a,lb,ub);
     printf("sorted data of array=");
        for(i=0;i<n;i++)
            printf(" %d",a[i]);
}
int quick(int a[],int lb,int ub)
{
    int loc,i;
    if(lb<ub)
    {
        loc=partition(a,lb,ub);
        quick(a,lb,loc-1);
        quick(a,loc+1,ub);
    }

}
int partition(int a[],int lb,int ub)
{
    int pivot,start,end,t,u;
    pivot=a[lb];
    start=lb;
    end=ub;
    while(start<end)
    {
        while(a[start]<=pivot)
        start++;
        while(a[end]>pivot)
        end--;
        if(start<end)
            {
                t=a[start];
                a[start]=a[end];
                a[end]=t;
            }
    }
            u=a[end];
                a[end]=a[lb];
                a[lb]=u;

    return(end);
}
