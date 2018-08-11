echo "enter  a number :"
read a 
f=1
while [ $a -gt 1 ]
do 
f=`expr $a \* $f`
a=`expr $a -1`
done
echo "factorial of number is $f"
