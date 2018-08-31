#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<process.h>
//....Function prototype declaration
float fun(float);
//..main execution thread
void main()
{
//...variable declaration field
//..floating type
float result=1;
float a,b;
float h,sum;
//..integer type
int i,j,n;
//..invoke clear screen function
clrscr();
//..input section
//..input range
printf("\n\n Enter the range- ");
printf("\n\n Lower limit a - ");
scanf("%f",&a);
printf("\n Upper limit b- ");
scanf("%f",&b);
//..input number of subintervals
printf("\nEnter number of subintervals- ");
scanf("%d",&n);
//..Calculation and Processing section
h=(b-a)/n;
sum=0;
sum=fun(a)+fun(b);
for(i=1;i<n;i++)
{
if(i%3==0)
{
sum+=2*fun(a+i*h);
}
else
{
sum+=3*fun(a+(i)*h);
}
}
result=sum*3*h/8;
//...output section
printf("\n\n Value of the integral is %6.4f\t",result);
printf("\n\n Press enter to Exit");
getch();
}

//...Terminate of Main Execution Thread
//... Fucntion Body
float fun(float x)
{
float temp;
temp=1/(1+(x*x));
return temp;
}
//...Termination of Function Body