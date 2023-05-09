from my_first_package_msgs.srv import MultiSpawn
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import Spawn


import rclpy as rp
import numpy as np

class MultiSpawning(Node):

    def __init__(self):
        # 노드 초기화 
        super().__init__('multi_spawn')
        # 서버 온 
        self.server = self.create_service(MultiSpawn, 'multi_spawn', self.callback_service)
        # 클라 sub 
        self.teleport = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        self.spawn = self.create_client(Spawn, '/spawn')

        # 터틀 텔포 서비스 메시지 
        self.req_teleport = TeleportAbsolute.Request()
        # 터틀 소환 서비스 메시지 
        self.req_spawn = Spawn.Request()
        self.center_x = 5.54
        self.center_y = 5.54

    def calc_position(self, n, r):
        gap_theta = 2*np.pi / n
        theta = [gap_theta*n for n in range(n)]
        x = [r*np.cos(th) for th in theta]
        y = [r*np.sin(th) for th in theta]

        return x, y, theta
        

    # 서비스 클라 호출 
    def callback_service(self, request, response):
        x, y, theta = self.calc_position(request.num, 3)

        for n in range(len(theta)):
            self.req_spawn.x = x[n] + self.center_x
            self.req_spawn.y = y[n] + self.center_y
            self.req_spawn.theta = theta[n]
            self.spawn.call_async(self.req_spawn)
        response.x = x
        response.y = y
        response.theta = theta
        
        return response
    
def main(args = None):
    rp.init(args=args)
    multi_spawn = MultiSpawning()
    rp.spin(multi_spawn)
    rp.shutdown()

if __name__ == '__main__':
    main()
