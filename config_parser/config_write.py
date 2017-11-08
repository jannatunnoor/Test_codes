from configobj import ConfigObj
config = ConfigObj()
config.filename = 'testconfig.conf'
#
config['keyword1'] = 1
config['keyword2'] = 2
#
config['section1'] = {}
config['section1']['keyword3'] = 3
config['section1']['keyword4'] = 4
#
section2 = {
    'keyword5': 5,
    'keyword6': 6,
    'sub-section': {
        'keyword7': 7
        }
}
config['section2'] = section2
#
config['section3'] = {}
config['section3']['keyword 8'] = [8, 9, 10]
config['section3']['keyword 9'] = [11, 12, 13]
#
config.write()