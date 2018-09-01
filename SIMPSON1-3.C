s//...Header files declaration
#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<process.h>
#include<string.h>
//...Function prototype Declaration
float fun(float);
//....main execution thread
void main()
{
//...variable declaration field
//...floating type
float result=1;
float a,b;
float h,sum;
//..interger type
int i,j;
int n;
clrscr();
//...input range
printf("\nenter the range:");
printf("\nlower limit a:");
scanf("%f",&a);
printf("\nUpper limit b:");
scanf("%f",&b);
//...input number of subintervals
printf("\n\nEnter number of subintervals:");
scanf("%d",&n);
//...Calculation and Processing section
h=(b-a)/n;
sum=0;
sum=fun(a)+4*fun(a+h)fun(b);
for(i=3;i<n;i+=2)
{
sum+=2*fun(a+(i-1)*h)+4*fun(a+i*h);
}
result=sum*h/3;

//..output section
printf("\n\nValue of the integral is %6.4f\t",result);
printf("\n\nPress enter to Exit");
getch();
}

     //... Termination of Main execution thread
     //..function body
     float fun(float x)
     {
     float temp;
     temp=1/(1+(x*x));
     return temp;
     }