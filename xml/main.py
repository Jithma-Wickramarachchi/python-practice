import xml.etree.ElementTree as ET

tree = ET.parse('vehical.xml')
root = tree.getroot()

# 'tree' stores object of element tree
print(tree)

# 'root' stores the root of the xml tree.
# which means the parent element
print(root)

# this returns tag of the root element
print(root.tag)

# Prints attribute of the element.
# In this case, It hasn't.
print(root.attrib)

# root saves values like an array.
for child in root:
    print(child.tag, child.attrib)
# So we also can retrieve them by indexes.
print(root[0][1].text)
print(root[1][1].text)

# findAll() and find() can be used to search data
for element in root.findall('vehicle'):
    reg_no = element.find('registration_no').text
    company = element.find('make').text
    print(reg_no, company)

# we can change values by iterating using iter()
for element in root.iter(tag='make'):
    newMake = 'nissan'
    element.text = newMake

# write them using root.write()
tree.write('output.xml')

# We can create a xml structure like this
# And print it using .dump()
a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(a, 'd')
ET.dump(a)