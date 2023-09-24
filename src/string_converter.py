"""This converter will return a string of text converted from
one known format to another."""

# Idea - each needs a signal for next word,
# which for camel case is a capital letter
# and for snake case is an underscore.

class CamelCase(str):
  """A string that is in CamelCase."""
  def __init__(self) -> None:
    super().__init__()

class SnakeCase(str):
  """A string that is in snake_case."""
  def __init__(self) -> None:
    super().__init__()

def char_is_underscore(character:str):
  """Test whether a character is an underscore (`_`).

  Raises:
    ValueError: when the character is not len of 1."""
  if len(character) != 1:
    raise ValueError('character must be length 1 string.')

  if character == '_':
    return True
  else:
    return False

def char_is_capital(character:str):
  """Test whether a character is capitalized (e.g. `A`).

  Raises:
    ValueError: when the character is not len of 1."""
  if len(character) != 1:
    raise ValueError('character must be length 1 string.')

  if character.isupper():
    return True
  else:
    return False

def detect_snake_case(text:str):
  """True if string contains an underscore character."""
  has_underscores = False
  for char in text:
    if char_is_underscore(char):
      has_underscores = True
      break
  return has_underscores

def detect_camel_case(text:str):
  """True if string contains uppercase character."""
  has_caps = False
  for char in text:
    if char_is_capital(char):
      has_caps = True
      break
  return has_caps

def _convert_camel_case_to_list(text:str):
  """Convert camelCase to ['camel', 'case']."""
  indexes_of_caps = []
  start_index = 0
  for char in text:
    if char_is_capital(char):
      index_of_this_cap = text.index(char, start_index)
      indexes_of_caps.append(
        index_of_this_cap
      )
      start_index = index_of_this_cap + 1
  print("step 1, indexes of caps:", indexes_of_caps)
  # TODO good test case coverage of this index shinanigans.
  list_of_words = []
  start_index = 0
  for index in indexes_of_caps:
    print ("start_index", start_index, "- type:", type(start_index),
           "\nindex:", index, "- type:", type(index))
    list_of_words.append(text[start_index:index].lower())
    start_index = index
  list_of_words.append(text[start_index:].lower())
  print("step 2, list of words:", list_of_words)
  return list_of_words

def _convert_snake_case_to_list(text:str):
  """Convert snake_case to ['snake', 'case']"""
  return text.split('_')

def convert_to_list_of_strings(name:str):
  """Detects snake_case or camelCase; else, throws."""
  is_camel_case = detect_camel_case(name)
  is_snake_case = detect_snake_case(name)
  if ((is_camel_case and is_snake_case)
      or
      (not (is_camel_case or is_snake_case))):
    raise ValueError('Cant handle non- snake or camel case.')

  if is_camel_case:
    return _convert_camel_case_to_list(name)

  if is_snake_case:
    return _convert_snake_case_to_list(name)

def convert(text:str):
  finished_list_of_words = []
  # Conditional convert to snake_case.
  if has_caps and not has_underscores:
    words = text.split() # Split on capitals?


def run():
  _convert_camel_case_to_list('camelCase')


if __name__ == '__main__':
  run()
