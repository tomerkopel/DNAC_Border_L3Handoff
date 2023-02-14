import dnacentersdk.api.v1_2_10.fabric_wired
from dnacentersdk import api
import json

dnac = api.DNACenterAPI(base_url="https://10.7.250.6", username='admin', password='C1sco12345', verify=False, version="2.2.3.3")

#virtual_network = dnac.sda.add_virtual_network_with_scalable_groups(virtualNetworkName="Kopel_Test")
#print(json.dumps(virtual_network, indent=4))

#task_status = dnac.task.get_task_by_id(task_id="c69f6e44-2055-45a3-ba77-4997e00d6d98")
#print(json.dumps(task_status, indent=4))

#add_vn_to_site = dnac.sda.add_vn(payload={'siteNameHierarchy': 'Global/EMEAR/Israel/NTN01', 'virtualNetworkName': 'Kopel_Test'})
#print(json.dumps(add_vn_to_site, indent=4))


vn = dnac.sda.get_virtual_network_with_scalable_groups(virtual_network_name="Campus")
print(json.dumps(vn, indent=4))

border_device = dnac.sda.gets_border_device_detail(device_management_ip_address="10.7.250.202")
#
# with open("output.json", "w") as outfile:
#      outfile.write(json.dumps(border_device, indent=4))
added_border_device = dnac.sda.adds_border_device()
print(json.dumps(border_device, indent=4))

