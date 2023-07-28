from pathlib import Path
import yaml

__all__ = ('load_config')


def load_config(config_file=None) -> dict:
    def load_file():


    if config_file is not None:
        if (Path(__file__).parent / config_file).exists():
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
                return config

    else:
        default_file = Path(__file__).parent / 'config.yaml'
        if default_file.exists():
            with open(default_file, 'r') as f:
                config = yaml.safe_load(f)
                return config
        else:
            raise FileNotFoundError(
                'Please add config file in current directory and set load_config(config_file=<your_config_file.yaml>)'
                f'\nor add default_config file "{default_file}"'
            )
