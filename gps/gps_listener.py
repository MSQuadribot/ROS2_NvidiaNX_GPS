import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class GPSSubscriber(Node):
    '''
    Create a node providing a subscriber.
    It will get the gps data from the gps_data topic.
    The data are then displayed for the user in a terminal.
    '''

    def __init__(self):
        super().__init__('GPS_subscriber')
        self.subscription = self.create_subscription(
            String,
            'gps_data',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    '''
    This function is called when the user launch the executable file.
    Ros2 will directly start the program here, according to the setup file.
    '''

    rclpy.init(args=args)

    GPS_subscriber = GPSSubscriber()

    rclpy.spin(GPS_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    GPS_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()