# Simple cinema manager

Toy python project to experiment on with code coverage.

## Files

- src/
  - cinema.py: Represents the entire cinema
  - hall.py: Represents a hall where movies are played
  - main.py: Shows example code of how to use the various classes
  - movie.py: Represents a movie that can be played
  - utils.py: Provides useful functions used by the other classes
- test/
  - test_cinema.py: Tests the cinema.py class
  - test_hall.py: Tests the hall.py class
  - test_movie.py: Tests the movie.py class

## Installation

Run the following command to install all requirements:
```
pip install -r requirements.txt
```

## Running the tests

To run all tests in the testing suite, use the command:

```
python3 -m unittest discover
```

## Code coverage

To obtain the current code coverage of the tests, use the command:

```
coverage run --branch -m unittest discover
coverage report
```

## Mutation score

To obtain the mutation score for a specific test file, use the command:

```
mut.py --target src.[MODULE NAME] --unit-test test.[TEST FILENAME]
```

For example:
```
mut.py --target src.hall --unit-test test.test_hall
```

To get the mutation score for the hall testing suite.