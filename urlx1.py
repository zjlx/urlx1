#!/usr/bin/env python3


from urllib import request
import urllib
import re


def introscreen():
    print("         ***   URL ANALYSIS SCRIPT FOR CYBER ANALYSTS   ***\n")
    print("         This program provides analysis information via the following websites.\n"
          "         [ URLVoid ][ Norton Safeweb ][ TALOSIntelligence ][ ThreatMiner ][ AbuseIPDB ]\n"
          "         Also displays the scraped desired text in the output.\n\n")

def urlvoid(urlx):
    urlvoidurl = ("https://urlvoid.com/scan/" + urlx + "/")
    #webbrowser.open(urlvoidurl)  # this works but only if the scan for a certain website has been done before.
    print("URLVOID.COM: " + urlvoidurl)
    fp = urllib.request.urlopen(urlvoidurl)  # this is the connection to the page?
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    score = re.findall("[0-9]{1,2}/[0-9]{2}", mystr)
    print("Score: ", score)


def safewebnorton(urlx):
    safewebnortonurl = ("https://safeweb.norton.com/report/show?url=" + urlx)
    print("SAFEWEB.NORTON.COM: " + safewebnortonurl)
    fp = urllib.request.urlopen(safewebnortonurl)  # this is the connection to the page?
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    verdict = re.findall("SAFE|CAUTION", mystr)
    print(verdict)


def sucurinet(urlx):
    sucurineturl = ("https://sitecheck.sucuri.net/results/" + urlx + "/")
    print("SITECHECK.SUCURI.NET: " + sucurineturl)
    fp = urllib.request.urlopen(sucurineturl)  # this is the connection to the page?
    sucuribytes = fp.read()
    mystr = sucuribytes.decode("utf8")
    fp.close()
    score = re.findall("Site issues detected", mystr)
    print("Issues detected: ", score)

introscreen()
urlx = input("  Enter a domain/url/ip address to get the analysis results:")
print("  You entered: ", urlx + "\n")

urlvoid(urlx)
safewebnorton(urlx)
sucurinet(urlx)