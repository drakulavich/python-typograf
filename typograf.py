#!/usr/bin/env python2
# encoding: utf-8

import xml.etree.ElementTree as ET
import pyperclip
from requests import post

SERVICE_URL = 'http://typograf.artlebedev.ru/webservices/'


def typograf(text):
    template = """<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n'
    <soap:Body>'
        <ProcessText xmlns="{url}">
            <text>{text}</text>
            <entityType>3</entityType>
            <useBr>0</useBr>
            <useP>0</useP>
            <maxNobr>3</maxNobr>
        </ProcessText>
        </soap:Body>
    </soap:Envelope>"""

    # Replace forbidden symbols
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')

    r = post('{url}typograf.asmx'.format(url=SERVICE_URL),
             template.format(url=SERVICE_URL, text=text))

    if r.status_code == 200:
        root = ET.fromstring(r.content)
        return root.findtext('.//{{{url}}}ProcessTextResult'.format(url=SERVICE_URL))
    else:
        return text

if __name__ == '__main__':
    print('clipboard type:', pyperclip._functions)

    # get text from clipboard and convert to <str>
    text = pyperclip.paste().encode('UTF-8')
    # replace text in clipboard
    pyperclip.copy(typograf(text))
    pyperclip.paste()
