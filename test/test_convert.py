"""Tests for string_converter.py."""

import unittest

import src.string_converter as converter

class StringConverterTestCase(unittest.TestCase):
  # region: char_is_underscore.
  def test_is_underscore_given_underscore(self):
    self.assertTrue(
      converter.char_is_underscore('_')
    )

  def test_is_underscore_given_letter(self):
    self.assertFalse(
      converter.char_is_underscore('A')
    )

  def test_is_underscore_given_number(self):
    self.assertFalse(
      converter.char_is_underscore('1')
    )

  def test_is_underscore_throws_on_len_gt_1(self):
    self.assertRaises(
      ValueError,
      converter.char_is_underscore,
      '123'
    )

  def test_is_underscore_throws_on_len_lt_1(self):
    self.assertRaises(
      ValueError,
      converter.char_is_underscore,
      ''
    )
  # endregion: char_is_underscore.
  # region: char_is_capital.
  def test_is_capital_given_symbol(self):
    self.assertFalse(
      converter.char_is_capital('_')
    )

  def test_is_capital_given_capital(self):
    self.assertTrue(
      converter.char_is_capital('A')
    )

  def test_is_capital_given_lower_case(self):
    self.assertFalse(
      converter.char_is_capital('a')
    )


  def test_is_capital_given_number(self):
    self.assertFalse(
      converter.char_is_capital('1')
    )

  def test_is_capital_throws_on_len_gt_1(self):
    self.assertRaises(
      ValueError,
      converter.char_is_capital,
      'ABC'
    )

  def test_is_capital_throws_on_len_lt_1(self):
    self.assertRaises(
      ValueError,
      converter.char_is_capital,
      ''
    )
  # endregion: char_is_capital.
  # region: convert_camel_case_to_list.
  def test_camel_to_list_two_words(self):
    self.assertEqual(
      converter.convert_to_list_of_strings('camelCase'),
      ['camel', 'case']
    )

  def test_camel_to_list_three_words(self):
    self.assertEqual(
      converter.convert_to_list_of_strings('camelCaseExample'),
      ['camel', 'case', 'example']
    )
  # endregion: convert_camel_case_to_list.
  # region: convert_snake_case_to_list.
  def test_snake_to_list_two_words(self):
    self.assertEqual(
      converter.convert_to_list_of_strings('snake_case'),
      ['snake', 'case']
    )

  def test_snake_to_list_three_words(self):
    self.assertEqual(
      converter.convert_to_list_of_strings('snake_case_example'),
      ['snake', 'case', 'example']
    )
  # endregion: convert_snake_case_to_list.

  def test_convert_snake_to_camel(self):
    start_string = 'snake_case_to_camel_case_example'
    converted_string = converter.convert(start_string)
    expected_string = 'snakeCaseToCamelCaseExample'
    self.assertEqual(
      converted_string,
      expected_string
    )

  def test_convert_camel_to_snake(self):
    start_string = 'camelCaseToSnakeCaseExample'
    converted_string = converter.convert(start_string)
    expected_string = 'camel_case_to_snake_case_example'
    self.assertEqual(
      converted_string,
      expected_string
    )


if __name__ == '__main__':
  unittest.main()
