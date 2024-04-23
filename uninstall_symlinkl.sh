#!/bin/bash

main() {
    local link_name="plot_vmaf_improved"
    local paths=("/usr/local/bin" "/usr/bin" "$HOME/bin" "$HOME/.local/bin")
    local found_path=""
    local response

    # Check each path for the existence of the symlink and prompt for its removal
    for path in "${paths[@]}"; do
        if [[ -L "$path/$link_name" ]]; then
            printf "Found symlink in '%s'. Do you want to remove it? [y/N]: " "$path"
            read -r response
            if [[ "$response" =~ ^[Yy] ]]; then
                if rm "$path/$link_name"; then
                    printf "Symlink removed successfully from '%s'.\n" "$path"
                    return 0
                else
                    printf "Failed to remove the symlink from '%s'.\n" "$path" >&2
                    return 1
                fi
            fi
            found_path="$path"
            break
        fi
    done

    if [[ -z "$found_path" ]]; then
        printf "No symlink named '%s' found in the checked directories.\n" "$link_name"
        return 1
    fi
}

main "$@"
