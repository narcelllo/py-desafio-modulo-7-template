'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''

class TaskHandler:
    
    def conect_api(): #ok
        pass

    def create_task(): #ok
        pass

    def update_task(): #ok
        pass

    def remove_task():#ok
        pass

    def send_notification(): #oK
        pass

    def generate_report(): #ok
        pass

    def send_report(): #ok
        pass
