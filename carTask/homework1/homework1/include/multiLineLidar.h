#pragma once

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// 多线激光雷达
typedef struct _multiLineLidar
{
    string type = "RS-Helios-16p"; // 型号   (RS-Helios-16p)
    int numberOfChannels = 16;     // 通道数   (16)
    float testSpecification = 100; // 测试范围   (100m)
    float powerDissipation = 8;    // 功耗   (8W)

    void save(string _saveFileName)
    {
        ofstream fw;
        fw.open(_saveFileName, ios::app);
        fw << "<多线激光雷达信息>" << endl;
        fw << "型号: " << type << endl;
        fw << "通道数: " << numberOfChannels << endl;
        fw << "测试范围: " << testSpecification << "m" << endl;
        fw << "功耗: " << powerDissipation << "w" << endl;
        fw.close();
        return;
    }

} MULTI_LINE_LIDAR;