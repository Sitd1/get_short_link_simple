import yaml
import re
import uuid

from pathlib import Path


def load_config(config_file=None) -> dict:

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


def is_valid_url(url) -> bool:
    # Регулярное выражение для проверки формата URL
    pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    # Проверяем, соответствует ли ссылка формату URL
    if re.match(pattern, url):
      return True
    else:
        return False


def generate_short_url(length: int = 8) -> str:
    # UUID  Generation
    short_link = str(uuid.uuid4()).replace('-', '')[:length]
    return short_link
