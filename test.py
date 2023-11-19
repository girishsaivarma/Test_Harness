import subprocess
import os
import unittest
import sys
import json

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
        elif program == 'ini2json':
            # For 'ini2json', the content should be passed through STDIN
            process = subprocess.run(cmd, input=input_content, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            self._assert_process_output(process, expected_file, test_name, program, use_args)
            return

        elif program == 'wc' and not use_args:
            # For 'wc', when use_args is False, the content should be passed through STDIN
            process = subprocess.run(cmd, input=input_content, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            self._assert_process_output(process, expected_file, test_name, program, use_args)
            return

        # For other programs, run the command normally
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self._assert_process_output(process, expected_file, test_name, program, use_args)

    def _assert_process_output(self, process, expected_file, test_name, program, use_args):
        # Check if the process exited with a non-zero status
        self.assertEqual(process.returncode, 0, f"Program exited with {process.returncode}. Error: {process.stderr}")

        # Get the actual output from the program
        actual_output = process.stdout.strip()
        
        # Debugging: Print the actual output
        print(f'Actual output for {test_name}: {actual_output}')

        # Compare the actual output to the expected output
        with open(expected_file, 'r') as f:
            expected_output = f.read().strip()

        # Debugging: Print the expected output
        print(f'Expected output for {test_name}: {expected_output}')

        if program == 'ini2json':
            # For 'ini2json', we need to compare JSON structures
            actual_json = json.loads(actual_output)
            expected_json = json.loads(expected_output)
            self.assertDictEqual(actual_json, expected_json, f'Failed test: {test_name} for {program} with {"arguments" if use_args else "stdin"}')
        else:
            # For other programs, compare output as text
            self.assertEqual(actual_output, expected_output, f'Failed test: {test_name} for {program} with {"arguments" if use_args else "stdin"}')

    def test_programs(self):
        # Test 'wc' program without command line arguments
        self.run_test('wc', 'test', False)
        self.run_test('wc', 'test', True)

        # Test 'gron' program with command line arguments
        self.run_test('gron', 'test', True)
        self.run_test('gron', 'test', False)

        # Test 'ini2json' program without command line arguments
        self.run_test('ini2json', 'test', False)
        self.run_test('ini2json', 'test', True)

if __name__ == '__main__':
    unittest.main()
