import rclpy as rp
from rclpy.node import Node

from geometry_msgs.msg import Twist

class TurtlePub(Node):
    def __init__(self):
        super().__init__('turtle_pub')
        self.publisher = self.create_publisher(Twist, '/turtlesim/turtle1/cmd_vel', 10)
        period = 0.5
        self.timer = self.create_timer(period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 2.0
        self.publisher.publish(msg)


def main(args=None):
    rp.init(args = args)
    turtle_pub = TurtlePub()
    rp.spin(turtle_pub)

    turtle_pub.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()