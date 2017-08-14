def enx(name):
 return_dict = { 'name': name, 'changes': {}, 'result': False, 'comment': '' }

 if __opts__['test'] == True:
   return_dict['result'] = None
   return_dict['comment'] = "This is a test run Hopefully it worked, {}".format(name)
   return return_dict

 return_dict['comment'] = "Hopefully it worked {}".format(name)
 return_dict['changes'] = { 'contents': {
   'old': "No Name",
   'new': name
   }
 } 
 return_dict['result'] = True
 return return_dict
