# kudu_csv_processor
> kudu export/import tool for CSV format

## installation
use Python3.6.6

need : kudu-python (1.2.0)


## usage

usage: python3.6 kudu_csv_export.py [-h] -i IP -t TABLE -f FILE [-p PORT]

optional arguments:

| index             | value                         |
|-------------------|-------------------------------|
|-h, --help         |show this help message and exit|
|-i IP, --ip IP     |target kudu ip address         |
|-t TABLE, --table TABLE  |target kudu table name   | 
|-f FILE, --file FILE     |export file name         |
|-p PORT, --port PORT     |target kudu port         |
              
## update log

* 0.0.1
    * added
    * kudu export csv add

## infomation
Choi JongHyeok - opendev.choi@gmail.com

[https://github.com/opendev-choi](https://github.com/opendev-choi)
