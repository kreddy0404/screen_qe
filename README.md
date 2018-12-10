# Instructions

1. Build this docker image

```shell
git clone https://github.com/andres-lowrie/screen-qe.git
cd screen-qe
docker build -t screen-qe .
```


2. Run `bash` as the command with an iteractive tty to get into the image:

```
docker run --rm -it screen-qe /bin/bash
```


3. Once you're inside the docker container you should see the following files:

```
Dockerfile
README.md
main.py
tasks.py
```


# Exercise

1. Write an automated test suite for the application


The following is the spec of what the application should do

```gherkin
Feature: Calculate average
  Scenario: Happy Path
    Given the applicaton can read the csv files in `/usr/src/data`
    When the cli application is ran like `./main.py --avg`
    Then the correct average number of fields across all csv files should be output to the screen


Feature: Word Count
  Scenario: Happy Path
    Given the applicaton can read the csv files in `/usr/src/data`
    And can write to `/usr/src/app/`
    When the cli application is ran like `./main.py --word_count`
    Then the csv file  `/usr/src/app/wordcount.csv` should be created
    And it should contain 2 fields named `value,count`
    And the field `value` shold contain every unique word in all the csv files
    And the field `count` should contain the number of times a word (value) appears in any of the csv file


Feature: Row Count
  Scenario: Happy Path
    Given the applicaton can read the csv files in `/usr/src/data`
    When the cli application is ran like `./main.py --row_count`
    Then the total number of rows in all the csv files should be output to the screen
```

2. Create a Pull Request with your code for review

**You're free to use whatever language or framework you want just as long as
you include the instructions on how to run your code in the Docker image in
your Pull Request. (Bonus points if you modify the `Dockerfile` instead)**
