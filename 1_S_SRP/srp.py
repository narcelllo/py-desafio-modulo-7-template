from typing import Dict

class ConectAPI:
    def conect_api(self) -> Dict:
        return {"API": "example", "data": {}}

class TaskHandler:
    def handlerTask(self, api_ata: ConectAPI) -> None:
        pass

    def __create_task(self,  apiData: Dict) -> None:
        pass

    def __update_task(self, task_id: int, apiData: Dict ) -> None:
        pass

    def __remove_task(self,task_id: int) -> None:
        pass

class RiseError():
    pass

    def generate_report(self, error_response: Dict) -> None:
        pass

    def send_report(self, error_response: str) -> None:
        pass

class Notificator:
    pass

    def send_notification(self, notification: str) -> None:
        pass