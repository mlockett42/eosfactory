from  eosfactory import *
import testnode_data

testnet = testnode_data.kylin
set_nodeos_address(testnet.url)
set_nodeos_address(testnet.url, prefix="registering_to_testnode")
remove_testnet_cache()

verify_testnet()

create_wallet(file=True)
create_master_account("master")

create_master_account("master", testnet)

