cmake_minimum_required (VERSION 2.8)   
project(homework2)          

# 设置c++编译器
set(CMAKE_CXX_COMPILER "g++")    
# 添加头文件路径
include_directories(${PROJECT_SOURCE_DIR}/include)    
# 将源文件列表写在变量SrcFiles中     
aux_source_directory(./src SrcFiles)                      
# 可执行文件输出路径            
set(EXECUTABLE_OUTPUT_PATH  ${PROJECT_SOURCE_DIR}/out)          
# 可执行文件的名称 
add_executable(main ${SrcFiles})                    
