from StableMarriageProblem import stable_matching, isStable
import unittest


class StableMarriageTests(unittest.TestCase):
    def test_matching(self):
        m_prefs = {'A1': ['B3', 'B2', 'B4', 'B1'], 'A2': ['B4', 'B3', 'B1', 'B2'], 'A3': ['B2', 'B1', 'B3', 'B4'],
                   'A4': ['B1', 'B2', 'B3', 'B4']}
        w_prefs = {'B1': ['A2', 'A1', 'A3', 'A4'], 'B2': ['A1', 'A4', 'A2', 'A3'], 'B3': ['A3', 'A2', 'A4', 'A1'],
                   'B4': ['A3', 'A1', 'A2', 'A4']}

        pairs = stable_matching(m_prefs, w_prefs)
        solution = {'B1': 'A4', 'B2': 'A3', 'B3': 'A1', 'B4':'A2'}

        assert pairs == solution
        assert isStable(pairs, m_prefs, w_prefs) is True


if __name__ == '__main__':
    unittest.main()