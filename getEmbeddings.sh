#!/bin/bash
th translate.lua -dump_input_encoding 1 -model ~/Downloads/onmt_baseline_wmt15-all.en-de_epoch13_7.19_release.t7 -src data/random.txt -output pred.txt