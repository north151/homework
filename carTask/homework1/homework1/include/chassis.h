#pragma once

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#include "tyre.h"

// 底盘
typedef struct _chassis
{
    string id;                       // 编号   (cqusn打头的16位数字+字母)
    string type = "SCOUT MINI";      // 型号   (SCOUT MINI)
    int wheelbase = 451;             // 轴距   (451mm)
    int wheeltrack = 490;            // 轮距   (490mm)
    int minGroundClearance = 115;    // 最小离地间隙   (115mm)
    double minTurningRadius = 0;     // 最小转弯半径   (0m)
    string drivingForm = "四轮四驱"; // 驱动形式   (四轮四驱)
    double maxStroke = 10;           // 最大行程   (10KM)
    TYRE tyre;                       // 轮胎

    void save(string _saveFileName)
    {
        ofstream fw;
        fw.open(_saveFileName, ios::app);
        fw << "<底盘信息>" << endl;
        fw << "编号: " << id << endl;
        fw << "型号: " << type << endl;
        fw << "轴距: " << wheelbase << "mm" << endl;
        fw << "轮距: " << wheeltrack << "mm" << endl;
        fw << "最小离地间隙: " << minGroundClearance << "mm" << endl;
        fw << "最小转弯半径: " << minTurningRadius << "m" << endl;
        fw << "驱动模式: " << drivingForm << endl;
        fw << "最大行程: " << maxStroke << "KM" << endl;
        fw.close();
        tyre.save(_saveFileName);
        return;
    }

} CHASSIS;