from validation import *

class Request:
  def __init__(self, type, protocol, src, dst, contents):
    self.type = type
    self.protocol = protocol
    self.src = src
    self.dst = dst
    self.contents = contents

  def is_valid(self):
    if validate_addr( src ) == False:
      return False
    if validate_addr( dst ) == False:
      return False
      
    return validate_req_contents( self.contents )
