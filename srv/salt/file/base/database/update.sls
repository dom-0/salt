/tmp/data.txt:
  file.managed:
    - source: salt://database/data.template
    - user: root
    - group: root
    - mode: 644
    - template: jinja
