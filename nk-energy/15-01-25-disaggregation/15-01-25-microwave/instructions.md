# Instructions for Obtaining Microwave information
The averaging script is called `avg.py`. Just pass a file with one number per
row to `stdin` and it will compute the average of said rows.

## Wattcher
To obtain only `Watt` or `Current` data, use:
`awk '/Current/' filename >data.tmp` where Current is either Current or Watt
and filename is one of the log files in this directory.

### Off
`microwave-wattcher-off.log`

### On
Data is fonud in `microwave-wattcher-on.log`


## Nikola
### Off
`microwave-nk-off.txt`

### On
`microwave-nk-on.txt`
