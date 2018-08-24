import os
import unittest
import setup
import eosf

from eosf import Verbosity
from eosf_wallet import Wallet

front_end.Logger.verbosity = [Verbosity.TRACE, Verbosity.OUT, Verbosity.DEBUG]

remote_testnet = "http://88.99.97.30:38888"
_ = front_end.Logger()

class Test(unittest.TestCase):

    def run(self, result=None):
        super().run(result)
        print('''

NEXT TEST ====================================================================
''')

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        front_end.set_is_testing_errors(False)
        front_end.set_throw_error(True)

    def test_create_keosd_wallet(self):
        _.SCENARIO('''
Test creation of a wallet under the KEOSD Wallet Manager.
Set-up: 
    * delete existing, if any, wallet named ``jungle_wallet`` using
        a general procedure as the EOSFactory does not have any;
    * set KEOSD as the Wallet Manager;
    * set the URL of a remote testnet;
    * stop the KEOSD Wallet Manager.
Tests:
    * create a wallet named ``jungle_wallet``;
        Expected result is that a password message is printed.
        ''')        
        wallet_name = "jungle_wallet"
        try:
            os.remove(eosf.wallet_dir() + wallet_name + ".wallet")
        except:
            pass
        front_end.set_is_testing_errors()
        setup.set_nodeos_address(remote_testnet)
        ######################################################################

        create_wallet(wallet_name)
        self.assertTrue("keys will not be retrievable." in wallet.out_buffer )

        _.COMMENT("wallet.index()")
        Wallet.wallet.index()

        _.COMMENT(" wallet.open()")
        Wallet.wallet.open()

        _.COMMENT("wallet.lock()")
        Wallet.wallet.lock()

        _.COMMENT("wallet.lock_all()")
        Wallet.wallet.lock_all()

        _.COMMENT("wallet.unlock()")
        Wallet.wallet.unlock()

        _.COMMENT("wallet.keys()")
        Wallet.wallet.keys()



    # def test_reopen_with_stored_password(self): 
    #     eosf.reset([front_end.Verbosity.INFO])
    #     eosf.Wallet()
    #     eosf.stop(is_verbose=0)
    #     eosf.run(is_verbose=0)
        
    #     wallet = eosf.Wallet()
    #     self.assertTrue(wallet.error)


    # def test_invalid_password(self): 
    #     eosf.reset([front_end.Verbosity.INFO])
    #     wallet = eosf.Wallet()
    #     eosf.stop(is_verbose=0)
    #     eosf.run(is_verbose=0)        
        
    #     wallet = eosf.Wallet(
    #         None, "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV")
    #     self.assertTrue(wallet.error)


    # def test_is_not_running_not_keosd_set(self):
    #     eosf.stop(is_verbose=0)
        
    #     wallet = eosf.Wallet()
    #     self.assertTrue(wallet.error)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()


