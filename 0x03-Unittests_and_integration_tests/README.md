# ALX Backend Python - Unittests and Integration Tests

A comprehensive Python testing project demonstrating professional testing practices using `unittest`, `parameterized`, and `mock`. This repository showcases proper unit and integration testing methodologies for Python utilities and a GitHub API client.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is part of the ALX Backend Python curriculum, focusing on building robust, testable Python applications. It includes utility functions, a GitHub organization client, and comprehensive test suites demonstrating industry-standard testing practices.

## Features

- **Utility Functions**: Helper methods for nested dictionary access, JSON fetching, and result memoization
- **GitHub Client**: Interface for interacting with GitHub organization data
- **Comprehensive Testing**: Full unit and integration test coverage using modern testing patterns
- **Parameterized Tests**: Efficient testing across multiple scenarios with minimal code duplication
- **Mock Testing**: Proper isolation of external dependencies in tests

## Project Structure

```
0x03-Unittests_and_integration_tests/
├── client.py              # GitHub organization client implementation
├── fixtures.py            # Test fixtures and sample data
├── utils.py               # Utility functions and helpers
├── test_client.py         # Integration and unit tests for client
├── test_utils.py          # Unit tests for utility functions
└── __pycache__/          # Python bytecode cache
```

## Requirements

- **Python**: 3.13 or higher
- **Dependencies**:
  - `parameterized` - For parameterized test cases
  - `unittest` - Built-in testing framework
  - `unittest.mock` - Built-in mocking library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AJMKEL/alx-backend-python.git
   cd alx-backend-python/0x03-Unittests_and_integration_tests
   ```

2. **Install dependencies**:
   ```bash
   pip install parameterized
   ```

## Usage

### Utility Functions (`utils.py`)

- **`access_nested_map(nested_map, path)`**: Safely navigate and retrieve values from nested dictionaries
- **`get_json(url)`**: Fetch and parse JSON data from remote URLs
- **`memoize`**: Decorator for caching method results to improve performance

### GitHub Client (`client.py`)

The `GithubOrgClient` class provides methods to interact with GitHub's organization API, enabling retrieval of organization data and repositories.

## Testing

### Running All Tests

Navigate to the project directory and run:

```bash
cd 0x03-Unittests_and_integration_tests
PYTHONPATH=.. python3 -m unittest discover -v
```

### Running Specific Test Modules

**Utils tests**:
```bash
python3 -m unittest test_utils -v
```

**Client tests**:
```bash
python3 -m unittest test_client -v
```

### Test Coverage

- ✅ Unit tests for all utility functions
- ✅ Integration tests for GitHub client
- ✅ Mock tests for external API interactions
- ✅ Parameterized tests for multiple input scenarios
- ✅ Exception handling and edge case coverage

### Example Test Case

```python
from parameterized import parameterized
from utils import access_nested_map
import unittest

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)
```

## Contributing

### Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes and commit**:
   ```bash
   git add .
   git commit -m "Add: descriptive commit message"
   ```

3. **Push to your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Resolving Conflicts

If you encounter merge conflicts during a rebase:

```bash
git status                    # View conflicted files
# Manually resolve conflicts in your editor
git add <resolved_files>      # Stage resolved files
git rebase --continue         # Continue the rebase process
```

## Best Practices

- Always ensure `PYTHONPATH` includes the parent directory when running tests
- Follow PEP 8 style guidelines for Python code
- Write descriptive test names that explain what is being tested
- Use mocks to isolate external dependencies in unit tests
- Keep test cases focused and test one thing at a time

## Notes

- The repository contains production-ready test cases
- All tests are executable and pass successfully
- Mock patterns are used to avoid external API calls during testing
- Parameterized tests reduce code duplication while maintaining comprehensive coverage

---

**Author**: AJMKEL  
**Repository**: [alx-backend-python](https://github.com/AJMKEL/alx-backend-python)  
**Project**: 0x03-Unittests_and_integration_tests
