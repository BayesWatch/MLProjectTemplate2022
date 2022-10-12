from dataclasses import dataclass
from typing import Any

from mlproject.base.utils.typing_utils import get_module_import_path
from mlproject.configs.base import DataLoaderConfig
from mlproject.configs.datasets import InstagramImageTextMultiModalDatasetConfig
from mlproject.configs.string_variables import DATASET_DIR
from mlproject.data.datamodules import InstagramImageTextDataModule


@dataclass
class InstagramImageTextMultiModalDataModuleConfig:
    _target_: Any = get_module_import_path(InstagramImageTextDataModule)
    dataset_config: Any = InstagramImageTextMultiModalDatasetConfig(
        dataset_dir=DATASET_DIR
    )
    data_loader_config: Any = DataLoaderConfig()
