from evmdeploy.compiler.solidity import compile_solidity
from evmdeploy.crypto.signer import sign_transaction
from evmdeploy.encoding.constructor import encode_constructor_args
from evmdeploy.artifacts.model import ContractArtifact
from typing import List, Dict


deployer_address: str = "0x7375299739fcb8e36b2b25ac61989dccbc8a6daa"

artifacts = compile_solidity(
    "contracts/Vault.sol",
)



contracts: List[ContractArtifact] = []

for name, artifact in artifacts.items():
    contracts.append(artifact)
    constructor_args = encode_constructor_args(artifact.abi, deployer_address)
    print(constructor_args.hex())