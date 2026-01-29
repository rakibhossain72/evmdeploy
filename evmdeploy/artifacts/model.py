from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass(frozen=True)
class ContractArtifact:
    name: str
    abi: List[Dict[str, Any]]
    bytecode: str
    compiler_version: str
    source_hash: str
