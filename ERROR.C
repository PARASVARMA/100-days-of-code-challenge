#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
float true_val,approx_val,absolute_err,relative_err,percentage_err;
clrscr();
printf("enter the value of true value and approximate value");
scanf("%f%f",true_val,approx_val);
absolute_err=(true_val-approx_val);
relative_err=absolute_err/true_val;
percentage_err=relative_err*100;
printf("The absolute error is %f",absolute_err);
printf("The relative error is %f",relative_err);
printf("The percentage error is %f",percentage_err);
getch();
}