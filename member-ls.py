import sys, requests
from optparse import OptionParser
from f5.bigip import ManagementRoot
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# ignore self signed certified
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# f5 connection
mgmt = ManagementRoot("10.220.1.156", "admin", "admin")

# parser arguments
parser = OptionParser()
parser.add_option("-p", "--pool", dest="pool", help="Informe o nome do pool: -p nome-pool")
(options, args) = parser.parse_args()

# verify arguments
if not options.pool:
    parser.error('Nome do pool nao informado. Ex: member-ls -p nome-do-pool')

# verify pool
if mgmt.tm.ltm.pools.pool.exists(name=options.pool, partition='Common'):
    print('Pool "' + options.pool + '" encontrado com sucesso')
    pool = mgmt.tm.ltm.pools.pool.load(name=options.pool, partition='Common')
    # show members
    print('Membros: ')
    for member in pool.members_s.get_collection():    
        print(member.name)
else:
    print('Pool "' + options.pool + '" nao encontrado')
    sys.exit(0)   
