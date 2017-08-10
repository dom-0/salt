{% set output = salt['cmd.run']('pwd') %}
cmd_output:
  cmd.run:
  - name: "echo 'The present working dir is {{ output }}'"
