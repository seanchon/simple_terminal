import os
from simple_terminal import Terminal
import unittest


class ChangeDirectoryTestCase(unittest.TestCase):
    """Tests that 'cd' works as expected."""
    def setUp(self):
        os.chdir(os.path.expanduser('~'))
        self.home_directory = os.getcwd()

    def test_current_working_directory(self):
        with Terminal() as t:
            self.assertEqual(t.command('pwd')[0], self.home_directory)

    def test_create_and_change_to_relative_directory_and_back(self):
        with Terminal() as t:
            t.command('mkdir temp')
            self.assertTrue('temp' in t.command('ls'))
            t.command('cd temp')
            self.assertEqual(self.home_directory + '/temp', t.command('pwd')[0])
            t.command('cd ..')
            self.assertEqual(self.home_directory, t.command('pwd')[0])

    def test_change_to_home_directory(self):
        with Terminal() as t:
            t.command('mkdir -p temp/temp')
            self.assertEqual(self.home_directory + '/temp/temp', t.command('cd temp/temp')[0])
            self.assertEqual(self.home_directory, t.command('cd ~')[0])
            self.assertEqual(self.home_directory + '/temp/temp', t.command('cd ~/temp/temp')[0])
            self.assertEqual(self.home_directory, t.command('cd ../..')[0])

    def test_change_to_relative_directory(self):
        with Terminal() as t:
            t.command('mkdir -p temp/temp')
            self.assertEqual(self.home_directory + '/temp/temp', t.command('cd temp/temp')[0])
            self.assertEqual(self.home_directory, t.command('cd ~')[0])
            self.assertEqual(self.home_directory + '/temp/temp', t.command('cd ~/temp/temp')[0])

    def tearDown(self):
        with Terminal() as t:
            t.command('rm -rf ~/temp')


class ContextManagerTestCase(unittest.TestCase):
    def setUp(self):
        with Terminal() as t:
            t.command('cd ~')
            self.home_directory = os.getcwd()

    def test_create_and_change_to_relative_directory_and_back(self):
        with Terminal() as t:
            t.command('mkdir temp')
            self.assertTrue('temp' in t.command('ls'))
            t.command('cd temp')
            self.assertEqual(self.home_directory + '/temp', t.command('pwd')[0])
            t.command('cd ..')
            self.assertEqual(self.home_directory, t.command('pwd')[0])

    def tearDown(self):
        with Terminal() as t:
            t.command('rm -rf ~/temp')

if __name__ == '__main__':
    unittest.main()
