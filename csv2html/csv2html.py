#!/usr/local/bin/python3

import sys

def main():
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line, color)
            count += 1
        except EOFError:
            break
    print_end()

def print_start():
    print("<table border='1'>")

def print_end():
    print("</table>")

def print_line(line, color):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            field = escape_html(field)
            print("<td>{0}</td>".format(field))
    print("</tr>")

def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted field
                quote = c
            elif quote == c: # end of quoted field
                quote = None
            else:
                field += c # different quote inside quoted string (i.e. 'some "test" string')
            continue
        if quote is None and c == ",": # end of field
            fields.append(field)
            field = ""
        else: # accumulating a field
            field += c
    if field:
        fields.append(field) # add the final field (no "," to check for)
    return fields

def escape_html(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text

main()
