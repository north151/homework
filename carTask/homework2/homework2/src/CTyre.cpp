#include "../include/CTyre.h"

void CTyre::print()
{
    cout << "轮胎信息: " << endl;
    cout << "轮胎数量: " << this->amount << "个" << endl;
    cout << "轮胎型号: " << this->type << endl;
    cout << "轮胎尺寸: " << this->size << "mm" << endl;
    return;
}
void CTyre::save(string _saveFileName)
{
    ofstream fw;
    fw.open(_saveFileName, ios::app);
    fw << "轮胎信息:" << endl;
    fw << "轮胎数量: " << this->amount << "个" << endl;
    fw << "轮胎型号: " << this->type << endl;
    fw << "轮胎尺寸: " << this->size << "mm" << endl;
    fw.close();
    return;
}

void CTyre::setType(string _type)
{
    this->type = _type;
    return;
}

void CTyre::setSize(int _size)
{
    this->size = _size;
    return;
}

void CTyre::setAmount(int _amount)
{
    this->amount = _amount;
    return;
}
