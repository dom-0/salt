import os

def enforce_tmp(name, contents=None):
  """
  Enforce a temp file has the desired contents.

  name
    The name of the file to change (Under /tmp)

  contents
    The value you will be storing

  """

  return_dict = {
    'name': name,
    'changes': {},
    'result': False,
    'comment': ''
  }

  tmp_file = os.path.join("/tmp", name)

  file_ok = False
  contents_ok = False
  file_contents = None

  if os.path.isfile(tmp_file):
    file_ok = True
    with open (tmp_file, 'r') as FH:
      file_contents = FH.read()
      file_contents = file_contents.rstrip('\n')

  if file_contents == contents:
    contents_ok = True

  comments = ""

  if file_ok:
    comments += "File Exists ({})\n".format(tmp_file)
  else:
    comments += "File Created ({})\n".format(tmp_file)
  if content_ok:
    comments += "Contents Correct ({})\n".format(file_contents)
  else:
    comments += "Contents Changed ({})\n".format(file_contents)
  
  return_dict['comment'] = comments

  if __opts__['test'] == True:
    return_dict['result'] = None

    if not content_ok:
      return_dict['changes'] = {
        'contents': { 'old': file_contents, 'new': contents } 
      } 
    return return_dict


  if not content_ok:
    with open (tmp_file, 'w') as fp:
      contents += "\n"
      fp.write(contents)

    return_dict['result'] = True
    return_dict['changes'] = {
      'contents': {
        'old': file_contents,
        'new': contents
      }
    }

  else:
    return_dict['changes'] = {}
    return_dict['result'] = True

  return return_dict 
