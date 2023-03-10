import argparse as arg
from sub_file import *
from sub_file import info
from sub_file import details
from sub_file import ssl_info
from sub_file import subdomain

cli= arg.ArgumentParser(description='Web Scanner For Pentester create by A-Coder\nExample: python main.py -i https://www.example.com')
cli.add_argument('-u',type=str,help='set target')
cli.add_argument('-i',type=str, help='see only security header details')
cli.add_argument('-s',type=str,help="see only ssl info")
cli.add_argument('-d',type=str,help="see only subdomain and ip")
args=cli.parse_args()

b=""
if args.u:
    info.info(args.u)
    details.detail(args.u)
    ssl_info.ssld(args.u)
    subdomain.subdomain(args.u)
if args.i:
    details.detail(args.i)
if args.s:
    ssl_info.ssld(args.s)
if args.d:
    subdomain.subdomain(args.d)
else:
    print("Miss Target")


