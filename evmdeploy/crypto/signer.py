from eth_account import Account
from eth_account.signers.local import LocalAccount
from eth_account.types import PrivateKeyType
from eth_account.datastructures import SignedTransaction
from web3 import Web3
from typing import Dict, Any


def sign_transaction(
    transaction: Dict[str, Any],
    private_key: PrivateKeyType,
) -> SignedTransaction:
    """
    Signs an Ethereum transaction (e.g. contract deployment or regular transfer)
    with the given private key.

    Args:
        transaction: Unsigned transaction dictionary.
                     Must contain at least: 'to', 'value', 'gas', 'gasPrice'/'maxFeePerGas' etc.
                     For contract deployment: 'to' can be None or '0x0', 'data' contains bytecode + constructor args.
        private_key: Private key (bytes, hex str, or int)

    Returns:
        Signed transaction dictionary ready for w3.eth.send_raw_transaction()
        Contains: 'rawTransaction', 'hash', 'r', 's', 'v' etc.

    Raises:
        ValueError: If transaction dict is missing required fields or malformed
        TypeError: If private_key cannot be converted to a valid signer
    """
    # 1. Create account signer from private key
    account: LocalAccount = Account.from_key(private_key)

    # 2. Sign the transaction
    #    eth_account handles EIP-1559 vs legacy automatically based on what's in the dict
    signed_tx = account.sign_transaction(transaction)

    # 3. Return the full signed transaction dict
    #    Most common thing you want next: signed_tx.rawTransaction (bytes)
    return signed_tx
