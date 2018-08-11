echo "enter  the  no."
read n
if [`expr $n % 2` -eq 0]
then
echo "no. is even"
else 
echo "no. is odd"
fi
