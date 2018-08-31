#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<process.h>
#include<string.h>

//Function prototype declaration
float fun(float);
//main execution thread
void main()
{
//variable declaration field
float result=1;
float a,b,sum,h;
//integer type
int i,j;
int n;
clrscr();
//input section
printf("\nenter the range-");
printf("\nlower limit a-");
scanf("%f",&a);
printf("\n\nupper limit b- ");
scanf("%f",&b);
//...input number of subintervals
printf("\n\nenter number of subintervals-  ");
scanf("%d",&n);
//...Calculation and processing section
h=(b-a)/n;
sum=0;
sum=fun(a)+fun(b);
for(i=1;i<n;i++)
{
sum+=2*fun(a+i);
}
result=sum*h/2;
//output section..
printf("\n\nvalue of the integral is %6,4f\t",result);
//invoke user watch halt fuction
printf("\n\nPresss enter to Exit0");
getch();
}

//...termination of main execution thread
//...function body
float fun(float x)
{
float temp;
temp = 1/(1+(x*x));
return temp;
}
// now termination of function body.....