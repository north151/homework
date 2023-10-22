#pragma once

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class CNineAxisGyroscope
{
private:
    string type = "CH110";
    string manufactor = "NXP";

public:
    CNineAxisGyroscope(){};
    ~CNineAxisGyroscope(){};
    void print();
    void save(string _saveFileName);

    void setType(string _type);
    void setManufactor(string _manufactor);
};