from .std import tqdm as std_tqdm
from typing import Any

class tqdm_tk(std_tqdm):
    def __init__(self, *args, **kwargs): ...
    disable: bool
    def close(self) -> None: ...
    def clear(self, *_, **__) -> None: ...
    def display(self, *_, **__) -> None: ...
    def set_description(self, desc: Any | None = ..., refresh: bool = ...) -> None: ...
    desc: Any
    def set_description_str(self, desc: Any | None = ..., refresh: bool = ...) -> None: ...
    def cancel(self) -> None: ...
    def reset(self, total: Any | None = ...) -> None: ...

def ttkrange(*args, **kwargs): ...
tqdm = tqdm_tk
trange = ttkrange
