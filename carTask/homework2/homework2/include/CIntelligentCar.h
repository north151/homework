#pragma once

#include <string>
#include <iostream>
#include <fstream>

#include "CStudent.h"
#include "CChassis.h"
#include "CTyre.h"
#include "CAgxKit.h"
#include "CBinocularCamera.h"
#include "CMultiLineLidar.h"
#include "CNineAxisGyroscope.h"
#include "CLcd.h"
#include "CBatteryModule.h"

using namespace std;

class CIntelligentCar
{
private:
    string id;                // 编号
    bool isAllocated = false; // 是否已经分配
    string saveFileName;      // 保存文件

    CStudent student;                     // 分配学生
    CChassis chassis;                     // 底盘
    CAgxKit agxKit;                       // Agx套件
    CBinocularCamera binocularCamera;     // 双目摄像头
    CMultiLineLidar multiLineLidar;       // 多线激光雷达
    CNineAxisGyroscope nineAxisGyroscope; // 9轴陀螺仪
    CLcd lcd;                             // 液晶显示屏
    CBatteryModule batteryModule;         // 电池

public:
    CIntelligentCar();
    ~CIntelligentCar() {}
    CIntelligentCar(string _id,                            // 编号
                    CStudent _student,                     // 分配学生
                    CChassis _chassis,                     // 底盘
                    CAgxKit _agxKit,                       // Agx套件
                    CBinocularCamera _binocularCamera,     // 双目摄像头
                    CMultiLineLidar _multiLineLidar,       // 多线激光雷达
                    CNineAxisGyroscope _nineAxisGyroscope, // 9轴陀螺仪
                    CLcd _lcd,                             // 液晶显示屏
                    CBatteryModule _batteryModule          // 电池
    );

    void print();
    void save();

    void setId(string _id);
    string getId();
    void setIsAllocated(bool _isAllocated);
    bool getIsAllocated();
    string getSaveFileName();
};
