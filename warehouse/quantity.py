"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a positive integer quantity parsed from *value*.

    Raises ValueError for zero or negative quantities.
    """
    result = int(value.strip())
    if result <= 0:
        raise ValueError(f"quantity must be positive, got {result}")
    return result
