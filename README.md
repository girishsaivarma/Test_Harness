# Project 1: Test Harness

## Personal Information

- Name: [Your Name]
- Stevens Login: [Stevens ID]

## Repository URL
https://github.com/girishsaivarma/Test_Harness.git

## Time Spent

Approximately 20 hours spent on this project.

## Utilities Overview

This repository contains Python implementations of command-line utilities with automated testing via a test harness.

### wc.py

Python equivalent of Unix's `wc`. It provides line, word, and character counts in text.

### gron.py

Flattens JSON objects for easier parsing and searching.

### ini2json.py

Converts INI files to a JSON format.

## Testing Approach

The `test.py` script serves as a test harness, automating the verification of utility outputs against expected results specified in `.out` files for corresponding `.in` input files. The harness supports a comprehensive range of tests, including edge cases and typical usage scenarios.

## Known Bugs/Issues

No known issues. The utilities are currently functioning as expected.

## Difficult Issues and Resolutions

A challenging issue involved the `ini2json.py` utility, which initially failed to properly handle quotation marks within INI files. This led to discrepancies in the JSON output where string values were enclosed in an extra set of quotes. The resolution involved modifying the utility to strip extraneous quotes from the parsed INI values, ensuring the output JSON matched the expected format precisely.

## Implemented Extensions

- **wc.py**: Added command-line flag functionality to selectively count lines, words, or characters.
- **gron.py**: Improved error handling to provide meaningful feedback on JSON parsing errors.
- **ini2json.py**: Enhanced the utility to support both standard input and file input, accommodating a wider range of use cases.

## How You Will Be Graded

Your grade will be based on the following criteria:
- **30%** Baseline behavior of your programs.
- **30%** Thoroughness and accuracy of your `README.md`.
- **30%** Implementation and demonstration of the chosen extensions (10% each).
- **10%** Continuous Integration setup demonstrating all tests passing with a green build at the time of submission.


