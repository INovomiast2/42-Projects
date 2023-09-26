#!/bin/bash

if [ $# -lt 1 ]; then
    echo No arguments were passed!!;
else
    #If parammeters were passed:Show Params
    if [ $# -eq 3 ]; then
        echo $*
    fi
    #If +3 parammeters:Show max args ERROR!
    if [ $# -gt 3 ]; then
        echo MAX 3 ARGUMENTS!!;
    fi

fi