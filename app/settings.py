from pathlib import Path
import yaml

__all__ = ('load_config')


def load_config(config_file_name=None, config_file_full_path=None) -> dict:

    def get_config(path) -> dict:
        with open(path) as f:
            config = yaml.safe_load(f)
        return config

    if config_file_name is None:
        config_file_name = 'config.yaml'

    if config_file_full_path is None:
        config_file_full_path = Path(__file__).parent

    config_file = config_file_full_path / config_file_name

    if config_file.exists():
        return get_config(config_file)
    else:
        raise FileNotFoundError(
            f'Please add config file {config_file}'
        )
