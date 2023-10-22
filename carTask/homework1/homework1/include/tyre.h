#pragma once

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// 轮胎
typedef struct _tyre
{
    string type = "公路轮、麦克纳姆轮";
    int size = 175;
    int amount = 4;

    void save(string _saveFileName)
    {
        ofstream fw;
        fw.open(_saveFileName, ios::app);
        fw << "轮胎信息:" << endl;
        fw << "轮胎数量: " << amount << "个" << endl;
        fw << "轮胎型号: " << type << endl;
        fw << "轮胎尺寸: " << size << "mm" << endl;
        fw.close();
        return;
    }

} TYRE;