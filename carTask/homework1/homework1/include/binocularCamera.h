#pragma once

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// 双目摄像头
typedef struct _binocularCamera
{
    string type = "RealSense D435i";         // 型号   (RealSense D435i)
    string camera = "D430";                  // 摄像头   (D430)
    string rgbFrameResolution = "1920*1080"; // RGB帧分辨率   (1920*1080)
    int rgbFrameRate = 30;                   // RGB帧率   (30)
    int fov = 30;                            // FOV   (87*58)
    int depthFrameRate = 90;                 // 深度帧率   (90)

    void save(string _saveFileName)
    {
        ofstream fw;
        fw.open(_saveFileName, ios::app);
        fw << "<双目摄像头信息>" << endl;
        fw << "型号: " << type << endl;
        fw << "摄像头: " << camera << endl;
        fw << "RGB帧分辨率: " << rgbFrameResolution << endl;
        fw << "RGB帧率: " << rgbFrameRate << endl;
        fw << "FOV: " << fov << endl;
        fw << "深度帧率: " << depthFrameRate << endl;
        fw.close();
        return;
    }

} BINOCULAR_CAMERA;