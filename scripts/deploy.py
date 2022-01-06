from brownie import FundMe, network, config
from scripts.helpful_scripts import get_price_feed_address, get_account

# Deploy new Fund Me smart contract
def deploy_fund_me():
    account = get_account()
    priceFeedAddress = get_price_feed_address()

    fundMe = FundMe.deploy(
        priceFeedAddress,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fundMe.address}")

    return fundMe


def main():
    deploy_fund_me()
