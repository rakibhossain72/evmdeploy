from evmdeploy.compiler.solidity import compile_solidity

artifacts = compile_solidity(
    "contracts/Vault.sol",
)

for name, artifact in artifacts.items():
    print(name, artifact)
