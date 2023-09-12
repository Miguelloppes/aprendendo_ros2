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

        self.subscription = self.create_subscription(String, 'meu_topico', self.listener_callback,10)
        # # Define o nível do logger
        # logger = self.get_logger()
        # logger.set_level(LoggingSeverity.INFO)

    # Aqui o seu nó está executando no ROS
    def run(self):
        self.get_logger().info('Criando Subscriber!')


        # Executa uma iteração do loop de processamento de mensagens.
        rclpy.spin(self)

    def listener_callback(self,msg):
        self.get_logger().info("Mensagem recebida: %s" % msg.data)
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




