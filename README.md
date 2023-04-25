# Internship NBP API App

An app written with Flask framework providing certain data from public NBP API 

### How to run app

Clone the git repository
```
$ git clone https://github.com/o-serafin/dynatrace_2023
```
Enter project directory and build docker image
```
$ cd dynatrace_2023
$ docker build --tag python-docker . 
```
Run container with:
```
$ docker run -d -p 5000:5000 python-docker
```
Visit http://127.0.0.1:5000/ or localhost:5000 in your local browser

### Tests

Once you have container running on yor machine, open new CMD window and navigate to place where downloaded repo resides
Then type
```
$ python tests.py
```
You should see a message that all 8 tests were performed correctly
