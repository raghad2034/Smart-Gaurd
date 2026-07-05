import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class FireSensorPublisher(Node):
    def __init__(self):
        super().__init__('fire_sensor_publisher')
        self.publisher_ = self.create_publisher(String, 'fire_alert', 10)
        timer_period = 2.0
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Fire Detected in Room A!' 
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing Alert: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = FireSensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
