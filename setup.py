"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import pathlib

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="mlproject",  # Required
    version="0.0.1",  # Required
    description="A template package for ML research projects build with HF transformers,"
    " hydra zen and wandb",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/BayesWatch/MLProjectTemplate2022.git",  # Optional
    author="Antreas Antoniou",  # Optional
    author_email="antreas@metalearnit.ai",  # Optional
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Machine Learning :: Tracking/Checkpointing of Experiments",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="wandb, ml, development",  # Optional
    packages=[
        "mlproject",
    ],
    python_requires=">=3.8, <4",
    # install_requires=["wandb"],
)
