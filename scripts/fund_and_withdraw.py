from brownie import FundMe
from brownie.network import account
from scripts.helpful_scripts import get_price_feed_address, get_account


def fund():
    fundMe = FundMe[-1]
    account = get_account()
    entranceFee = fundMe.getEntranceFee()
    print("Entry fee: ", entranceFee)
    print("Funding...")
    fundMe.fund({"from": account, "value": entranceFee})


def withdraw():
    fundMe = FundMe[-1]
    account = get_account()
    fundMe.withdraw({"from": account})


def main():
    fund()
    withdraw()
