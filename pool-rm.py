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
    # delete pool
    pool_automacao = mgmt.tm.ltm.pools.pool.load(name=options.pool, partition='Common')
    pool_automacao.delete()
    print('Pool "' + options.pool + '" removido com sucesso')
else:    
    print('Pool "' + options.pool + '" nao encontrado')
    