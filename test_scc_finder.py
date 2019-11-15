import unittest

from GraphAssignment import Graph as SccFinder


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.scc_finder = SccFinder(filename = "jason_smko.txt")

    def test_scc_finder_reads_graph(self):
        self.assertIsNotNone(self.scc_finder)

    

    def test_scc_computes_sccs_smko_second_testcase(self):
        scc_finder = SccFinder("jason_smko2.txt")
        
        scc_finder.strongly_connected_components()
        expected_sccs = [3, 3, 2]
        self.assertEqual(scc_finder.scc_list, expected_sccs)

    def test_scc_computes_sccs_smko_third_testcase(self):
        scc_finder = SccFinder("jason_smko3.txt")
        scc_finder.strongly_connected_components()
        expected_sccs = [3, 3, 2]
        self.assertEqual(scc_finder.scc_list, expected_sccs)

    def test_scc_computes_sccs_smko_fourth_testcase(self):
        scc_finder = SccFinder("jason_smko4.txt")
        scc_finder.strongly_connected_components()
        expected_sccs = [3, 3, 2]
        self.assertEqual(scc_finder.scc_list, expected_sccs)

    def test_scc_computes_sccs_smko_last_testcase(self):
        scc_finder = SccFinder("jason_smko_last.txt")
        scc_finder.strongly_connected_components()
        expected_sccs = [3, 3, 2]
        self.assertEqual(scc_finder.scc_list, expected_sccs)

if __name__ == '__main__':
    unittest.main()
