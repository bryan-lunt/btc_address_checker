# Installation
This program currently only works in Python 2.7, due to incompatibilities in libraries it requires.

To install the requirements

```shell
pip install -r requirements.txt
```

# Running

to run the program, type

```shell
python simple_checker.py inputfile.txt outputfile.txt
```

## Options
If you use "-" for the input or output files, the program will use stdin or stdout, respectively.

# Output

Output will be in the tab-separated format `<address>	<TRUE or FALSE>	<BALANCE>` with the balance expressed in BTC.
So, a balance line like

```
1DS57SoKe2bRxBuR2ayjjz3tb5JFxsdZEk      TRUE    0.06800000
```

means that that address has a non-zero balance of 0.068 BTC.

Previously, the balance was expressed in Satoshis, and future versions may make this an optional behaviour.

# Required Libraries

All requirements are in the `requirements.txt` file.

The software requires that the blockchain.info client library be installed.

- https://github.com/blockchain/api-v1-client-python

That requires that the `enum` library be installed.
