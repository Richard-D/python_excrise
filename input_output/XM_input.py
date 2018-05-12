from lxml import etree
from lxml import objectify
parsed = objectify.parse(open(""))
root = parsed.getroot()
print(root)