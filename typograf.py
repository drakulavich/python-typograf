#!/usr/bin/env python
# encoding: utf-8

import xml.etree.ElementTree as ET
import pyperclip
from requests import post

SERVICE_URL = 'http://typograf.artlebedev.ru/webservices/'


def typograf(text):
    """
    Sends text to typograf webservice.
    Returns text with proper dashes, quotes and non-breaking spaces.
    """

    template = """<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <ProcessText xmlns="{url}">
            <text>{text}</text>
            <entityType>3</entityType>
            <useBr>1</useBr>
            <useP>0</useP>
            <maxNobr>3</maxNobr>
        </ProcessText>
    </soap:Body>
    </soap:Envelope>"""

    # convert chars into HTML-safe sequences
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')

    r = post('{url}typograf.asmx'.format(url=SERVICE_URL),
             template.format(url=SERVICE_URL, text=text).encode('utf-8'))

    if r.status_code == 200:
        root = ET.fromstring(r.content)
        return root.findtext(
            './/{{{url}}}ProcessTextResult'.format(url=SERVICE_URL)) \
            .replace('<br />\n', '\n') \
            .rstrip('\n')  # remove <br> tags and the last newline
    else:
        return text


if __name__ == '__main__':
    print('clipboard type:', pyperclip._functions)

    # get text from clipboard
    text = pyperclip.paste()
    # replace text in clipboard
    pyperclip.copy(typograf(text))
    pyperclip.paste()
