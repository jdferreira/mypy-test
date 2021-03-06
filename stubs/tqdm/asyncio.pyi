from .std import tqdm as std_tqdm
from typing import Any

class tqdm_asyncio(std_tqdm):
    iterable_awaitable: bool
    iterable_next: Any
    iterable_iterator: Any
    def __init__(self, iterable: Any | None = ..., *args, **kwargs) -> None: ...
    def __aiter__(self): ...
    async def __anext__(self): ...
    def send(self, *args, **kwargs): ...
    @classmethod
    def as_completed(cls, fs, *, loop: Any | None = ..., timeout: Any | None = ..., total: Any | None = ..., **tqdm_kwargs) -> None: ...
    @classmethod
    async def gather(cls, fs, *, loop: Any | None = ..., timeout: Any | None = ..., total: Any | None = ..., **tqdm_kwargs): ...

def tarange(*args, **kwargs): ...
tqdm = tqdm_asyncio
trange = tarange
