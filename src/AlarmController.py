from MainController import MainController
from tb_rest_client.rest_client_ce import *
from handle_exception import *

@handle_tb_wrapper_exception
class AlarmController(MainController):
    tb_client = None
    
    def __init__(self, tb_url, userfile, passwordfile):
        super().__init__(tb_url, userfile, passwordfile)

    def build_alarm(self, tenant_obj_id, alarm_name, alarm_type, entity_orginator, customer_obj_id, severity_alarm, alarm_status, ack, clear):    

        return Alarm(tenant_id=tenant_obj_id,
                    name=alarm_name,
                    type=alarm_type,
                    originator=entity_orginator,
                    customer_id=customer_obj_id,
                    severity=severity_alarm,
                    status=alarm_status,
                    acknowledged=ack,
                    cleared=clear)

    def save_alarm(self, alarm):
        return self.tb_client.save_alarm(alarm)