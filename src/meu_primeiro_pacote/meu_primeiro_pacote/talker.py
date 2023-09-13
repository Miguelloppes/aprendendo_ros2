import rclpy
from rclpy.node import Node

from std_msgs.msg import String 

from rclpy.logging import LoggingSeverity
# Cria o nó do ROS como uma clase do python
class MeuNo(Node):

    # Contrutor do nó
    def __init__(self):
        # Aqui é definido o nome do nó
        super().__init__('no_com_classe')

        self.publisher = self.create_publisher(String, 'meu_topico', 10)

    # Aqui o seu nó está executando no ROS
    def run(self):
        self.get_logger().info('Criando primeiro publisher!')
        self.create_timer(1, self.talker_callback)

        # Executa uma iteração do loop de processamento de mensagens.
        rclpy.spin(self)

    def talker_callback(self):
        msg = String()
        msg.data = 'Mensage :D'
        self.publisher.publish(msg)

    # Destrutor do nó
    def __del__(self):
        self.get_logger().info('Finalizando o nó! Tchau, tchau...')


# Função principal
def main(args=None):
    rclpy.init(args=args)
    node = MeuNo()
    try:
        node.run()
        node.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass
    
if __name__ == '__main__':
    main()    




