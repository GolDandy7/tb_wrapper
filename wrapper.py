from tb_rest_client.rest_client_ce import *
from handle_exception import *
'''
Connection and User Controller
'''

def tb_connection(tb_url, userfile, passwordfile):
    tb_rest_client = RestClientCE(base_url=tb_url)
    with open(userfile) as f: 
        USERNAME = f.readline().strip()
    with open(passwordfile) as f: 
       PASSWORD = f.readline().strip()
    tb_rest_client.login(username=USERNAME, password=PASSWORD)
    return tb_rest_client

def tb_connection_with_strings(tb_url, username, password):
    tb_rest_client = RestClientCE(base_url=tb_url)
    tb_rest_client.login(username=username, password=password)
    return tb_rest_client

def actual_user(tb_client):
    return tb_client.get_user()

def get_users_from_customer(tb_client, customer_id):
    return tb_client.get_customer_users(customer_id=customer_id, page_size=1000, page=0)

def get_tenant_id(tb_client):
    return tb_client.get_user().tenant_id.id

def get_tenant_entity_id(tb_client):
    return tb_client.get_user().tenant_id

'''
Asset Controller
'''
def get_default_asset_profile_info(tb_client):
    return tb_client.get_default_asset_profile_info()

# TODO: change id to obj id 
def create_asset(tb_client,asset_profile_id, asset_name, customer_id):    
    customer_obj_id = CustomerId(customer_id, "CUSTOMER")
    asset = Asset(name=asset_name, asset_profile_id=asset_profile_id, customer_id=customer_obj_id)
    asset = tb_client.save_asset(asset)
    return asset

# TODO: remove this function replaced by create_asset_profile
def create_profile(tb_client, profile_name, profile_type):
    tenant_id = get_tenant_entity_id(tb_client)
    match profile_type:
    
        case "ASSET_PROFILE":
            asset_profile = AssetProfile(name=profile_name, description=profile_name, tenant_id=tenant_id)
            return tb_client.save_asset_profile(asset_profile)
            
        case "DEVICE_PROFILE":
            device_profile = DeviceProfile(name=profile_name,
                                        profile_data=DeviceProfileData(configuration={"type": "DEFAULT"}, transport_configuration={"type": "DEFAULT"}),
                                        type="DEFAULT",
                                        transport_type='DEFAULT',
                                        tenant_id=tenant_id)
            return tb_client.save_device_profile(device_profile)

        case _:
            raise GenericException("Profile type " + profile_type + " not allowed. Allowed values: [ASSET_PROFILE, DEVICE_PROFILE]")


def create_asset_profile(tb_client, profile_name):
    tenant_id = get_tenant_entity_id(tb_client)    
    asset_profile = AssetProfile(name=profile_name, description=profile_name, tenant_id=tenant_id)
    return tb_client.save_asset_profile(asset_profile)
            
       
def check_asset_exists_by_name(tb_client,asset_name):
    info_asset = tb_client.get_tenant_asset_infos(page_size=10000, page=0)
    for info in info_asset.data:
        if info.name == asset_name:
            return True
    return False

# TODO: remove this function  replaced with check_asset_profile_exists_by_name
def check_profile_exists_by_name(tb_client, profile_name, profile_type):
    match profile_type:
        case "ASSET_PROFILE":
            profiles = tb_client.get_asset_profiles(page=0, page_size=1000)
            for profile in profiles.data:
                if profile.name == profile_name:
                    return True
            return False

        case "DEVICE_PROFILE":
            profiles = tb_client.get_device_profiles(page=0, page_size=1000)
            for profile in profiles.data:
                if profile.name == profile_name:
                    return True
            return False

        case _:
            raise GenericException("Profile type " + profile_type + " not allowed. Allowed values: [ASSET_PROFILE, DEVICE_PROFILE]")
        

def check_asset_profile_exists_by_name(tb_client, profile_name):

    profiles = tb_client.get_asset_profiles(page=0, page_size=1000)
    for profile in profiles.data:
        if profile.name == profile_name:
            return True
    return False

def get_profile_by_name(tb_client, profile_name, profile_type):

    match profile_type:
        case "ASSET_PROFILE":
            profiles = tb_client.get_asset_profiles(page=0, page_size=1000)
            for profile in profiles.data:
                if profile.name == profile_name:
                    return profile
            raise GenericException("Profile: " + profile_name + ", with profile type: " + profile_type + ", does not exist.")

        case "DEVICE_PROFILE":
            profiles = tb_client.get_device_profiles(page=0, page_size=1000)
            for profile in profiles.data:
                if profile.name == profile_name:
                    return profile
            raise GenericException("Profile: " + profile_name + ", with profile type: " + profile_type + ", does not exist.")

        case _:
            raise GenericException("Profile type " + profile_type + " not allowed. Allowed values: [ASSET_PROFILE, DEVICE_PROFILE]")

def get_asset_profile_by_name(tb_client, profile_name):


    profiles = tb_client.get_asset_profiles(page=0, page_size=1000)
    for profile in profiles.data:
        if profile.name == profile_name:
            return profile
    raise GenericException("Profile: " + profile_name + " does not exist.")

def save_asset_attributes(tb_client, asset_id, scope, body):
    return tb_client.save_entity_attributes_v2(asset_id, scope, body)

def get_tenant_asset(tb_client, asset_name):
    return tb_client.get_tenant_asset(asset_name)


def create_relation(tb_client,from_id, to_id,relation_type):
    relation = EntityRelation(_from=from_id, to=to_id, type=relation_type)
    relation = tb_client.save_relation(relation)
    return relation

'''
Alarm Controller
'''
# TODO: customer id da passare come object e rimuovere la creazione di CustomerId nel metodo
def build_alarm(tenant_obj_id, alarm_name, alarm_type, entity_orginator, customer_id, severity_alarm, alarm_status, ack, clear):    
    #my_entity_originator = EntityId(entity_orginator.id,"DEVICE")
    customer = CustomerId(customer_id,"CUSTOMER")

    return Alarm(tenant_id=tenant_obj_id,
                 name=alarm_name,
                 type=alarm_type,
                 originator=entity_orginator,
                 customer_id=customer,
                 severity=severity_alarm,
                 status=alarm_status,
                 acknowledged=ack,
                 cleared=clear)

def save_alarm(tb_client, alarm):
    return tb_client.save_alarm(alarm)


'''
Query Controller 
'''
def query_body_attribute (filter_key_scope,filter_key_name,filter_key_value,filter_key_type):
    predicate = {"operation": "EQUAL",
                  "value": {"defaultValue": filter_key_value},
                  "type": filter_key_type}    
    ef = EntityFilter(entity_type="CUSTOMER",type="entityType",resolve_multiple=True)
    filter_key = EntityKey(key=filter_key_name,type=filter_key_scope)
    mfilter = KeyFilter(key=filter_key, value_type=filter_key_type,predicate=predicate)
    
    field = EntityKey(type="ENTITY_FIELD",key="name")
    latest_values_field = EntityKey(type=filter_key_scope,key=filter_key_name)

    page = EntityDataPageLink(page=0,page_size=1000,dynamic=True)

    body = EntityDataQuery(entity_fields=[field],entity_filter=ef, key_filters=[mfilter], page_link=page,latest_values=[latest_values_field])
    
    return body

#find customers_by attribute: attribute_scope,attribute_value,attribute_keyname,attribute_type
def find_customers_by_attribute(tb_client,filter_key_scope,filter_key_name,filter_key_value,filter_key_type):
    body = query_body_attribute (filter_key_scope,filter_key_name,filter_key_value,filter_key_type)
    return tb_client.find_entity_data_by_query(body=body)

'''
Device Controller
'''

def get_tenant_device(tb_client, device_name):
    return tb_client.get_tenant_device(device_name)
def check_device_exists_by_name(tb_client,device_name):
    info_device =tb_client.get_tenant_device_infos(page_size=10000, page=0)
    for info in info_device.data:
        if info.name == device_name:
            return True
    return False

def create_device_with_customer(tb_client,device_profile_id, device_name, customer_id):
    customer = CustomerId(customer_id,"CUSTOMER")
    device = Device(name=device_name, device_profile_id=device_profile_id, customer_id=customer)
    device = tb_client.save_device(device)
    return device


def create_device_without_customer(tb_client,device_profile_id, device_name):
    device = Device(name=device_name, device_profile_id=device_profile_id)
    device = tb_client.save_device(device)
    return device

def save_device_attributes(tb_client, device_id, scope, body):
    return tb_client.save_device_attributes(device_id, scope, body)

def get_default_device_profile_info(tb_client):
    return tb_client.get_default_device_profile_info()