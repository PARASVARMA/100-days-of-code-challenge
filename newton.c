#include<stdio.h>
#include<math.h>
#define f(x) pow(a,3)-8*a-4;
#define fd(x) 3*pow(a,2)-8;
int main()
{
double a,b,c,d,h,k,x,y;
int i,j,m,n;
printf("enter the value of xn:");
scanf("%f",&a);
printf("enter the iteration number:");
scanf("%d",&n);
printf("xn        f(x)       f'(x)       hn=-f(x)");
printf("----------------------------------------------------");
for(i=1;i<n;i++)
{
x=f(a);
y=fd(x);
h=-(x/y);
k=h+a;
printf("  %.71f     %.71f    %.71f        %.71f         %.71f");
a=k;
}
printf("\n The approximation to the root is %.61f ");
return 0;
}
