import pandas as pd
# noinspection PyPep8Naming
import xml.etree.ElementTree as ET


# gathers tenant, unit, and tv type from user
def get_user_input():
    tenant_name = input("Enter tenant name: ")
    unit = input("Enter unit: ")
    tv_type = input("Enter tv type: ")
    return tenant_name, unit, tv_type


# reads the room numbers from a csv file
def read_room_numbers(csv_file_path):
    df = pd.read_csv(csv_file_path)
    room_numbers = df['room'].tolist()
    return room_numbers


# creates the xml file that contains the tenant, unit, tv type, and a list of the room numbers
def create_xml(tenant_name, unit, tv_type, room_numbers):
    root = ET.Element('root')
    ET.SubElement(root, 'TENANTNAME').text = tenant_name
    ET.SubElement(root, 'UNIT').text = unit
    ET.SubElement(root, 'TV').text = tv_type

    room_list = ET.SubElement(root, 'roomList')
    for room in room_numbers:
        ET.SubElement(room_list, 'room').text = room

    tree = ET.ElementTree(root)
    return tree


# Main function
def main():
    tenant_name, unit, tv_type = get_user_input()
    csv_file = 'rooms.csv'
    room_numbers = read_room_numbers(csv_file)
    tree = create_xml(tenant_name, unit, tv_type, room_numbers)

    # Save the XML to a file
    tree.write('output.xml', encoding='utf-8', xml_declaration=True)

    print("XML file 'output.xml' has been created successfully.")


if __name__ == '__main__':
    main()
    print("Thank You!")
