#pragma once

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class CLcd
{
private:
    string type = "super"; // 尺寸   (11.6)
    float size = 11.6;     // 型号   (super)

public:
    CLcd(){};
    ~CLcd(){};
    void print();
    void save(string _saveFileName);

    void setType(string _type);
    void setSize(float _size);
};
