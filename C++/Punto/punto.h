#ifndef PUNTO_H
#define PUNTO_H
#include <iostream>

using namespace std;


class Punto
{
public:
  static int count;
public:
    Punto();
    Punto(double _x, double _y);
    Punto (double _x);
    Punto (const Punto& );
    Punto getPunto(){return *this;}
    void setX(double _x){x = verificaValor(_x);}
    void setY(double _y){y = verificaValor(_y);}
    static void printCount();
    void setPunto(const Punto& );
    double getX(){return x;}
    double getY(){return y;}
    void printPunto();
    Punto& operator+(const Punto & );
    Punto& operator-(const Punto & );
    Punto& operator=(const Punto & );
    friend ostream& operator<<(ostream&, const Punto& );
    friend istream& operator>>(istream&, Punto&);


private:
    double x;
    double y;
    double verificaValor(double );


};
int Punto::count=0;


#endif // PUNTO_H
