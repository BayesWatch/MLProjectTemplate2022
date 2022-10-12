from dataclasses import dataclass
from typing import Any

from package_name.base.utils.typing_utils import get_module_import_path
from package_name.configs.base import DataLoaderConfig
from package_name.configs.datasets import InstagramImageTextMultiModalDatasetConfig
from package_name.configs.string_variables import DATASET_DIR
from package_name.data.datamodules import InstagramImageTextDataModule


@dataclass
class InstagramImageTextMultiModalDataModuleConfig:
    _target_: Any = get_module_import_path(InstagramImageTextDataModule)
    dataset_config: Any = InstagramImageTextMultiModalDatasetConfig(
        dataset_dir=DATASET_DIR
    )
    data_loader_config: Any = DataLoaderConfig()
