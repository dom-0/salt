track_example_tag:
  local.file.append:
  - tgt: minion1
  - arg:
    - /tmp/reactor_example.txt 
    - {{ data }}
