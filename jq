# list possible paths
jq -c 'path(..)|[.[]|tostring]|join("/")'

# list unique keys
jq -n '[inputs | keys[]] | unique' FILE
