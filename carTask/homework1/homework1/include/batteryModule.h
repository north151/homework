#pragma once

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// 电池模块
typedef struct _batteryModule
{
    string parameter = "24V/15Ah"; // 参数   (24V/15Ah)
    int externalPowerSupply = 24;  // 对外供电   (24V)
    float chargingTime = 2;        // 充电时长   (2H)

    void save(string _saveFileName)
    {
        ofstream fw;
        fw.open(_saveFileName, ios::app);
        fw << "<电池信息>" << endl;
        fw << "参数: " << parameter << endl;
        fw << "对外供电: " << externalPowerSupply << "V" << endl;
        fw << "充电时长: " << chargingTime << "H" << endl;
        fw.close();
        return;
    }

} BATTERY_MODULE;