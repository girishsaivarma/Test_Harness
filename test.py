import subprocess
import sys
import os

def run_test(test_script, input_file, expected_output_file):
    # Run the utility script with the input file and capture the output
    with open(input_file, 'r') as infile, open(expected_output_file, 'r') as expectedfile:
        try:
            # Execute the script using the Python interpreter
            result = subprocess.run(
                [sys.executable, test_script],
                stdin=infile,
                text=True,
                capture_output=True
            )
            expected_output = expectedfile.read()
            return (result.stdout == expected_output, result.stderr, result.returncode)
        except subprocess.CalledProcessError as e:
            return (False, e.stderr, e.returncode)

def main(tests_dir, test_script):
    # Find all test input files
    input_files = [f for f in os.listdir(tests_dir) if f.endswith('_input.txt')]
    
    # Run each test
    for input_file in input_files:
        test_name = input_file[:-10]  # remove '_input.txt'
        expected_output_file = f"{test_name}_expected.txt"
        
        # Check if the expected output file exists
        if not os.path.isfile(os.path.join(tests_dir, expected_output_file)):
            print(f"Expected output file for {test_name} does not exist. Skipping.")
            continue
        
        print(f"Running test: {test_name}")
        success, stderr, exit_code = run_test(
            test_script,
            os.path.join(tests_dir, input_file),
            os.path.join(tests_dir, expected_output_file)
        )
        
        if success:
            print(f"Test {test_name} passed!")
        else:
            print(f"Test {test_name} failed!")
            print(f"STDERR: {stderr}")
            print(f"Exit Code: {exit_code}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python test_harness.py <tests_dir> <test_script>")
        sys.exit(1)
    
    tests_dir = sys.argv[1]
    test_script = sys.argv[2]
    main(tests_dir, test_script)
