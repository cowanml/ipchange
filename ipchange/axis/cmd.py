import argparse
import os
import sys
import ipaddress
import ipchange.moxa

sys.tracebacklimit = 0


def axis_base_argparser(description):
    parser = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        description=description
    )

    parser.add_argument(
        'AXIS Webcam address/hostname',
        metavar='host', type=str,
        help='Address or Hostname of the AXIS Webcam to change'
    )

    parser.add_argument(
        '-u', '--username', dest='username', action='store',
        help='Username of the AXIS Webcam to connect to',
        default=None
    )

    parser.add_argument(
        '-p', '--password', dest='password', action='store',
        help='Password of the AXIS Webcam to connect to',
        default=None
    )

    return parser


def axis_change_ip():
    parser = axis_base_argparser('Change IP Addresses of AXIS Webcam')

    parser.add_argument(
        'New IP Address',
        metavar='address', type=ipaddress.ip_address,
        help='New IP Address'
    )

    parser.add_argument(
        'New Netmask',
        metavar='netmask', type=ipaddress.ip_address,
        help='New Netmask'
    )

    parser.add_argument(
        'New Gateway',
        metavar='gateway', type=ipaddress.ip_address,
        help='New Gateway'
    )

    args = vars(parser.parse_args())

    # Now run the set routine

    axis = ipchange.axis.AxisWebcam(
        args['AXIS Webcam address/hostname'],
        username=args['username'],
        password=args['password']
    )

    axis.set_ipaddr(
        str(args['New IP Address']),
        str(args['New Netmask']),
        str(args['New Gateway'])
    )

    return 0


def axis_change_passwd():

    parser = axis_base_argparser('Change Password of AXIS Webcam')

    parser.add_argument(
        'Username to change',
        metavar='username', type=str,
        help='Username of the user to change password for'
    )

    parser.add_argument(
        'Password to change',
        metavar='host', type=str,
        help='New password for given user'
    )

    args = vars(parser.parse_args())

    # Now run the set routine

    axis = ipchange.axis.AxisWebcam(
        args['AXIS Webcam address/hostname'],
        username=args['username'],
        password=args['password']
    )

    axis.change_passwd(
        username=args['Username to change'],
        password=args['Password to change']
    )

    return 0
