### CSVProcessor

CSVProcessor is a fun project where I practice building some command line tools in python.

CSVProcessor takes a CSV with the following format:

|Store Name | Amount | AccountNumber|
| ------------- |:-------------:| -----:|

##### Command Inputs
```--inputPath```

_Where is the CSV located?_

```--outputPath```

_Where should we save our results?_

##### How to run:

Install python3

```brew install python```

Run CSVProcessor.py

```python3 CSVProcessor.py --inputPath ~/Documents/Data/lineitems.csv --outputPath ~/Documents/Data/info.txt```

##### How to install:

Install pip, then:

```pip install e .```

