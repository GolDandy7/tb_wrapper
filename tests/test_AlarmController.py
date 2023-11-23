import pytest
from unittest.mock import MagicMock
from src.AlarmController import AlarmController

@pytest.fixture
def alarm_controller():
    tb_url = 'http://217.76.51.6:9090'
    userfile = 'user.secrets'
    passwordfile = 'pass.secrets'
    return AlarmController(tb_url, userfile, passwordfile)

def test_build_alarm(alarm_controller):
    tenant_obj_id = "tenant_id"
    alarm_name = "alarm_name"
    alarm_type = "alarm_type"
    entity_orginator = "entity_orginator"
    customer_obj_id = "customer_obj_id"
    severity_alarm = "INDETERMINATE"
    alarm_status = "ACTIVE_ACK"
    ack = True
    clear = False

    expected_alarm = {
        "tenant_id": tenant_obj_id,
        "name": alarm_name,
        "type": alarm_type,
        "originator": entity_orginator,
        "customer_id": customer_obj_id,
        "severity": severity_alarm,
        "status": alarm_status,
        "acknowledged": ack,
        "cleared": clear
    }
    
    assert alarm_controller.build_alarm(tenant_obj_id, alarm_name, alarm_type, entity_orginator, 
                            customer_obj_id, severity_alarm, alarm_status, ack, clear) is not None

def test_save_alarm(alarm_controller):
    alarm_controller.tb_client.save_alarm = MagicMock(return_value="mocked_result")

    alarm = {"mock": "alarm"}

    result = alarm_controller.save_alarm(alarm)

    assert result is not None 