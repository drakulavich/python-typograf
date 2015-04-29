# encoding: utf-8

u"""Простой интерфейс к веб-сервису Типографа Студии Артемия Лебедева

Работает в связке с Alfred, но может использоваться отдельно"""

from __future__ import print_function

import sys

import xml.etree.ElementTree as ET
import httplib, urllib
import unicodedata

def process(text):
    headers = {"Content-type": "application/xml"}

    template = u"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n'
    <soap:Body>'
        <ProcessText xmlns="http://typograf.artlebedev.ru/webservices/">
            <text>{text}</text>
            <entityType>3</entityType>
            <useBr>0</useBr>
            <useP>0</useP>
            <maxNobr>3</maxNobr>
        </ProcessText>
        </soap:Body>
    </soap:Envelope>"""

    conn = httplib.HTTPConnection("typograf.artlebedev.ru")
    conn.request("POST", "/webservices/typograf.asmx",
                 template.format(text=text).encode('utf-8'),
                 headers)
    response = conn.getresponse()
    if response.status == 200:
        root = ET.fromstring(response.read())
        conn.close()
        return root.findtext(".//{http://typograf.artlebedev.ru/webservices/}ProcessTextResult")
    else:
        conn.close()
        return text

if __name__ == '__main__':
    text = sys.stdin.read().decode('utf-8')
    # http://www.alfredforum.com/topic/1724-script-filter-arguments-are-decomposed/
    # Альфред передаёт данные в декомпозированном виде,
    # т.е. букву ё в виде двух символов е и  ̈
    # Поэтому надо нормализовать переданную строку
    text = unicodedata.normalize('NFC', text)
    processed = process(text)
    sys.stdout.write(processed.encode('utf-8'))

