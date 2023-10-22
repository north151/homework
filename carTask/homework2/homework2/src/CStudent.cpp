#include "../include/CStudent.h"

#include <iostream>
#include <string>
#include <fstream>

void CStudent::print()
{
    cout << "学号: " << this->studentNumber << endl;
    cout << "姓名: " << this->studentName << endl;
    return;
}

void CStudent::save(string _saveFileName)
{
    ofstream fw;

    fw.open(_saveFileName, ios::app);
    fw << "-----------------分配学生信息------------------" << endl;
    fw << "学生学号: " << this->studentNumber << endl;
    fw << "学生姓名: " << this->studentName << endl;
    fw.close();
    return;
}

void CStudent::setStudentNumber(string _studentNumber)
{
    this->studentNumber = _studentNumber;
    return;
}

void CStudent::setStudentName(string _studentName)
{
    this->studentName = _studentName;
    return;
}
