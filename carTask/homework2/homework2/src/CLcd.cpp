#include "../include/CLcd.h"

void CLcd::print()
{
    cout << "<液晶显示器信息>" << endl;
    cout << "尺寸: " << this->size << endl;
    cout << "型号: " << this->size << endl;
    return;
}

void CLcd::save(string _saveFileName)
{
    ofstream fw;
    fw.open(_saveFileName, ios::app);
    fw << "<液晶显示器信息>" << endl;
    fw << "尺寸: " << this->size << endl;
    fw << "型号: " << this->size << endl;
    fw.close();
    return;
}

void CLcd::setType(string _type)
{
    this->type = _type;
    return;
}

void CLcd::setSize(float _size)
{
    this->size = _size;
    return;
}
