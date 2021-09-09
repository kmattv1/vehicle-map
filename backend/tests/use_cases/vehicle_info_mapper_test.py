import unittest


class TestVehicleInfoMapper(unittest.TestCase):
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tear down")

    def test_palace_holder(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
