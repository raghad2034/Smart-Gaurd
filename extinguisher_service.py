import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class ExtinguisherService(Node):
    def __init__(self):
        super().__init__('extinguisher_service')
        self.srv = self.create_service(SetBool, 'activate_extinguisher', self.extinguish_callback)

    def extinguish_callback(self, request, response):
        if request.data == True:
            response.success = True
            response.message = 'Extinguisher Activated! Fire is being put out.'
            self.get_logger().info('Action: Activating Water Pump via Arduino...')
        else:
            response.success = False
            response.message = 'Extinguisher OFF. Area is safe.'
            self.get_logger().info('Action: Stopping Water Pump.')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ExtinguisherService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
