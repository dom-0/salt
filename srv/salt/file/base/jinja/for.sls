{% set my_list = ['a', 'b', 'c'] %}
{% for i in my_list %}
jinja_for_{{ i }}:
  cmd.run:
  - name: 'echo "The value of i is {{ i }}"'
{% endfor %}
