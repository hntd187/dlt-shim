import unittest

import dlt_shim as dlt

class TestDltShim(unittest.TestCase):
    def test_shim(self):
        @dlt.table()
        def table_test():
            return None


if __name__ == '__main__':
    unittest.main()
