from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                namespace='turtlesim', package='turtlesim',
                executable='turtlesim_node', name='sim'),
            Node(
                namespace= 'pub_cmd_vel', package='my_first_pkg',
                executable='pub', output='screen'),
        ]
    )
        