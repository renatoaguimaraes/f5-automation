import requests
from f5.bigip import ManagementRoot
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# ignore self signed certified
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# f5 connection
mgmt = ManagementRoot("10.220.1.156", "admin", "admin")
# virtual servers
virtuals = mgmt.tm.ltm.virtuals.get_collection()
for vs in virtuals:
    print('(' + vs.mask + ') - ' + vs.name)