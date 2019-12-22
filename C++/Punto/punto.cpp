#include "punto.h"

double Punto::verificaValor(double k)
{
    if(k < -1000)
        return -1000;
    else if (k >1000)
        return 1000;
    else
        return k;
}

Punto::Punto()
{
    x = 0;
    y = 0;

}

Punto::Punto(double _x, double _y)
{
    x = verificaValor(_x);
    y = verificaValor(_y);
}

Punto::Punto(double _x)
{
    x = _x;
}

Punto::Punto(const Punto &p):x(p.x), y(p.y)
{
}
////////////////////////////////////////////////////////////////////////
void Punto::printCount()
{
    cout<<"instancias del objeto: "<<count<<endl;
}
////////////////////////////////////////////////////////////////////////
void Punto::setPunto(const Punto &p)
{
    x = p.x;
    y = p.y;
}

void Punto::printPunto()
{
    cout <<"("<<x<<","<<y<<")"<<endl;
}

Punto &Punto::operator+(const Punto &p)
{
    x+=p.x;
    y+=p.y;

    return *this;
}

Punto &Punto::operator-(const Punto &p)
{
    x-=p.x;
    y-=p.y;

    return *this;
}

Punto &Punto::operator=(const Punto &p)
{
    x = p.x;
    y = p.y;

    return *this;
}

istream& operator>>(istream &i, Punto &p)
{
    cout<<"ingrese x: ";
    i >> p.x;
    cout<<"ingrese y: ";
    i>>p.y;

    return i;
}

ostream& operator<<(ostream & o, const Punto &p)
{
    o <<"("<<p.x<<","<<p.y<<")";
    return o;
}




