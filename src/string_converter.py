"""This converter will return a string of text converted from
one known format to another."""

class CamelCase(str):
  """A string that is in CamelCase."""
  def __init__(self) -> None:
    super().__init__()

class SnakeCase(str):
  """A string that is in snake_case."""
  def __init__(self) -> None:
    super().__init__()
