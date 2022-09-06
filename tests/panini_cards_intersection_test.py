import unittest
from panini_cards_intersection import cards_intersection, assemble_repeated_dict

class TestPaniniCardsIntersection(unittest.TestCase):
    def test_assemble_repeated_dict(self):
        fixtures = [
            {
                "args": ["FWC 1"],
                "expected": {"FWC1": True}
            },
            {
                "args": ["FWC 1", "FWC 2"],
                "expected": {"FWC1": True, "FWC2": True}
            },
            {
                "args": [],
                "expected": {}
            },
        ]

        for fixture in fixtures:
            self.assertDictEqual(fixture["expected"], assemble_repeated_dict(fixture["args"]))


    def test_cards_intersection(self):
        fixtures = [
            {
                "args": ["FWC 1, FWC2", "FWC 1, FWC 2"],
                "expected": "FWC 1, FWC2"
            },
            {
                "args": ["FWC 1|FWC2", "FWC 1|FWC 2", "|"],
                "expected": "FWC 1|FWC2"
            },
            {
                "args": ["FWC 1, FWC2", "FWC 2"],
                "expected": "FWC2"
            },
            {
                "args": ["FWC 1", "FWC 2"],
                "expected": ""
            },
            {
                "args": ["", ""],
                "expected": ""
            }
        ]

        for fixture in fixtures:
            self.assertEqual(fixture["expected"], cards_intersection(*fixture["args"]))

if __name__ == "__main__":
    unittest.main()