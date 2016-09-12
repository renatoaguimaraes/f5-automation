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
parser.add_option("-m", "--member", dest="member", help="Informe o nome do membro: -m ip:porta")
(options, args) = parser.parse_args()
# load pool
pool = mgmt.tm.ltm.pools.pool.load(name=options.pool, partition='Common')
# verify member
if pool.members_s.members.exists(name=options.member, partition='Common'):
    print('Pool "' + pool.name + '" encontrado com sucesso')
    member = pool.members_s.members.load(name=options.member, partition='Common')
    member.delete()
    print('Membro "' + options.member + '" removido do pool ' + options.pool + ' com sucesso')
else:
    print('Membro ' + options.member + ' nao encontrado no pool ' + options.pool)
