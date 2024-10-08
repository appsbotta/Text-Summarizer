from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class dataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class dataValidationConfig:
    rootDir:Path
    statusFile: str
    allRequiredFiles:list    
    
@dataclass(frozen=True)
class dataTransformationConfig:
    rootDir: Path
    dataPath: Path
    tokenizerName: Path