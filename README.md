# ros2_study
### TIL
1. 파이썬 빌드론 커스텀 msg를 만들 수 없기 때문에 msg 정의만 된 cmake 빌드 시스템을 사용한다.

```bash

# 기존 msg type만 사용하는 경우 pkg 생성 
ros2 pkg create --build-type ament_python --node-name my_first_node my_first_package 
# 사용자 정의 msg type을 생성해 사용하는 경우 
ros2 pkg create --build-type ament_cmake my_first_package_msgs 

``` 
2. 특정 pkg만 빌드하고 싶을 경우 

```bash
colcon build --packages-select my_first_package_msgs

``` 

3. msg, srv type을 확인하고 싶을 경우 

```bash
ros2 interface show my_first_package_msgs/srv/MultiSpawn

``` 

4. 한 노드에서 여러 콜백 함수가 작동될 경우 하나의 콜백 함수만 실행 되기에 이를 해결하기 위해 멀티 스레드를 사용한다. 
