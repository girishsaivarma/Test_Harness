import subprocess
import os
import unittest
import sys  # Import the sys module

class TestProgram(unittest.TestCase):
    test_dir = './test'
    prog_dir = './prog'

    def run_test(self, program, test_name, use_args):
        input_file = f'{self.test_dir}/{program}.{test_name}.in'
        expected_file = f'{self.test_dir}/{program}.{test_name}' + ('.arg.out' if use_args else '.out')
        cmd = [sys.executable, os.path.join(self.prog_dir, f'{program}.py')]

        # Read the input content
        with open(input_file, 'r') as f:
            input_content = f.read()

        if program == 'gron':
            # If 'gron', expect a JSON file as an argument
            cmd.append(input_file)
        elif program == 'wc' and not use_args:
            # For 'wc', when use_args is False, the content should be passed through STDIN
            process = subprocess.run(cmd, input=input_content, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            self._assert_process_output(process, expected_file, test_name, program, use_args)
            return

        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self._assert_process_output(process, expected_file, test_name, program, use_args)

    def _assert_process_output(self, process, expected_file, test_name, program, use_args):
        # Check if the process exited with a non-zero status
        self.assertEqual(process.returncode, 0, f"Program exited with {process.returncode}. Error: {process.stderr}")

        # Compare the actual output to the expected output
        actual_output = process.stdout.strip()
        with open(expected_file, 'r') as f:
            expected_output = f.read().strip()

        self.assertEqual(actual_output, expected_output, f'Failed test: {test_name} for {program} with {"arguments" if use_args else "stdin"}')

    def test_programs(self):
        # Test 'wc' program without command line arguments
        self.run_test('wc', 'test1', False)

        # Test 'gron' program with command line arguments
        self.run_test('gron', 'test1', True)

        # Add tests for other programs as needed, with the correct use_args setting

if __name__ == '__main__':
    unittest.main()
