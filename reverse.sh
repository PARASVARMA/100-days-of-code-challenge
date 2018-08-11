echo "enter a no."
read num
rev=0
while [ $num -ne 0 ]
do 
rem=`expr $num % 10`
rev=`expr $rev \* 10 + $rem`
num=`expr $num / 10`
done 
echo "reverse of the given no. is "$rev
