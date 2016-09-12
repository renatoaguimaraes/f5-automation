import sys, requests
from optparse import OptionParser
from f5.bigip import ManagementRoot
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# ignore self signed certified
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# f5 connection
mgmt = ManagementRoot("10.220.1.156", "admin", "admin")
# arguments parser
parser = OptionParser()
parser.add_option("-vs", "--virtual-server", dest="virtual_server", help="Informe o nome do vs: -vs nome-do-virtual-server")
(options, args) = parser.parse_args()
# verify virtual server
if mgmt.tm.ltm.virtuals.virtual.exists(name=options.virtual_server, partition='Common'):
    print('Virtual server "' + options.virtual_server + '" já cadastrado')
# create virtual server    	
else:
    mgmt.tm.ltm.virtuals.virtual.create(name=options.virtual_server, partition='Common', description='Virtual server criado automaticamente')
    print('Virtual server "' + options.virtual_server + '" cadastrado com sucesso')
    

