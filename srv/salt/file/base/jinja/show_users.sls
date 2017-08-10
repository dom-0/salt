{% set all_users = {
  'saltmaster': [],
  'minion1': [],
  'minion2': ['wilma'],
  'minion3': ['wilma', 'barney', 'betty'],
  'minion4': ['wilma', 'barney', 'betty', 'fred']
  }
%}
{% set cur_users = salt['grains.filter_by'](all_users, grain='id') %}

show_users:
  cmd.run:
  - name: "echo 'User list is {{ cur_users }}'"
