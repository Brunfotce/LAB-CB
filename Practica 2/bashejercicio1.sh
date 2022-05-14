a=0
while [ $a == 0 ]
do
	echo que palabras quiere encontrar en base a su palabra?
	read pal
	cat Albion.txt | sort | grep $pal
	echo presione 1 para terminar de recolectar info
	read a
 
done


