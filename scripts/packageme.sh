#!/bin/bash

function changeToProjectRoot {

    export areHere=`basename ${PWD}`
    if [[ ${areHere} = "scripts" ]]; then
        cd ..
    fi
}

changeToProjectRoot

clear

# python3 setup.py sdist bdist_wheel
python3 -m build --sdist --wheel

# Check package
twine check dist/*
