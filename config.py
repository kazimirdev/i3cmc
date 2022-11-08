from dataclasses import dataclass

from environs import Env


@dataclass
class Config:
    name: str
    price: int


def load_config(path: str = None):
    env = Env()
    env.read_env(path)
    

    return Config(
            name=env.str("NAME"),
            price=env.int("PRICE")
            )
