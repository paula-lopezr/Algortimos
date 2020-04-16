#include "carro.hpp"

Carro::Carro(int Numas){
  this -> Numas = Numas;  //Numero de asientos disponibles
}

int Carro::getAs(){
  return Numas;  //Retorna el numero de asientos disponibles
}

void Carro::setAs(int dispo){
  if(dispo<=Numas)
    Numas -= dispo;
  //Al total  de asientos disponibles le restamos la cantidad
  //de personas que se haya subido al Carro para tener un nuevo numero de asientos
  else{
    cout<<"No hay cupo para tantas personas.\n";
  }
}

int Carro::straint(string k){
  int num = stoi(k);
  return num;
}
