
import yaml

device_data = {'serial_into_USBhub_port' : [0, 1, 2, 3, 4, 5, 6, 7],
               'camera_into_serial_port' : [1, 2, 3, 4],
               'USBhub_SN' : ['OX518EFFE1', 'OXCD12637D'],
               'camera_into_USBhub_port' : [0, 1, 2, 3, 4, 5, 6, 7],
               'sbig_SN' : ['83F011167', '83F011791', '83F011639', '83F010801', '83F010774', '83F011758', '83F010771', '83F011810'],
              'birger_SN': ['10858', '14287', '14286', '14285', '13281', '13134', '14284', '13208', '14276'],
              'lens_SN': ['3360000099', '3360000063', '3360000087', '2850000067', '3150000110', '5370000054'],
              'filter_ID': ['r2_1', 'r2_2', 'g2_3', 'g2_4', 'r2_5', 'r2_5', 'r2_6', 'r2_7', 'g2_8', 'g2_9', 'ha1_10', 'ha1_11', 'g2_12', 'ha1_13', 'ha1_14']
              }

with open('serial_management.yaml', 'w') as file:
    yaml.dump(device_data)
    file.write(yaml.dump(device_data))

from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

with open('serial_management.yaml', 'r') as file:
    data = yaml.load(file)

birger_sn = data['birger_SN']

def f(x):
    return x

from IPython.display import display

birger_serial_number = interactive(f, x=birger_sn);

display(birger_serial_number)

birger_SN = birger_serial_number.result

sbig_sn = data['sbig_SN']
sbig_serial_number = interactive(f, x=sbig_sn);

display(sbig_serial_number)

sbig_SN = sbig_serial_number.result

lens_sn = data['lens_SN']
lens_serial_number = interactive(f, x=lens_sn);

display(lens_serial_number)

lens_SN = lens_serial_number.result

filter_ID = data['filter_ID']
filter_ID_code = interactive(f, x=filter_ID);

display(filter_ID_code)

filter_ID = filter_ID_code.result

serial_into_USBhub = data['serial_into_USBhub_port']
serial_into_USBhub_port = interactive(f, x=serial_into_USBhub);

display(serial_into_USBhub_port)

serial_to_USBhub_port = serial_into_USBhub_port.result

camera_into_serial = data['camera_into_serial_port']
camera_into_serial_port = interactive(f, x=camera_into_serial);

display(camera_into_serial_port)

camera_to_serial_port = camera_into_serial_port.result

USBhub = data['USBhub_SN']
USBhub_SN = interactive(f, x=USBhub);

display(USBhub_SN)

USB_hub_SN = USBhub_SN.result

camera_into_USBhub = data['camera_into_USBhub_port']
camera_into_USBhub_port = interactive(f, x=camera_into_USBhub);

display(camera_into_USBhub_port)

camera_to_USBhub_port = camera_into_USBhub_port.result

chosen_data = {'cameras' : [{'hdr_mode' : True,
               'auto_detect' : False,
                             'selected_device' : [{'model' : 'sbig',
                                                    'port' : sbig_SN,
                                                   'filter_ID_code' : filter_ID,
                                                    'focuser' : [{'model' : 'birger',
                                                                  'port' : birger_SN

                                                    }],
                                                    'lens' : [{'model' : 'canon',
                                                               'port' : lens_SN}],
                                                    'USB_hub_serial_number' : USB_hub_SN,
                                                    'camera_into_serial_adaptor_port' : camera_to_serial_port,
                                                    'serial_adaptor_into_USBhub_port' : serial_to_USBhub_port,
                                                   'camera_into_USBhub_port' : camera_to_USBhub_port

                                                              }]
                            }]
              }



output_stream = open("device_info_management.yaml","a")
yaml.dump(chosen_data,output_stream,default_flow_style=False)
output_stream.close()
