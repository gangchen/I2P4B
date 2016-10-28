#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count(seq):
    counts = {'A':0, 'C':0,'G':0,'T':0,'N':0}
    for base in seq:
        if base in counts.keys():
            counts[base] += 1

    return(counts)
