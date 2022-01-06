from brownie import FundMe
from brownie.network import account
from scripts.helpful_scripts import get_price_feed_address, get_account


# Fund the contract with the needed amount
def fund():
    fundMe = FundMe[-1]
    account = get_account()
    entranceFee = fundMe.getEntranceFee()
    print("Entry fee: ", entranceFee)
    print("Funding...")
    fundMe.fund({"from": account, "value": entranceFee})


# Withdraw all money
def withdraw():
    fundMe = FundMe[-1]
    account = get_account()
    fundMe.withdraw({"from": account})


def main():
    fund()
    withdraw()
