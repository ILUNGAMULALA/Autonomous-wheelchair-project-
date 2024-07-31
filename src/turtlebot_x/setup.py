
from setuptools import find_packages, setup
import os
from glob import glob
from setuptools import setup
from setuptools import find_packages
package_name = 'turtlebot_x'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name), glob('urdf/*')),
        (os.path.join('share', package_name), glob('sdf/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='josue',
    maintainer_email='josue@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "video_subscriber = turtlebot_x.video_recorder_node:main",
            "driving_node = turtlebot_x.driving_node:main",
        ],
    },
)
