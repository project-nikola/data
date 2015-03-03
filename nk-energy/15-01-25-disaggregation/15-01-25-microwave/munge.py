#!/usr/bin/env python3

with open('data.tmp') as f:
    data = f.readlines()
    avg = sum(float(s.strip()) for s in data) / len(data)
    print(avg)
