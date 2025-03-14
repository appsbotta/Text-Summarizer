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

@dataclass(frozen=True)
class modelTrainerConfig:
    rootDir: Path
    dataPath: Path
    modelCkpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int
    size: int

@dataclass(frozen=True)
class modelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path