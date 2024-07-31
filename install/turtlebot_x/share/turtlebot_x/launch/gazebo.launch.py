from launch.actions import ExecuteProcess
from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    ld = LaunchDescription()

    # Définir le chemin absolu du fichier "chairbot.world"
    model_path = os.path.expanduser('~/chair_ws/src/turtlebot_x/models/chairbot.world')

    # Démarrer Gazebo avec le monde "chairbot.world"
    start_gazebo_cmd = ExecuteProcess(
        cmd=['gzserver', '--verbose', '-s', 'libgazebo_ros_factory.so', model_path],
        output='screen'
    )
    ld.add_action(start_gazebo_cmd)

    # Lancer le nœud pour contrôler le modèle
    driving_node_cmd = Node(
        package='turtlebot_x',
        executable='driving_node.py',
        output='screen'
    )
    ld.add_action(driving_node_cmd)

    return ld
