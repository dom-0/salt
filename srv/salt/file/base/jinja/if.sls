{% set my_bool = true %}
jinja_if:
  cmd.run:
  {% if my_bool %}
  - name: 'echo "Het is waar"'
  {% else %}
  - name: 'echo "Nee! niet waar"'
  {% endif %}
