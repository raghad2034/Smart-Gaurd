import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RobotControllerSubscriber(Node):
    def __init__(self):
        super().__init__('robot_controller_subscriber')
        self.subscription = self.create_subscription(
            String,
            'fire_alert',
            self.listener_callback,
            10)
        self.subscription   

    def listener_callback(self, msg):
        self.get_logger().info('Received Alert: "%s" - Moving Smart Guard towards target...' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = RobotControllerSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
