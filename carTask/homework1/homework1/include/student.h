#pragma once

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

typedef struct _student
{
    string studentNumber;           // 学号
    string studentName;             // 姓名
    void save(string _saveFileName) // 保存信息
    {
        ofstream fw;
        fw.open(_saveFileName, ios::app);
        fw << "-----------------分配学生信息------------------" << endl;
        fw << "学生学号: " << studentNumber << endl;
        fw << "学生姓名: " << studentName << endl;
        fw.close();
        return;
    }
} STUDENT;
