import os
import json
import xml.etree.ElementTree as ET
import argparse

print "run: parser.py -h for help."
print "\n"

parser = argparse.ArgumentParser(
	description = "two arguments: messages.xml, messages.json")
parser.add_argument(
	"-x",
	"--xml_messages",
	help = "Path to SMS messages in XML format to be parsed.")
parser.add_argument(
	"-j",
	"--json_messages",
	help = "Path to Facebook messages in JSON format to be parsed.")
parser.add_argument(
	"-o",
	"--output_path",
	help = "Path to output file (default: current directory).",
	default = "./")

args = parser.parse_args()
xml_messages = args.xml_messages
json_messages = args.json_messages
out = args.output_path
outfile = os.path.join(out, "plain.txt")
to_write = open(outfile, "w")

if json_messages is not None:
	with open(json_messages) as JSON:
		json_obj = json.load(JSON)
		msgs = json_obj["messages"]
		for msg in msgs:
			try:
				to_write.write(msg["content"].encode("ascii", "ignore") + "\n")
			except KeyError:
				continue
	print "finished parsing and printing JSON messages..."

if xml_messages is not None:
	xml_obj = ET.parse(xml_messages)
	root = xml_obj.getroot()
	for child in root.iter("sms"):
		to_write.write(child.attrib["body"].encode("ascii", "ignore") + "\n")
	print "finished parsing and printing XML messages..."
print "done!"

