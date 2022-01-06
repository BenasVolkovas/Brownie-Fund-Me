from scripts.fund_and_withdraw import fund
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest

# Test if whole fund and withdraw process works
def test_can_fund_and_withdraw():
    # Arrange
    account = get_account()
    fundMe = deploy_fund_me()
    entranceFee = fundMe.getEntranceFee()

    # Act 1
    tx = fundMe.fund({"from": account, "value": entranceFee})
    tx.wait(1)
    # Assert 1
    assert fundMe.addressToAmountFunded(account.address) == entranceFee

    # Act 2
    tx2 = fundMe.withdraw({"from": account})
    tx2.wait(1)
    # Assert 2
    assert fundMe.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    # Make this test run only on local blockchains, because running it on mainnet can take a long time
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")

    # Arrange
    fundMe = deploy_fund_me()
    fakeAccount = accounts.add()

    # Act, Assert
    with pytest.raises(exceptions.VirtualMachineError):
        fundMe.withdraw({"from": fakeAccount})
