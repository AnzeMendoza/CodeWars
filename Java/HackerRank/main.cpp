#include <iostream>
#include <list>

using namespace std;

int main(int argc, char const *argv[])
{
    list<int> linkedList = {1, 2, 3, 4, 5};

    for(int i: linkedList){
        cout<<i<<endl;
    }

}
