{% from "jinja/some_vars.jinja" import list1 as list_of_bogus with context %}
{% for i in list_of_bogus %}
jinja_forloop{{ i }}:
    cmd.run:
      - name: 'echo "The value of i is {{ i }}"'
{% endfor %}
