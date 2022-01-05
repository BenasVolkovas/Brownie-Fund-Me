from brownie import MockV3Aggregator, network, accounts, config
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 2000 * 10 ** 8
LOCAL_BLOCKCHAIN_ENVS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def get_price_feed_address():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVS:
        priceFeedAddress = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"Network: {network.show_active()}")

        if len(MockV3Aggregator) <= 0:
            print("Deploying Mocks...")
            MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
            print("Mocks Deployed!")
        priceFeedAddress = MockV3Aggregator[-1].address

    return priceFeedAddress
