

#include "../include/CAgxKit.h"

void CAgxKit::print()
{
    cout << "<AGX套件信息>" << endl;
    cout << "型号: " << this->type << endl;
    cout << "AI: " << this->ai << "TOPS" << endl;
    cout << "CUDA核心: " << this->cudaCore << endl;
    cout << "Tensor CORE: " << this->tensorCore << endl;
    cout << "显存: " << this->videoMemory << "G" << endl;
    cout << "存储: " << this->externalStorage << "G" << endl;
    return;
}

void CAgxKit::save(string _saveFileName)
{
    ofstream fw;
    fw.open(_saveFileName, ios::app);
    fw << "<AGX套件信息>" << endl;
    fw << "型号: " << this->type << endl;
    fw << "AI: " << this->ai << "TOPS" << endl;
    fw << "CUDA核心: " << this->cudaCore << endl;
    fw << "Tensor CORE: " << this->tensorCore << endl;
    fw << "显存: " << this->videoMemory << "G" << endl;
    fw << "存储: " << this->externalStorage << "G" << endl;
    fw.close();
    return;
}

/////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////
void CAgxKit::setType(string _type)
{
    this->type = _type;
    return;
}

void CAgxKit::setAi(int _ai)
{
    this->ai = _ai;
    return;
}

void CAgxKit::setCudaCore(int _cudaCore)
{
    this->cudaCore = _cudaCore;
    return;
}

void CAgxKit::setVideoMemory(int _videoMemory)
{
    this->videoMemory = _videoMemory;
    return;
}

void CAgxKit::setExternalStorage(int _externalStorage)
{
    this->externalStorage = _externalStorage;
    return;
}
