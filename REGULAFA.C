#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define f(x) ((x*x*x)-18)
int main()
{
float a=0,b=0,error=0,c,cold;
int i=0;
printf("input interval:");
scanf("%f%f",&a,&b);
if((f(a)*f(b))>0)
{
printf("invalid interval exit!");
exit(1);
}
else if((f(a)==0) || (f(b)==0))
{
printf("root is one of interval bounds");
exit(0);
}
printf("Ite\ta\t\tb\t\tc\t\tf(c)\t\terror\n");
do{
cold=c;
c=((a*f(b))-(b*f(a)))/(f(b)-f(a));
printf("%2d\t%4.6f\t%4.6f\t%4.6f\t%4.6f");
if(f(c)==0)
{
break;
}
else if(f(a)*f(c)<0)
{
b=c;
}
else  a=c;
error=fabs(c-cold);
if(i==1)
{
printf("----\n");
}
else
printf("%4.6f\n",error);
}
while(error>0.00005);
printf("root is %4.6f\n",c);
return 0;
}