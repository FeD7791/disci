#include <iostream>
#include <cstring>
using namespace std;



void printer(){
    int var1 = 10;//creo una variable
    int* var2 = &var1; //asigno a la variable var2 un adress
    int var3 = *var2;
    //cout << var2 <<"\n"; //Me devuelve el adress
    printf("WAIT\n");
    //cout << *var2; //con *var2 puedo acceder al valor que hay en el adress
    cout << var3 << "\n";
    for(int i=0;i<*var2;i++){
       
        cout << i << "\n";

    }
}

int main(){
    printer();
    return 0;
}






