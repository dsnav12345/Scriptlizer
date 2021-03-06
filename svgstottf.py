import sys
import os.path
import json
import fontforge
from PIL import Image

IMPORT_OPTIONS = ('removeoverlap', 'correctdir')

try:
    unicode
except NameError:
    unicode = str

def loadConfig(filename='font.json'):
    with open(filename) as f:
        return json.load(f)

def setProperties(font, config):
    props = config['props']
    lang = props.pop('lang', 'English (US)')
    family = props.pop('family', None)
    style = props.pop('style', 'Regular')
    props['encoding'] = props.get('encoding', 'UnicodeFull')
    if family is not None:
        font.familyname = family
        font.fontname = family + '-' + style
        font.fullname = family + ' ' + style
    for k, v in config['props'].items():
        if hasattr(font, k):
            if isinstance(v, list):
                v = tuple(v)
            setattr(font, k, v)
        else:
            font.appendSFNTName(lang, k, v)
    for t in config.get('sfnt_names', []):
        font.appendSFNTName(str(t[0]), str(t[1]), unicode(t[2]))

def addGlyphs(font, config):
    for k, v in config['glyphs'].items():
        g = font.createMappedChar(int(k, 0))
        # Get outlines
        src = '%s.svg' % k
        if not isinstance(v, dict):
            v = {'src': v or src}
        src = '%s%s%s' % (config.get('input', '.'), os.path.sep, v.pop('src', src))
        g.importOutlines(src, IMPORT_OPTIONS)
        g.removeOverlap()
        # Copy attributes
        for k2, v2 in v.items():
            if hasattr(g, k2):
                if isinstance(v2, list):
                    v2 = tuple(v2)
                setattr(g, k2, v2)

chars=[33, 34, 39, 44, 46, 58, 59, 63, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

def main(src, outfile, name):
    config={ "props":  { 	"ascent": 96, "descent": 32, "em": 128, "encoding": "UnicodeFull", "lang": "English (US)", "family": "{}".format(name), "style": "Regular", "familyname": "{}".format(name), 
                            "fontname": "{}".format(name), "fullname": "{}-Regular".format(name)}
            , "glyphs":{ 	"0x21" : "33.svg",	"0x22" : "34.svg",	"0x27" : "39.svg",	"0x2c" : "44.svg",	"0x2e" : "46.svg",	"0x3a" : "58.svg",	"0x3b" : "59.svg",	"0x3f" : "63.svg",	"0x41" : "65.svg",
                            "0x42" : "66.svg",	"0x43" : "67.svg",	"0x44" : "68.svg",	"0x45" : "69.svg",	"0x46" : "70.svg",	"0x47" : "71.svg",	"0x48" : "72.svg",	"0x49" : "73.svg",	"0x4a" : "74.svg",
                            "0x4b" : "75.svg",	"0x4c" : "76.svg",	"0x4d" : "77.svg",	"0x4e" : "78.svg",	"0x4f" : "79.svg",	"0x50" : "80.svg",	"0x51" : "81.svg",	"0x52" : "82.svg",	"0x53" : "83.svg",
                            "0x54" : "84.svg",	"0x55" : "85.svg",	"0x56" : "86.svg",	"0x57" : "87.svg",	"0x58" : "88.svg",	"0x59" : "89.svg",	"0x5a" : "90.svg",	"0x61" : "97.svg",	"0x62" : "98.svg",
                            "0x63" : "99.svg",	"0x64" : "100.svg",	"0x65" : "101.svg",	"0x66" : "102.svg",	"0x67" : "103.svg",	"0x68" : "104.svg",	"0x69" : "105.svg",	"0x6a" : "106.svg",	"0x6b" : "107.svg",
                            "0x6c" : "108.svg",	"0x6d" : "109.svg",	"0x6e" : "110.svg",	"0x6f" : "111.svg",	"0x70" : "112.svg",	"0x71" : "113.svg",	"0x72" : "114.svg",	"0x73" : "115.svg",	"0x74" : "116.svg",
                            "0x75" : "117.svg",	"0x76" : "118.svg",	"0x77" : "119.svg",	"0x78" : "120.svg",	"0x79" : "121.svg",	"0x7a" : "122.svg"}
            , "sfnt_names": [ 	["English (US)", "Copyright", "Copyright (c) 2014 by Nobody"], ["English (US)", "Family", "{}".format(name)], ["English (US)", "SubFamily", "Regular"], 
                                ["English (US)", "UniqueID", "{} 2021-05-21".format(name)], ["English (US)", "Fullname", "{} Regular".format(name)], ["English (US)", "Version", "Version 001.000"], 
                                ["English (US)", "PostScriptName", "{}-Regular".format(name)] ]
            , "input": "{}".format(src)
            , "# vim: set et sw=2 ts=2 sts=2:": False
    }

    font = fontforge.font()
    setProperties(font, config)
    addGlyphs(font, config)
    for char in chars:
        im=Image.open('Media/{}/images/{}.png'.format(name, char))
        w, h=im.size
        font[char].width=w
    font.generate(outfile)

if __name__ == '__main__':
    main('config.json')

# vim: set filetype=python:
