from typing import Callable


class MysqlConfig:
    def __init__(self, save_function: Callable = None):
        self.save = save_function or (lambda: None)

        self.host = '127.0.0.1'
        self.port = 3306

    def to_dict(self) -> dict:
        return {
            'host': self.host,
            'port': self.port,
        }

    def __setattr__(self, key, value) -> None:
        super().__setattr__(key, value)
        self.save()

    def update(self, config: dict) -> None:
        for key, value in config.items():
            if hasattr(self, key):
                t = type(getattr(self, key))
                setattr(self, key, t(value))

    def __len__(self) -> int:
        return len(self.to_dict())
