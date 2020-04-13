
#ifndef _CARRO_HPP_
#define _CARRO_HPP_

#include <iostream>
using namespace std;


class Carro {
private:
  int Numas;
public:
  Carro(int Numas);
  void setAs( int dispo);
  int getAs();
  int straint(string k);
};
 #endif
