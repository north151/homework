#include "../include/CNineAxisGyroscope.h"

void CNineAxisGyroscope::print()
{
    cout << "<9轴陀螺仪信息>" << endl;
    cout << "型号: " << this->type << endl;
    cout << "厂家: " << this->manufactor << endl;
}

void CNineAxisGyroscope::save(string _saveFileName)
{
    ofstream fw;
    fw.open(_saveFileName, ios::app);
    fw << "<9轴陀螺仪信息>" << endl;
    fw << "型号: " << this->type << endl;
    fw << "厂家: " << this->manufactor << endl;
    fw.close();
    return;
}

void CNineAxisGyroscope::setType(string _type)
{
    this->type = _type;
    return;
}

void CNineAxisGyroscope::setManufactor(string _manufactor)
{
    this->manufactor = _manufactor;
    return;
}
