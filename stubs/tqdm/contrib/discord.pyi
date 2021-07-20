from .utils_worker import MonoWorker
from tqdm.auto import tqdm as tqdm_auto
from typing import Any

class DiscordIO(MonoWorker):
    text: Any
    message: Any
    def __init__(self, token, channel_id) -> None: ...
    def write(self, s): ...

class tqdm_discord(tqdm_auto):
    dio: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def display(self, **kwargs) -> None: ...
    def clear(self, *args, **kwargs) -> None: ...

def tdrange(*args, **kwargs): ...
tqdm = tqdm_discord
trange = tdrange
