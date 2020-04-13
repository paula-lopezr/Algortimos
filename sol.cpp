#include <fstream>
#include "carro.hpp"

using namespace std;
//Tengo que mirara como poner bien el python
int main(){
  string cadena;
  string dispo;
  ifstream fe("Dispo.txt");
  ifstream hi("Asientos.txt");
  while(!fe.eof()){
    fe>>cadena;
    // cout<<cadena<<endl;
  }
  while(!hi.eof()){
    hi>>dispo;
  }
  Carro carrito(stoi(dispo));//Entra el numero de asientos
  carrito.setAs(carrito.straint(cadena));
  

  fe.close();
  ofstream file;
  file.open("Asientos.txt");
  file.close();
  return 0;
}
