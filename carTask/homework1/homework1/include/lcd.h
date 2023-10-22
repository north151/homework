#pragma once

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// 液晶显示屏
typedef struct _lcd
{
    string type = "super"; // 尺寸   (11.6)
    float size = 11.6;     // 型号   (super)

    void save(string _saveFileName)
    {
        ofstream fw;
        fw.open(_saveFileName, ios::app);
        fw << "<液晶显示器信息>" << endl;
        fw << "尺寸: " << size << endl;
        fw << "型号: " << size << endl;
        fw.close();
        return;
    }

} LCD;