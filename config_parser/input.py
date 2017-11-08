from configobj import ConfigObj
config = ConfigObj('testconfig.conf')
#
# s = {'p': 1,
#      'a': 1,
#      'c': 1}
# s['invalid'] = []

s = config['ipvSwift']
#s['inactive'] = []
print s
