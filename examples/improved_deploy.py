from evmdeploy import compile_solidity, Contract, ArtifactStorage
from web3 import Web3


def main():
    # 1. Improved compile_solidity with optimizer settings
    artifacts = compile_solidity("contracts/Vault.sol", optimizer=True, runs=500)

    # 2. Store artifacts and create Contract object
    vault = Contract(artifacts["Vault"])
    vault.save()
    print(f"Artifact for {vault.name} saved.")

    # 3. Use the new combined Contract object
    print(f"Contract: {vault.name}")

    # 3. Encode constructor args through the Contract object
    # Assume Vault has a constructor that takes an address
    owner_address = "0x0000000000000000000000000000000000000001"
    encoded_args = vault.encode_constructor_args(owner_address)
    print(f"Encoded constructor args: {encoded_args.hex()}")

    # 4. Sign deployment transaction through the Contract object
    # (Mock private key for demonstration)
    private_key = "0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d"

    # For a real test, one might use a local node, but here we just check integration
    w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
    assert w3.is_connected(), "Failed to connect to the Ethereum node"

    # deploy
    result = vault.deploy(
        w3=w3, private_key=private_key, constructor_args=[owner_address]
    )

    print(f"Deployment Hash: {result.tx_hash}")
    print(f"Contract Address: {result.contract_address}")
    # print(f"Full Receipt: {result.receipt}")

    


if __name__ == "__main__":
    main()
