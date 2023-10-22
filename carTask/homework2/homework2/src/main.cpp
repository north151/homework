#include <string>
#include <iostream>
#include <fstream>

using namespace std;

#include "../include/CChassis.h"
#include "../include/CTyre.h"
#include "../include/CAgxKit.h"
#include "../include/CBinocularCamera.h"
#include "../include/CMultiLineLidar.h"
#include "../include/CNineAxisGyroscope.h"
#include "../include/CLcd.h"
#include "../include/CBatteryModule.h"
#include "../include/CStudent.h"
#include "../include/CIntelligentCar.h"

int main()
{
    int nums;
    string carId;
    string chassisId;
    string studentNumber;
    string studentName;

    CTyre tyre;                           // 轮胎
    CChassis chassis;                     // 底盘
    CAgxKit agxKit;                       // Agx套件
    CBinocularCamera binocularCamera;     // 双目摄像头
    CMultiLineLidar multiLineLidar;       // 多线激光雷达
    CNineAxisGyroscope nineAxisGyroscope; // 9轴陀螺仪
    CLcd lcd;                             // 液晶显示屏
    CBatteryModule batteryModule;         // 电池

    cout << "请输入学生人数： ";
    cin >> nums;

    CStudent students[nums];
    CIntelligentCar *intelligentCars[nums];

    for (int i = 0; i < nums; ++i)
    {
        cout << "请输入第" << i + 1 << "位学生学号: ";
        cin >> studentNumber;
        students[i].setStudentNumber(studentNumber);
        cout << "请输入第" << i + 1 << "位学生姓名: ";
        cin >> studentName;
        students[i].setStudentName(studentName);
    }
    system("clear");

    for (int i = 0; i < nums; i++)
    {
        cout << "<开始构建第" << i + 1 << " 辆小车>" << endl;
        cout << "请输入小车编号: ";
        cin >> carId;
        cout << "请输入底盘编号: ";
        cin >> chassisId;
        chassis.setId(chassisId);
        chassis.setTyre(tyre);
        intelligentCars[i] = new CIntelligentCar(carId, students[i], chassis, agxKit, binocularCamera, multiLineLidar, nineAxisGyroscope, lcd, batteryModule);
        intelligentCars[i]->setIsAllocated(true);
    }
    system("clear");

    cout << "小车分配完成" << endl;
    cout << "按y查看小车信息,按n退出: ";
    char ch;
    cin >> ch;
    if (ch == 'y')
    {
        intelligentCars[0]->print();
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
        intelligentCars[i]->print();
    }

    return 0;
}
