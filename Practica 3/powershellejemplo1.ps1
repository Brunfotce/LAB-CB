$var=Read-Host "Ingrese un texto:"
echo "Cuantas veces repetira texto?"
$vari=Read-Host
$yes=1
out-file "tacto-tacto.txt"
while ($yes -le $vari){
    $mos=$var + " numero:" + $yes
    echo $mos | Out-File -FilePath "C:\Users\USER\Desktop\ciberseguridad\LABS\Practica 3\tacto-tacto.txt" -Append 
    $yes=$yes+1
}