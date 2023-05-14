import rclpy as rp 
from rclpy.action import ActionServer
from rclpy.node import Node
# 멀티 스레드
from rclpy.executors import MultiThreadedExecutor

# cmd_vel 토픽 pub & turtlesim pose sub 
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

from my_first_package_msgs.action import DistTurtle
# turtlesim vel 
from my_first_pkg.sub import TurtleSub

import time
import math


# turtlesim vel값 받는 sub 상속 
class TurtleSub_Action(TurtleSub):
    # ac_sercer : 액션 서버 지정 
    def __init__(self, ac_server):
        super().__init__()
        self.ac_server = ac_server
    # 오버라이딩 새롭게 초기화 msg : turtle pose 
    def callback(self, msg):
        self.ac_server.current_pose = msg

# 사용자가 지정한 거리만큼 이동 
class DistTurtleServer(Node):
    def __init__(self):
        super().__init__('dist_turtle_action_server')
        # 총 이동거리 
        self.total_dist = 0
        self.is_first_time = True
        # 현 turtlesim 좌표
        self.current_pose = Pose()
        # 과거 turtlesim 좌표 
        self.previous_pose = Pose()
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.action_server = ActionServer(self, DistTurtle, 'dist_turtle', self.execute_callback)
    # 이동거리 계산 
    def calc_diff_pose(self):
        # 첫 계산은 포함하지 않는다.
        if self.is_first_time:
            self.previous_pose.x = self.current_pose.x
            self.previous_pose.y = self.current_pose.y
            self.is_first_time = False
        # turtlesim 이동거리 공식 
        diff_dist = math.sqrt((self.current_pose.x - self.previous_pose.x)**2 +\
                              (self.current_pose.y - self.previous_pose.y)**2)
        
        self.previous_pose = self.current_pose
        return diff_dist

    def execute_callback(self, goal_handle):
        # 액션 피드백 메시지 사용 
        feedback_msg = DistTurtle.Feedback()
        # goal_handle : 지정 속도 
        msg = Twist()
        msg.linear.x = goal_handle.request.linear_x
        msg.angular.z = goal_handle.request.angular_z

        while True:
            self.total_dist += self.calc_diff_pose()
            feedback_msg.remained_dist = goal_handle.request.dist - self.total_dist
            # 순간적인 이동거리 pub
            goal_handle.publish_feedback(feedback_msg)
            # 총 이동거리 pub
            self.publisher.publish(msg)
            time.sleep(0.01)
            # 오차 범위가 0.2 미만이면 종료 
            if feedback_msg.remained_dist < 0.2:
                break
        
        goal_handle.succeed()
        result = DistTurtle.Result()
        result.pos_x = self.current_pose.x
        result.pos_y = self.current_pose.y
        result.pos_theta = self.current_pose.theta
        result.result_dist = self.total_dist

        self.total_dist = 0
        self.is_first_time = True

        return result

def main(args=None):
    rp.init(args=args)

    executor = MultiThreadedExecutor()

    ac = DistTurtleServer()
    # turtlesim pose를 토픽으로 받은 후 액션 서버에 전달
    sub = TurtleSub_Action(ac_server = ac)

    executor.add_node(sub)
    executor.add_node(ac)

    try:
        executor.spin()
    finally:
        executor.shutdown()
        sub.destroy_node()
        ac.destroy_node()
        rp.shutdown()

if __name__ == '__main__':
    main()