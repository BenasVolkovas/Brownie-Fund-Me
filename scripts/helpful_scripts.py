from brownie import MockV3Aggregator, network, accounts, config
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 2000 * 10 ** 8

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

# Get account depending on active network chain
def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


# Get the price feed address for smart contract deployment
def get_price_feed_address():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        priceFeedAddress = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"Network: {network.show_active()}")

        # Create/Get mock of price feed
        if len(MockV3Aggregator) <= 0:
            print("Deploying Mocks...")
            MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
            print("Mocks Deployed!")
        priceFeedAddress = MockV3Aggregator[-1].address

    return priceFeedAddress
