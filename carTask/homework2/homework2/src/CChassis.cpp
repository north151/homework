#include "../include/CChassis.h"

void CChassis::print()
{
    cout << "<底盘信息>" << endl;
    cout << "编号: " << this->id << endl;
    cout << "型号: " << this->type << endl;
    cout << "轴距: " << this->wheelbase << endl;
    cout << "轮距: " << this->wheeltrack << endl;
    cout << "最小离地间隙: " << this->minGroundClearance << endl;
    cout << "最小转弯半径: " << this->minTurningRadius << endl;
    cout << "驱动模式: " << this->drivingForm << endl;
    cout << "最大行程: " << this->maxStroke << endl;
    this->tyre.print();
    return;
}

void CChassis::save(string _saveFileName)
{
    ofstream fw;
    fw.open(_saveFileName, ios::app);
    fw << "<底盘信息>" << endl;
    fw << "编号: " << this->id << endl;
    fw << "型号: " << this->type << endl;
    fw << "轴距: " << this->wheelbase << "mm" << endl;
    fw << "轮距: " << this->wheeltrack << "mm" << endl;
    fw << "最小离地间隙: " << this->minGroundClearance << "mm" << endl;
    fw << "最小转弯半径: " << this->minTurningRadius << "m" << endl;
    fw << "驱动模式: " << this->drivingForm << endl;
    fw << "最大行程: " << this->maxStroke << "KM" << endl;
    fw.close();
    this->tyre.save(_saveFileName);
    return;
}

void CChassis::setId(string _id)
{
    this->id = _id;
    return;
}

void CChassis::setType(string _type)
{
    this->type = _type;
    return;
}

void CChassis::setWheelBase(int _wheelbase)
{
    this->wheelbase = _wheelbase;
    return;
}

void CChassis::setWheelTrack(int _wheeltrack)
{
    this->wheeltrack = _wheeltrack;
    return;
}

void CChassis::setMinGroundClearance(int _minGroundClearance)
{
    this->minGroundClearance = _minGroundClearance;
    return;
}

void CChassis::setMinTurningRadius(int _minTurningRadius)
{
    this->minTurningRadius = _minTurningRadius;
    return;
}

void CChassis::setDrivingForm(string _drivingForm)
{
    this->drivingForm = _drivingForm;
    return;
}

void CChassis::setMaxStroke(int _maxStroke)
{
    this->maxStroke = _maxStroke;
    return;
}

void CChassis::setTyre(CTyre _tyre)
{
    this->tyre = _tyre;
    return;
}
