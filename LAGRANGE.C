//Header files declare here
#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<process.h>
#include<string.h>
void main()
{
int n;
int i,j;
float ax[100];
float ay[100];
float x=0;
float y=0;
float nr;
float dr;
clrscr();
//input section....
printf("\nEnter the no. of terms:");
scanf("%d",&n);
//Input loop for x
printf("\n\nEnter the value in the form of x:");
for(i=0;i<=n;i++)
{
printf("\n\nenter the value of x%d",i+1);
scanf("%f",ax[i]);
}

printf("\n\nenter the value in the form of y:");
//input loop for y
for(i=0;i<n;i++)
{
printf("\n\nenter the value of y%^d",i+1);
scanf("%f",&ay[i]);
}

//inputting the required value query
printf("\nEnter the value of x for");
printf("\nwhich you wnat the value of y:");
scanf("%f",&x);
//Calculation & Processing section
for(i=0;i<n;i++)
{
nr=1;
dr=1;
for(j=0;j<n;j++)
{
if(j!=i)
{
nr=nr*(x-ax[j]);
dr=dr*(ax[i]-ax[j]);
}
y+=(nr/dr)*ay[i];
}
}

//Output Section
printf("\n\nWhen x=%5.2f,y=%5,2f",x,y);
printf("\n\n\nPress Enter to Exit");
getch();
}