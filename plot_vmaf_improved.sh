#!/bin/bash

main() {
    local python_cmd

    # Check for Python3 installation and retrieve the command path
    if ! python_cmd=$(command -v python3 || command -v python); then
        printf "Python is not installed on this system.\n" >&2
        return 1
    fi

    # Execute the Python script
    "$python_cmd" "$(dirname "$(readlink -f "$0")")/plot_vmaf_improved.py"
}

main "$@"
