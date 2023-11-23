from MainController import MainController
from tb_rest_client.rest_client_ce import *
from handle_exception import *

@handle_tb_wrapper_exception
class AssetController(MainController):
    tb_client = None

    def __init__(self, tb_url, userfile, passwordfile):
        super().__init__(tb_url, userfile, passwordfile)
            
    def get_default_asset_profile_info(self):
        return self.tb_client.get_default_asset_profile_info()

    def create_asset(self, asset_profile_id, asset_name, customer_obj_id):
        asset = Asset(name=asset_name, asset_profile_id=asset_profile_id, customer_id=customer_obj_id)
        asset = self.tb_client.save_asset(asset)
        return asset

    def create_asset_profile(self, profile_name):
        tenant_id = get_tenant_entity_id(self.tb_client)    
        asset_profile = AssetProfile(name=profile_name, description=profile_name, tenant_id=tenant_id)
        return self.tb_client.save_asset_profile(asset_profile)
        
    def check_asset_exists_by_name(self, asset_name):
        info_asset = self.tb_client.get_tenant_asset_infos(page_size=10000, page=0)
        for info in info_asset.data:
            if info.name == asset_name:
                return True
        return False

    def check_asset_profile_exists_by_name(self, profile_name):
        profiles = self.tb_client.get_asset_profiles(page=0, page_size=1000)
        for profile in profiles.data:
            if profile.name == profile_name:
                return True
        return False

    def get_asset_profile_by_name(self, profile_name):
        profiles = self.tb_client.get_asset_profiles(page=0, page_size=1000)
        for profile in profiles.data:
            if profile.name == profile_name:
                return profile
        raise GenericException("Profile: " + profile_name + ", with profile type: " + profile_type + ", does not exist.")

    def get_asset_profile_by_name(self, profile_name):
        profiles = self.tb_client.get_asset_profiles(page=0, page_size=1000)
        for profile in profiles.data:
            if profile.name == profile_name:
                return profile
        raise GenericException("Profile: " + profile_name + " does not exist.")

    def save_asset_attributes(self, asset_id, scope, body):
        return self.tb_client.save_entity_attributes_v2(asset_id, scope, body)

    def get_tenant_asset(self, asset_name):
        return self.tb_client.get_tenant_asset(asset_name)

    def create_relation(self, from_id, to_id,relation_type):
        relation = EntityRelation(_from=from_id, to=to_id, type=relation_type)
        relation = self.tb_client.save_relation(relation)
        return relation