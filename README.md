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

5. 액션 서버에서 feedback 메시지를 보고싶을 경우 action send_goal --feedback 

```bash

ros2 action send_goal --feedback /dist_turtle my_first_package_msgs/action/DistTurtle "linear_x: 0.1
angular_z: 0.1
dist: 2.0" 

```

6. DDS 버그 :: 연결이 안됨  :: 포싱 문제 (gost posing)

ros 프로세스 보기, 죽이는건 구글링 

```bash
ps -ef | grep ros
```

7. param 적용 

```bash
ros2 param load /turtlesim ./turtlesim.yaml
```

8. 코파일럿 사용해보자 - vscode extensions
9. ros2 launch 구성 
    1. launch 파일 생성 
    2. [setup.py](http://setup.py) 수정 

```bash
ros2 launch my_first_pkg turtlesim_and_teleop.launch.py
```