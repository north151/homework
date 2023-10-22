#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

#include "student.h"
#include "tyre.h"
#include "chassis.h"
#include "agxKit.h"
#include "binocularCamera.h"
#include "multiLineLidar.h"
#include "nineAxisGyroscope.h"
#include "lcd.h"
#include "batteryModule.h"
#include "intelligentCar.h"

int main()
{
    int nums;
    cout << "请输入学生人数： ";
    cin >> nums;

    STUDENT students[nums];
    INTELLIGENT_CAR intelligentCars[nums];

    for (int i = 0; i < nums; ++i)
    {
        cout << "请输入第" << i + 1 << "位学生学号: ";
        cin >> students[i].studentNumber;
        cout << "请输入第" << i + 1 << "位学生姓名: ";
        cin >> students[i].studentName;
    }
    system("clear");

    for (int i = 0; i < nums; i++)
    {
        cout << "<开始构建第" << i + 1 << " 辆小车>" << endl;
        cout << "请输入小车编号: ";
        cin >> intelligentCars[i].id;
        cout << "请输入底盘编号: ";
        cin >> intelligentCars[i].chassis.id;
        intelligentCars[i].isAllocated = true;
        intelligentCars[i].save();
    }
    system("clear");

    cout << "小车分配完成" << endl;
    cout << "按y查看小车信息,按n退出: ";
    char ch;
    cin >> ch;
    if (ch == 'y')
    {
        intelligentCars[0].print();
    }
    else
    {
        return 0;
    }

    for (int i = 0; true;)
    {
        cout << "按n查看下一辆小车,按p查看上一辆小车，否则退出: ";
        cin >> ch;
        switch (ch)
        {
        case 'n':
            if (i == nums - 1)
            {
                cout << "无下一辆小车,请重新输入：" << endl;
                continue;
            }
            else
            {
                ++i;
            }
            break;
        case 'p':
            if (i == 0)
            {
                cout << "无上一辆小车,请重新输入：" << endl;
                continue;
            }
            else
            {
                --i;
            }
            break;
        case 'q':
            cout << "查看小车信息结束" << endl;
            return 0;
        }
        system("clear");
        intelligentCars[i].print();
    }

    return 0;
}
