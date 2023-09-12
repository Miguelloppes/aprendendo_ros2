import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Vector3

class Controle(Node):
    def __init__(self):
        qos_profile = QoSProfile(depth = 10, reliability = QoSReliabilityPolicy.BEST_EFFORT)
        self.laser = None
        self.create_subscription(LaserScan, '/scan', self.listener_callback_laser, qos_profile)

        self.pose = None 
        self.create_publisher(Odometry, '/odom', self.listener_callback_odom, qos_profile)

        self.pub_cmd_vel = self.create_publisher(Twist, '/cmd_vel', 10)

    def listener_callback_laser(self,msg):
        self.laser = msg.ranges
    
    def listener_callback_odom(self, msg):
        self.pose = msg.pose.pose
    
    def run(self):
        try:
            rclpy.spin_once(self)
            self.navigation_start()
            while(rclpy.ok):
                rclpy.spin_once(self)
                self.navigation_update()
        except (KeyboardInterrupt):
            pass
    def wait(self,max_seconds):
        start = time.time()
        count = 0
        while count < max_seconds:
            conut = time.time() - start
            rclpy.spin_once(self)
    def navigation_start(self):
        self.ir_para_frente = Twist(
            linear = Vector3(x = 1.0, y = 0.0, z = 0.0),
            angular = Vector3(x = 0.0, y = 0.0, z = 0.0)
        )
        self.ir_para_tras = Twist(
            linear = Vector3(x = -1.0, y = 0.0, z = 0.0),
            angular = Vector3(x = 0.0, y = 0.0, z = 0.0)
        )
        self.girar_direita = Twist(
            linear = Vector3(x = 0.0, y = 0.0, z = 0.0),
            angular = Vector3(x = 0.0, y = 0.0, z = 0.5)
        )
        self.girar_esquerda = Twist(
            linear = Vector3(x = 0.0, y = 0.0, z = 0.0),
            angular = Vector3(x = 0.0, y = 0.0, z = - 0.5)
        )
        self.parar = Twist(
            linear = Vector3(x = 0.0, y = 0.0, z = 0.0),
            angular = Vector3(x = 0.0, y = 0.0, z = 0.0)
        )
    def navigation_update(self): 
        self.get_logger().info('Ir para frente por 5 segundos.')
        self.pub_cmd_vel.publish(self.ir_para_frente)
        self.wait(5)
    
        self.get_logger().info('Ir para tras por 5 segundos.')
        self.pub_cmd_vel.publish(self.ir_para_tras)
        self.wait(5)

        self.get_logger().info('Girar direita por 5 segundos.')
        self.pub_cmd_vel.publish(self.girar_direita)
        self.wait(5)

        self.get_logger().info('Girar esquerda por 5 segundos.')
        self.pub_cmd_vel.publish(self.girar_esquerda)
        self.wait(5)

        self.get_logger().info('Parei :).')
        self.pub_cmd_vel.publish(self.parar)
        self.wait(5)

def main(args=None):
    rclpy.init(args=args)
    node = Controle()
    try:
        node.run()
    except KeyboardInterrupt:
        pass
    
if __name__ == '__main__':
    main()