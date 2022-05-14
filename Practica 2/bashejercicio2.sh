#                             Online Bash Shell.
#                 Code, Compile, Run and Debug Bash script online.
# Write your code in this editor and press "Run" button to execute it.

create () {
  touch $1.txt
}
delete (){
    rm -f $1.txt
}
echo Bienvenido al creador o destructor de archivos txt
echo 'a continuacion escoga que quiere hacer crear:(1) eliminar:(2)'
read des
if [ $des == 1 ]; then
    echo 'ingrese el nombre para crear:' 
    read word 
    create $word
else
    if [ $des == 2 ]; then
        echo 'ingrese el nombre para destruir:'
        read word
        delete $word
    else
        echo por favor ingrese un numero valido
    fi
    
fi