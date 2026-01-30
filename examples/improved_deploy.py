import os
from evmdeploy import compile_solidity, Contract

def main():
    # 1. Improved compile_solidity with optimizer settings
    artifacts = compile_solidity(
        "contracts/Vault.sol",
        optimizer=True,
        runs=500
    )
    
    vault_artifact = artifacts["Vault"]
    
    # 2. Use the new combined Contract object
    vault = Contract(vault_artifact)
    print(f"Contract: {vault.name}")
    
    # 3. Encode constructor args through the Contract object
    # Assume Vault has a constructor that takes an address
    owner_address = "0x0000000000000000000000000000000000000001"
    encoded_args = vault.encode_constructor_args(owner_address)
    print(f"Encoded constructor args: {encoded_args.hex()}")
    
    # 4. Sign deployment transaction through the Contract object
    # (Mock private key for demonstration)
    private_key = "0x" + "1" * 64
    
    signed_tx = vault.sign_deployment(
        private_key=private_key,
        nonce=0,
        gas=2000000,
        gas_price=20 * 10**9,
        chain_id=1,
        constructor_args=[owner_address]
    )
    
    print(f"Signed transaction hash: {signed_tx.hash.hex()}")
    print(f"Raw transaction length: {len(signed_tx.raw_transaction)}")

if __name__ == "__main__":
    main()
