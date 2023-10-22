#pragma once

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// 9轴陀螺仪
typedef struct _nineAxisGyroscope
{
    string type = "CH110";     // 型号   (CH110)
    string manufactor = "NXP"; // 厂家   (NXP)

    void save(string _saveFileName)
    {
        ofstream fw;
        fw.open(_saveFileName, ios::app);
        fw << "<9轴陀螺仪信息>" << endl;
        fw << "型号: " << type << endl;
        fw << "厂家: " << manufactor << endl;
        fw.close();
        return;
    }
} NINE_AXIS_GYROSCOPE;