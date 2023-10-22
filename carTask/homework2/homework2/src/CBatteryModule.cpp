#include "../include/CBatteryModule.h"

void CBatteryModule::print()
{
    cout << "<电池信息>" << endl;
    cout << "参数: " << this->parameter << endl;
    cout << "对外供电: " << this->externalPowerSupply << "V" << endl;
    cout << "充电时长: " << this->chargingTime << "H" << endl;
    return;
}

void CBatteryModule::save(string _saveFileName)
{
    ofstream fw;
    fw.open(_saveFileName, ios::app);
    fw << "<电池信息>" << endl;
    fw << "参数: " << this->parameter << endl;
    fw << "对外供电: " << this->externalPowerSupply << "V" << endl;
    fw << "充电时长: " << this->chargingTime << "H" << endl;
    fw.close();
    return;
}

void CBatteryModule::setParameter(string _parameter)
{
    this->parameter = _parameter;
    return;
}

void CBatteryModule::setOutputVoltage(int _externalPowerSupply)
{
    this->externalPowerSupply = _externalPowerSupply;
    return;
}

void CBatteryModule::setChargeTime(int _chargingTime)
{
    this->chargingTime = _chargingTime;
    return;
}
