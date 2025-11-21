## set synchronized panes
CTRL B :
setw synchronize-panes on/off

## capture pane output
tmux capture-pane -t :$WINDOWS.$PANE -pS -
tmux capture-pane -t :0.0 -pS -
