#pragma once

#include <string>
#include <iostream>
#include <fstream>

#include "../include/CTyre.h"

using namespace std;

class CChassis // 底盘类
{
private:
    string id;                       // 编号   (cqusn打头的16位数字+字母)
    string type = "SCOUT MINI";      // 型号   (SCOUT MINI)
    int wheelbase = 451;             // 轴距   (451mm)
    int wheeltrack = 490;            // 轮距   (490mm)
    int minGroundClearance = 115;    // 最小离地间隙   (115mm)
    double minTurningRadius = 0;     // 最小转弯半径   (0m)
    string drivingForm = "四轮四驱"; // 驱动形式   (四轮四驱)
    double maxStroke = 10;           // 最大行程   (10KM)
    CTyre tyre;                      // 轮胎

public:
    CChassis() {}
    ~CChassis() {}
    CChassis(CTyre _tyre) {}
    void print();
    void save(string _saveFileName);

    void setId(string _id);
    void setType(string _type);
    void setWheelBase(int _wheelbase);
    void setWheelTrack(int _wheeltrack);
    void setMinGroundClearance(int _minGroundClearance);
    void setMinTurningRadius(int _minTurningRadius);
    void setDrivingForm(string _drivingForm);
    void setMaxStroke(int _maxStroke);
    void setTyre(CTyre _tyre);
};
