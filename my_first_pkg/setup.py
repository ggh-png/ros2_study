from setuptools import setup

package_name = 'my_first_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 런치파일 추가 
        ('share/' + package_name + '/launch', ['launch/turtlesim_and_teleop.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ggh',
    maintainer_email='0380089@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_first_node = my_first_pkg.my_first_node:main',
            'sub = my_first_pkg.sub:main',
            'pub = my_first_pkg.pub:main',
            'cmd_pose = my_first_pkg.cmd_pose:main',
            'my_service_server = my_first_pkg.my_service_server:main',
            'dist_turtle_action_server = my_first_pkg.dist_turtle_action_server:main',
            'my_multi_thread = my_first_pkg.my_multi_thread:main'
        ],
    },
)
