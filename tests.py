import os
from simple_terminal import Terminal
import unittest


class ChangeDirectoryTestCase(unittest.TestCase):
    """Tests that 'cd' works as expected."""
    def setUp(self):
        self.t = Terminal()
        os.chdir(os.path.expanduser('~'))
        self.home_directory = os.getcwd()

    def test_current_working_directory(self):
        self.assertEqual(self.t.command('pwd')[0], self.home_directory)

    def test_create_and_change_to_relative_directory_and_back(self):
        self.t.command('mkdir temp')
        self.assertTrue('temp' in self.t.command('ls'))
        self.t.command('cd temp')
        self.assertEqual(self.home_directory + '/temp', self.t.command('pwd')[0])
        self.t.command('cd ..')
        self.assertEqual(self.home_directory, self.t.command('pwd')[0])

    def test_change_to_home_directory(self):
        self.t.command('mkdir -p temp/temp')
        self.assertEqual(self.home_directory + '/temp/temp', self.t.command('cd temp/temp')[0])
        self.assertEqual(self.home_directory, self.t.command('cd ~')[0])
        self.assertEqual(self.home_directory + '/temp/temp', self.t.command('cd ~/temp/temp')[0])

    def tearDown(self):
        self.t.command('rm -rf ~/temp')

if __name__ == '__main__':
    unittest.main()
