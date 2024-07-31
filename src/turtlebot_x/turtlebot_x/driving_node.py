from geometry_msgs.msg import Twist
from rclpy.node import Node 
from cv_bridge import CvBridge 
import rclpy 
from std_msgs.msg import Float64MultiArray
from gazebo_msgs.srv import SpawnEntity
from gazebo_msgs.srv import DeleteEntity
from gazebo_msgs.msg import ModelState

class TurtleDriver(Node):
    def __init__(self):
        super().__init__('driving_node')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 40)
        timer_period = 0.5
        # Création d'un groupe de rappels
        self.callback_group = rclpy.callback_groups.ReentrantCallbackGroup()
        self.timer = self.create_timer(1.0, self.send_cmd_vel, callback_group=self.callback_group)
        self.velocity = Twist()
        self.nodeName = self.get_name()
        self.get_logger().info("{0} started".format(self.nodeName))

    def send_cmd_vel(self):
        self.velocity.linear.x = 0.2       
        self.velocity.angular.z = 0.0
        self.publisher.publish(self.velocity)

def main(args=None):
    rclpy.init(args=args)
    cmd_vel_publisher = TurtleDriver()
    rclpy.spin(cmd_vel_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
