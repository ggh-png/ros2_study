# ros2_study
### TIL
1. 파이썬 빌드론 커스텀 msg를 만들 수 없기 때문에 msg 정의만 된 cmake 빌드 시스템을 사용한다.

```bash

# 기존 msg type만 사용하는 경우 pkg 생성 
ros2 pkg create --build-type ament_python --node-name my_first_node my_first_package 
# 사용자 정의 msg type을 생성해 사용하는 경우 
ros2 pkg create --build-type ament_cmake my_first_package_msgs 

```