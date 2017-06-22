# list possible paths
jq -c 'path(..)|[.[]|tostring]|join("/")'
