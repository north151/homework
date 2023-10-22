#include "../include/CBinocularCamera.h"

void CBinocularCamera::print()
{
    cout << "<双目摄像头信息>" << endl;
    cout << "型号: " << this->type << endl;
    cout << "摄像头: " << this->camera << endl;
    cout << "RGB帧分辨率: " << this->rgbFrameResolution << endl;
    cout << "RGB帧率: " << this->rgbFrameRate << endl;
    cout << "FOV: " << this->fov << endl;
    cout << "深度帧率: " << this->depthFrameRate << endl;
    return;
}

void CBinocularCamera::save(string _saveFileName)
{
    ofstream fw;
    fw.open(_saveFileName, ios::app);
    fw << "<双目摄像头信息>" << endl;
    fw << "型号: " << this->type << endl;
    fw << "摄像头: " << this->camera << endl;
    fw << "RGB帧分辨率: " << this->rgbFrameResolution << endl;
    fw << "RGB帧率: " << this->rgbFrameRate << endl;
    fw << "FOV: " << this->fov << endl;
    fw << "深度帧率: " << this->depthFrameRate << endl;
    fw.close();
    return;
}

void CBinocularCamera::setType(string _type)
{
    this->type = _type;
    return;
}

void CBinocularCamera::setCamera(string _camera)
{
    this->camera = _camera;
    return;
}

void CBinocularCamera::setRGBFrameResolution(string _rgbFrameResolution)
{
    this->rgbFrameResolution = _rgbFrameResolution;
    return;
}

void CBinocularCamera::setRGBFrameRate(int _rgbFrameRate)
{
    this->rgbFrameRate = _rgbFrameRate;
    return;
}

void CBinocularCamera::setFOV(int _fov)
{
    this->fov = _fov;
    return;
}

void CBinocularCamera::setDepthFrameRate(int _depthFrameRate)
{
    this->depthFrameRate = _depthFrameRate;
    return;
}
