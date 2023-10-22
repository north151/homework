#pragma once

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class CTyre
{
private:
    string type = "公路轮、麦克纳姆轮";
    int size = 175;
    int amount = 4;

public:
    void print();
    void save(string _saveFileName);

    void setType(string type);
    void setSize(int _size);
    void setAmount(int _amount);
};