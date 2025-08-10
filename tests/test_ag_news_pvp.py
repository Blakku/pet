import unittest
from unittest.mock import MagicMock
from pet.ag_news_pvp import AGNewsPVP
from pet.tasks import InputExample


class TestAgNewsPVP(unittest.TestCase):
    def setUp(self):
        mock_wrapper = MagicMock()
        self.pvp = AGNewsPVP(mock_wrapper)

    def test_get_parts_pattern0(self):
        self.pvp.pattern_id = 0
        example = InputExample(
        guid="test 1",
        text_a="Apple releases new iPhone.",
        text_b=None,
        label="0"
    )
        parts_a,parts_b = self.pvp.get_parts(example)
        self.assertIsInstance(parts_a,list)
        self.assertTrue(any("iPhone" in str(part) for part in parts_a if isinstance(part,str)))

    def test_get_parts_pattern1_with_text_b(self):
        self.pvp.pattern_id = 1
        example = InputExample(
            guid= "test 2",
            text_a="Breaking news:",
            text_b="Stock market surges.",
            label="2"
        )
        parts_a, parts_b = self.pvp.get_parts(example)
        # loosing assertion to check both lists
        combine_parts = [str(p) for p in parts_a + parts_b if isinstance(p, str)]
        self.assertTrue(any("Stock market" in p for p in combine_parts))

    def test_get_parts_pattern2(self):
        self.pvp.pattern_id = 2
        example = InputExample(
            guid="test 3",
            text_a="NASA launches rocket.",
            label=3

        )
        parts_a, parts_b = self.pvp.get_parts(example)
        self.assertGreater(len(parts_a), 0)

    def test_get_parts_pattern3(self):
        self.pvp.pattern_id = 3
        example = InputExample(
            guid="test 4",
            text_a="Team wins championship.",
            label="1"
        )
        parts_a, parts_b = self.pvp.get_parts(example)
        self.assertGreater(len(parts_a),0)

    def test_get_part_invalid_pattern(self):
        self.pvp.pattern_id = 999
        example = InputExample(
            guid="test_valid",
            text_a="Some irrelevant news text",
            text_b=None,
            label=0
        )
        # Expect a ValueError for unsupported pattern
        with self.assertRaises(ValueError):
            self.pvp.get_parts(example)

    def test_verbalize_valid_label(self):
        self.assertEqual(self.pvp.verbalize("0"), ["World"])
        self.assertEqual(self.pvp.verbalize("1"),["Sports"])
        self.assertEqual(self.pvp.verbalize("2"),["Business"])
        self.assertEqual(self.pvp.verbalize("3"),["Science/Tech"])

    def test_verbalize_invalid_label(self):
        result = self.pvp.verbalize("99")
        self.assertTrue(isinstance(result, list))
        self.assertGreaterEqual(len(result),0)


if __name__ == "__main__":
    unittest.main()
