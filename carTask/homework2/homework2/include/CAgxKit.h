#pragma once

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class CAgxKit
{
private:
    string type = "AGX Xavier"; // 型号
    int ai = 32;                // AI
    int cudaCore = 512;         // CUDA核心数
    int tensorCore = 64;        // TensorCore
    int videoMemory = 32;       // 显存
    int externalStorage = 32;   // 外存

public:
    CAgxKit(){};
    ~CAgxKit(){};
    void print();
    void save(string _saveFileName);

    void setType(string _type);
    void setAi(int _ai);
    void setCudaCore(int _cudaCore);
    void setVideoMemory(int _videoMemory);
    void setExternalStorage(int _externalStorage);
};