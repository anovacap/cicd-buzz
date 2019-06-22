# cicd-buzz
---
## Description
* How to build a modern CI/CD pipeline
* https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b
* Write a little Python program (not Hello World)
* Add some automated tests for the program
* Push your code to GitHub
* Setup Travis CI to continuously run your automated tests
* Setup Better Code Hub to continuously check your code quality
* Turn the Python program into a web app
* Create a Docker image for the web app
* Push the Docker image to Docker Hub
* Deploy the Docker image to Heroku
## Files
File | Task
---|---
buzz/generator.py | generates a sentence about CICD
tests/test_generator.py | the tests for generator.py
.travis.yml | Travis CI setup instruction
Directory Name | Description
---|---
cicd-buzz | root directory of project travis files
cicd-buzz/buzz | main Python file
cicd-buzz/tests | test file for generator - Python
## Author
Damon Nyhan