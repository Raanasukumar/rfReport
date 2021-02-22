import xml.etree.ElementTree as ET
import subprocess
import sys
import argparse
from prettytable import PrettyTable
parser=argparse.ArgumentParser()
parser.format_help()
parser.add_argument('--xmlfile','-x', help="enter pma saps with extension")
args = parser.parse_args()
xmlfile=str(args.xmlfile)
tree=ET.parse(xmlfile)
root=tree.getroot()
statistics_list=[]
myTable = PrettyTable(["Suite","Pass","Fail"])
for statistics in root.findall("./statistics/suite/"):
        statistics_list.append(statistics.attrib)
for stats in statistics_list:
        myTable.add_row([stats['name'],stats['pass'],stats['fail']])
print(myTable)
