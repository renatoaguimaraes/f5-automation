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
parser.add_option("-p", "--pool", dest="pool", help="Informe o nome do pool: -p nome-pool")
(options, args) = parser.parse_args()
# verify pool
if mgmt.tm.ltm.pools.pool.exists(name=options.pool, partition='Common'):
    print('Pool "' + options.pool + '" ja cadastrado')
    sys.exit(0)
# create pool        
else:
    mgmt.tm.ltm.pools.pool.create(name=options.pool, partition='Common', description='Pool criado automaticamente', monitor='http', loadBalancingMode='observed-member')
    print('Pool "' + options.pool + '" cadastrado com sucesso')
 