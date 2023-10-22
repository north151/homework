#pragma once

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#include "student.h"
#include "tyre.h"
#include "chassis.h"
#include "agxKit.h"
#include "binocularCamera.h"
#include "multiLineLidar.h"
#include "nineAxisGyroscope.h"
#include "lcd.h"
#include "batteryModule.h"

typedef struct _intelligentCar
{
    string id;                // 编号
    bool isAllocated = false; // 是否已经分配
    string saveFileName;      // 保存文件

    STUDENT student;                       // 学生
    CHASSIS chassis;                       // 底盘
    AGX_KIT agxKit;                        // AGX套件
    BINOCULAR_CAMERA binocularCamera;      // 双目摄像头
    MULTI_LINE_LIDAR multiLineLidar;       // 多线激光雷达
    NINE_AXIS_GYROSCOPE nineAxisGyroscope; // 9轴陀螺仪
    LCD lcd;                               // 液晶显示屏
    BATTERY_MODULE batteryModule;          // 电池模块

    void save()
    {
        saveFileName = "../carInfo/" + id + ".txt";
        string _saveFileName = saveFileName;
        fstream fw;
        // 清空文件
        fw.open(_saveFileName, ios::trunc);
        fw.clear();
        fw.close();
        // 开始写入
        fw.open(_saveFileName, ios::app);
        fw << "-----------------智能小车信息------------------" << endl;
        fw << "小车编号: " << id << endl;
        chassis.save(_saveFileName);
        agxKit.save(_saveFileName);
        binocularCamera.save(_saveFileName);
        multiLineLidar.save(_saveFileName);
        nineAxisGyroscope.save(_saveFileName);
        lcd.save(_saveFileName);
        batteryModule.save(_saveFileName);
        fw << "-----------------------------------------------" << endl;
        student.save(_saveFileName);
        fw << endl;
        fw.close();
        return;
    }

    void print()
    {
        ifstream fr;
        string _saveFileName = saveFileName;
        fr.open(_saveFileName, ios::in);
        string line;

        while (getline(fr, line)) // 逐行读取
        {
            cout << line << endl;
        }
        fr.close();
        return;
    }
} INTELLIGENT_CAR;
