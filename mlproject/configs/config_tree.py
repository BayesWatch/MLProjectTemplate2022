import os
from dataclasses import MISSING, dataclass, field
from typing import Any, List, Optional

from omegaconf import OmegaConf

from mlproject.base.utils import get_logger
from mlproject.configs.callbacks import (
    LearningRateMonitor,
    LogConfigInformation,
    LogGrads,
    ModelSummaryConfig,
    RichProgressBar,
    UploadCodeAsArtifact,
    model_checkpoint_eval,
    model_checkpoint_train,
)

log = get_logger(__name__)

defaults = [
    {"callbacks": "wandb"},
    {"logger": "wandb"},
    {"model": "clip-image-text"},
    {"datamodule": "InstagramImageTextMultiModal"},
    {"optimizer": "AdamW"},
    {"trainer": "base"},
    {"mode": "base"},
    {"hydra": "custom_logging_path"},
]

overrides = []

OmegaConf.register_new_resolver("last_bit", lambda x: x.split(".")[-1])
OmegaConf.register_new_resolver("lower", lambda x: x.lower())
OmegaConf.register_new_resolver(
    "remove_redundant_words",
    lambda x: x.replace("scheme", "").replace("module", "").replace("config", ""),
)


@dataclass
class Config:
    callbacks: Any = MISSING
    logger: Any = MISSING
    model: Any = MISSING
    datamodule: Any = MISSING
    optimizer: Any = MISSING
    trainer: Any = MISSING
    mode: Any = MISSING
    hydra: Any = MISSING

    resume: bool = False
    checkpoint_path: Optional[str] = None
    # pretty print config at the start of the run using Rich library
    print_config: bool = True

    # disable python warnings if they annoy you
    ignore_warnings: bool = True
    logging_level: str = "INFO"
    prefix: str = ""
    # evaluate on test set, using best model weights achieved during training
    # lightning chooses best weights based on metric specified in checkpoint
    # callback
    test_after_training: bool = True
    batch_size: int = 1
    # seed for random number generators in learn2learn_hub, numpy and python.random
    seed: int = 0
    # top level argument that sets all the downstream configs to run an
    # experiment on this many iterations

    # path to original working directory
    # hydra hijacks working directory by changing it to the new log directory
    # so it's useful to have this path as a special variable
    # https://hydra.cc/docs/next/tutorials/basic/running_your_app/working_directory
    root_experiment_dir: str = os.environ["EXPERIMENTS_DIR"]
    # path to folder with data
    data_dir: str = os.environ["DATASET_DIR"]
    defaults: List[Any] = field(default_factory=lambda: defaults)
    overrides: List[Any] = field(default_factory=lambda: overrides)
    name: str = (
        "${prefix}-"
        "${remove_redundant_words:"
        "${lower:"
        "${last_bit:"
        "${datamodule.dataset_config._target_}}}}-"
        "${last_bit:${optimizer._target_}}-"
        "${model.model_name_or_path}-"
        "pretrained=${model.pretrained}-"
        "fine_tune=${model.fine_tunable}-"
        "${seed}"
    )

    current_experiment_dir: str = "${root_experiment_dir}/${name}"
    code_dir: str = "${hydra:runtime.cwd}"


base_callbacks = dict(
    model_checkpoint_eval=model_checkpoint_eval,
    model_checkpoint_train=model_checkpoint_train,
    model_summary=ModelSummaryConfig(),
    progress_bar=RichProgressBar(),
    lr_monitor=LearningRateMonitor(),
)

wandb_callbacks = dict(
    model_checkpoint_eval=model_checkpoint_eval,
    model_checkpoint_train=model_checkpoint_train,
    model_summary=ModelSummaryConfig(),
    progress_bar=RichProgressBar(),
    lr_monitor=LearningRateMonitor,
    code_upload=UploadCodeAsArtifact(),
    log_grads=LogGrads(),
    log_config=LogConfigInformation(),
)
