#pragma once
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class CStudent
{
private:
    string studentNumber; // 学号
    string studentName;   // 姓名

public:
    CStudent() {}
    ~CStudent() {}

    void print();
    void save(string _saveFileName);

    void setStudentNumber(string _studentNumber);
    void setStudentName(string _studentName);
};