#include<stdio.h>
float calc(float temp)
{
float value;
value=1/(1 + temp*temp);
return(value);
}
int main()
{
int interval,limit,count=0;
float upper_limit,lower_limit,interval_gap,sum=0;
printf("\nLower limit:");
scanf("%f",&lower_limit);
printf("\nUpper limit");
scanf("%f",&upper_limit);
printf("\nTotal intervals:");
scanf("%d",&interval);
interval_gap=(upper_limit-lower_limit)/interval;
printf("\n\nInterval gap:%f",interval_gap);
limit=interval/6;
if(interval%6==0)
{
while(count<limit)
 {
 sum=sum+((3*interval_gap/10)*(calc(lower_limit)+calc(lower_limit+2*interval_gap)+5*calc(lower_limit+interval_gap)+6*calc(lower_limit+3*interval_gap)+calc(lower_limit+4*interval_gap)+5*calc(lower_limit+5*interval_gap)+calc(lower_limit+6*interval_gap)));
 lower_limit=lower_limit+6*interval_gap;
 count=count+1;
 }
 printf("\nWEdddle Rule is satisfied. Evaluated result :\t%f",sum);
}
else
{
printf("\nThe WEddle Rule is not satisfied");
}
return 0;
}