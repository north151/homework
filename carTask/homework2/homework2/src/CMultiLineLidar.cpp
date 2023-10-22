#include "../include/CMultiLineLidar.h"

void CMultiLineLidar::print()
{
    cout << "<多线激光雷达信息>" << endl;
    cout << "型号: " << this->type << endl;
    cout << "通道数: " << this->numberOfChannels << endl;
    cout << "测试范围: " << this->testSpecification << "m" << endl;
    cout << "功耗: " << this->powerDissipation << "w" << endl;
    return;
}

void CMultiLineLidar::save(string _saveFileName)
{
    ofstream fw;
    fw.open(_saveFileName, ios::app);
    fw << "<多线激光雷达信息>" << endl;
    fw << "型号: " << this->type << endl;
    fw << "通道数: " << this->numberOfChannels << endl;
    fw << "测试范围: " << this->testSpecification << "m" << endl;
    fw << "功耗: " << this->powerDissipation << "w" << endl;
    fw.close();
    return;
}

void CMultiLineLidar::setType(string _type)
{
    this->type = _type;
    return;
}

void CMultiLineLidar::setNumberOfChannels(int _numberOfChannels)
{
    this->numberOfChannels = _numberOfChannels;
    return;
}

void CMultiLineLidar::setTestSpecification(float _testSpecification)
{
    this->testSpecification = _testSpecification;
    return;
}

void CMultiLineLidar::setPowerDissipation(float _powerDissipation)
{
    this->powerDissipation = _powerDissipation;
    return;
}
