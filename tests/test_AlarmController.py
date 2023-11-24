import pytest
from unittest.mock import MagicMock
from tb_wrapper.AlarmController import AlarmController

@pytest.fixture
def alarm_controller():
    tb_url = 'http://217.76.51.6:9090'
    userfile = 'user.secrets'
    passwordfile = 'pass.secrets'
    return AlarmController(tb_url, userfile, passwordfile)

def test_build_alarm(alarm_controller):

    tenant_obj = {'entity_type': 'TENANT','id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'}
    customer_obj = {'entity_type': 'CUSTOMER','id': '13814000-1dd2-11b2-8080-808080808080'}
    entity_orginator = {'entity_type': 'ASSET', 'id': '774f8440-8946-11ee-9593-fbf738de8bd6'}
    alarm_name = "alarm_name"
    alarm_type = "alarm_type"
    severity_alarm = "INDETERMINATE"
    alarm_status = "ACTIVE_ACK"
    ack = True
    clear = False

    result = alarm_controller.build_alarm(tenant_obj, alarm_name, alarm_type, entity_orginator, 
                            customer_obj, severity_alarm, alarm_status, ack, clear)
    
    assert result is not None
    assert result.tenant_id == tenant_obj
    assert result.customer_id == customer_obj
    assert result.originator == entity_orginator
    assert result.name == alarm_name
    assert result.status == alarm_status
    assert result.type == alarm_type
    assert result.severity == severity_alarm
    assert result.acknowledged == ack
    assert result.cleared == clear

def test_save_alarm(alarm_controller):

    alarm_controller.tb_client.save_alarm = MagicMock(return_value="mocked_result")
    alarm = {"mock": "alarm"}
    result = alarm_controller.save_alarm(alarm)
    assert result is not None 

