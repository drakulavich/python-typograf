#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import xml.etree.ElementTree as ET
import pyperclip
from requests import post

SERVICE_URL = 'http://typograf.artlebedev.ru/webservices/'
TEMPLATE = u"""<?xml version="1.0" encoding="UTF-8"?>
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


def get_htmlsafe(text):
    """ Returns HTML-safe string """

    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')

    return text


def typograf(text):
    """ Returns text with russian typography """

    src = get_htmlsafe(text)
    r = post('{url}typograf.asmx'.format(url=SERVICE_URL),
             TEMPLATE.format(url=SERVICE_URL, text=src)
             .encode('utf-8'))

    if r.status_code == 200:
        root = ET.fromstring(r.content)
        res = root.findtext('.//{{{url}}}ProcessTextResult'
                            .format(url=SERVICE_URL))
        # remove br tags and last newline
        res = res.replace('<br />\n', '\n').rstrip('\n')
        text = res

    return text


if __name__ == '__main__':
    print('used func:', pyperclip.copy.__name__)

    # get text from clipboard
    text = pyperclip.paste()
    # replace text in clipboard
    pyperclip.copy(typograf(text))
    pyperclip.paste()
