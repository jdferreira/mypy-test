from collections.abc import Generator
from typing import Any

def product(*iterables, **tqdm_kwargs) -> Generator[Any, None, None]: ...
