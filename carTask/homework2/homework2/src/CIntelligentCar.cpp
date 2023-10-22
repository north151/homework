#include <iostream>
#include <fstream>

#include "../include/CIntelligentCar.h"

CIntelligentCar::CIntelligentCar()
{
    this->saveFileName = "../carInfo/" + this->id + ".txt";
    return;
}

CIntelligentCar::CIntelligentCar(string _id, CStudent _student, CChassis _chassis, CAgxKit _agxKit, CBinocularCamera _binocularCamera, CMultiLineLidar _multiLineLidar, CNineAxisGyroscope _nineAxisGyroscope, CLcd _lcd, CBatteryModule _batteryModule)
{
    this->id = _id;
    this->student = _student;
    this->chassis = _chassis;
    this->agxKit = _agxKit;
    this->binocularCamera = _binocularCamera;
    this->multiLineLidar = _multiLineLidar;
    this->nineAxisGyroscope = _nineAxisGyroscope;
    this->lcd = _lcd;
    this->batteryModule = _batteryModule;
    this->saveFileName = "../carInfo/" + this->id + ".txt";
    return;
}

void CIntelligentCar::print()
{
    ifstream fr;
    string _saveFileName = this->saveFileName;
    fr.open(_saveFileName, ios::in);
    string line;

    while (getline(fr, line)) // 逐行读取
    {
        cout << line << endl;
    }
    fr.close();
    return;
}

void CIntelligentCar::save()
{
    ofstream fw;
    string _saveFileName = this->saveFileName;
    // 清空文件
    fw.open(_saveFileName, ios::trunc);
    fw.clear();
    fw.close();
    // 开始写入
    fw.open(_saveFileName, ios::app);
    fw << "-----------------智能小车信息------------------" << endl;
    fw << "小车编号: " << this->id << endl;
    this->chassis.save(_saveFileName);
    this->agxKit.save(_saveFileName);
    this->binocularCamera.save(_saveFileName);
    this->multiLineLidar.save(_saveFileName);
    this->nineAxisGyroscope.save(_saveFileName);
    this->lcd.save(_saveFileName);
    this->batteryModule.save(_saveFileName);
    fw << "-----------------------------------------------" << endl;
    this->student.save(_saveFileName);
    fw << endl;
    fw.close();
    return;
}

void CIntelligentCar::setId(string _id)
{
    this->id = _id;
    return;
}

string CIntelligentCar::getId()
{
    return this->id;
}

void CIntelligentCar::setIsAllocated(bool _isAllocated)
{
    this->isAllocated = _isAllocated;
    return;
}

bool CIntelligentCar::getIsAllocated()
{
    return this->isAllocated;
}

string CIntelligentCar::getSaveFileName()
{
    return this->saveFileName;
}