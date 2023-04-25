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

### How to use it

If you visit http://127.0.0.1:5000/ you will see Bootstrap 4 UI for application where you can perform 3 available operations

 - With date (formatted YYYY-MM-DD) and a currency code get its average exchange rate.
 - With currency code and the number of last quotations N, get two days with max and min exchange rate in given interval.
 - With currency code and the number of last quotations N, provide the major difference between the buy and ask rate, with a date of day.

<img src="static/ui.PNG" alt="Alt text" title="Optional title">


### Tests

Once you have container running on yor machine, open new CMD window and navigate to place where downloaded repo resides.
Then type:
```
$ python tests.py
```
You should see a message that all 8 tests were performed correctly. 
!!! Note that tests were made as for 25.04.2023 and after some time, operations 
test_min_max_avg_value and test_major_diff might present other values, as they operate on constantly changing data !!!

