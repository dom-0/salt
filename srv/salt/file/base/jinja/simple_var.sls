{% set my_dict = {'first': 'value 1', 'second': 'value 2'} %}
jinja_var:

  cmd.run:
  - name: echo "Output of list is {{ my_dict.keys() }}"
