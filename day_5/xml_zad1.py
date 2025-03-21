# xml
# xml używa tagów

from xml.dom import minidom

root = minidom.Document()
xml = root.createElement('root')
root.appendChild(xml)

productChile = root.createElement('product')
productChile.setAttribute('name', "GFG")
xml.appendChild(productChile)

xml_str = root.toprettyxml(indent="\t")
print(xml_str)
# <?xml version="1.0" ?>
# <root>
# 	<product name="GFG"/>
# </root>
