# TODO : is installing it but is not accessible
from setuptools import setup, find_packages

# with open("requirements.txt") as f:
#     install_requires = f.read().splitlines()

setup(
    name="generate-dags",
    version="0.1",
    packages=find_packages(),
    # install_requires=install_requires,
    install_requires=["toml", "pydantic", "pendulum", "jinja2", "click"],
    entry_points={
        "console_scripts": [
            "generate_dags=src.generate_dags:generate_dags",
        ],
    },
)
