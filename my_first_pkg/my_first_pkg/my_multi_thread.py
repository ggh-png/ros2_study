import rclpy as rp
from rclpy.node import Node
# 멀티 스레드
from rclpy.executors import MultiThreadedExecutor

# 터틀심 속도 명령 pub, 현 속도 값 sub
from my_first_pkg.pub import TurtlePub
from my_first_pkg.sub import TurtleSub



def main(args=None):
    rp.init()

    sub = TurtleSub()
    pub = TurtlePub()

    # 멀티 스레딩 Class 
    executor = MultiThreadedExecutor()
    executor.add_node(sub)
    executor.add_node(pub)

    try:
        executor.spin()

    finally:
        executor.shutdown()
        sub.destroy_node()
        pub.destroy_node()
        rp.shutdown()

if __name__ == '__main__':
    main()
