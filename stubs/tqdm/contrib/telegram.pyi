from .utils_worker import MonoWorker
from tqdm.auto import tqdm as tqdm_auto
from typing import Any

class TelegramIO(MonoWorker):
    API: str
    token: Any
    chat_id: Any
    session: Any
    text: Any
    message_id: Any
    def __init__(self, token, chat_id) -> None: ...
    def write(self, s): ...

class tqdm_telegram(tqdm_auto):
    tgio: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def display(self, **kwargs) -> None: ...
    def clear(self, *args, **kwargs) -> None: ...

def ttgrange(*args, **kwargs): ...
tqdm = tqdm_telegram
trange = ttgrange
