#pragma once

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// AGX套件
typedef struct _agxKit
{
    string type = "AGX Xavier"; // 型号
    int ai = 32;                // AI
    int cudaCore = 512;         // CUDA核心数
    int tensorCore = 64;        // TensorCore
    int videoMemory = 32;       // 显存
    int externalStorage = 32;   // 外存

    void save(string _saveFileName)
    {
        ofstream fw;
        fw.open(_saveFileName, ios::app);
        fw << "<AGX套件信息>" << endl;
        fw << "型号: " << type << endl;
        fw << "AI: " << ai << "TOPS" << endl;
        fw << "CUDA核心: " << cudaCore << endl;
        fw << "Tensor CORE: " << tensorCore << endl;
        fw << "显存: " << videoMemory << "G" << endl;
        fw << "存储: " << externalStorage << "G" << endl;
        fw.close();
        return;
    }

} AGX_KIT;