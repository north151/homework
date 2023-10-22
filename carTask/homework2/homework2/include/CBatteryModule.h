#pragma once

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class CBatteryModule
{
private:
    string parameter = "24V/15Ah"; // 参数   (24V/15Ah)
    int externalPowerSupply = 24;  // 对外供电   (24V)
    float chargingTime = 2;        // 充电时长   (2H)
public:
    CBatteryModule(){};
    ~CBatteryModule(){};
    void print();
    void save(string _saveFileName);

    void setParameter(string _parameter);
    void setOutputVoltage(int _externalPowerSupply);
    void setChargeTime(int _chargingTime);
};
