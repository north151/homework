#pragma once

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class CBinocularCamera
{
private:
    string type = "RealSense D435i";         // 型号   (RealSense D435i)
    string camera = "D430";                  // 摄像头   (D430)
    string rgbFrameResolution = "1920*1080"; // RGB帧分辨率   (1920*1080)
    int rgbFrameRate = 30;                   // RGB帧率   (30)
    int fov = 30;                            // FOV   (87*58)
    int depthFrameRate = 90;                 // 深度帧率   (90)

public:
    CBinocularCamera(){};
    ~CBinocularCamera(){};
    void print();
    void save(string _saveFileName);

    void setType(string __type);
    void setCamera(string _camera);
    void setRGBFrameResolution(string _rgbFrameResolution);
    void setRGBFrameRate(int _rgbFrameRate);
    void setFOV(int _fov);
    void setDepthFrameRate(int _depthFrameRate);
};
