#pragma once

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class CMultiLineLidar
{
private:
    string type = "RS-Helios-16p"; // 型号   (RS-Helios-16p)
    int numberOfChannels = 16;     // 通道数   (16)
    float testSpecification = 100; // 测试范围   (100m)
    float powerDissipation = 8;    // 功耗   (8W)

public:
    CMultiLineLidar(){};
    ~CMultiLineLidar(){};
    void print();
    void save(string _saveFileName);

    void setType(string _type);
    void setNumberOfChannels(int _numberOfChannels);
    void setTestSpecification(float _testSpecification);
    void setPowerDissipation(float _powerDissipation);
};
