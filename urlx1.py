#!/usr/bin/env python3

# This app can be used to put one domain main and get the reputation from the different sites that are mentioned
# in the readme.md.
# Save some time by not having to go to different sites and pasting in the domain name.

from urllib import request
import urllib
import re


def introscreen():
    print("         ***   URL ANALYSIS SCRIPT FOR CYBER ANALYSTS   ***")


def urlvoid(urlx):
    urlvoidurl = ("https://urlvoid.com/scan/" + urlx + "/")
    fp = urllib.request.urlopen(urlvoidurl)  # this is the connection to the page?
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    score = re.findall("[0-9]{1,2}/[0-9]{2}", mystr)
    print("URLVOID.COM: " + urlvoidurl + "Score: ", score)


def safewebnorton(urlx):
    safewebnortonurl = ("https://safeweb.norton.com/report/show?url=" + urlx)
    # print("SAFEWEB.NORTON.COM: " + safewebnortonurl)
    fp = urllib.request.urlopen(safewebnortonurl)  # this is the connection to the page?
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    verdict = re.findall("SAFE|CAUTION", mystr)
    verdict = str(verdict) #converitng verdict from list to string.
    print("SAFEWEB.NORTON.COM: " + safewebnortonurl + " Verdict: " + verdict)


def sucurinet(urlx):
    sucurineturl = ("https://sitecheck.sucuri.net/results/" + urlx + "/")
    print("SITECHECK.SUCURI.NET: " + sucurineturl)
    # fp = urllib.request.urlopen(sucurineturl)  # this is the connection to the page?
    # sucuribytes = fp.read()
    # mystr = sucuribytes.decode("utf8")
    # fp.close()
    # score = re.findall("Site issues detected", mystr)
    # print("Issues detected: ", score)


def talosintelligence(urlx):
    talosurl = ("https://talosintelligence.com/reputation_center/lookup?search=" + urlx)
    print("TALOSINTELLIGENCE.COM: " + talosurl)


def threatminerorg(urlx):
    threatminerurl = ("https://www.threatminer.org/domain.php?q=" + urlx)
    print("THREATMINER.ORG: " + threatminerurl)
    #webbrowser.open(threatminerurl)


def abuseipdb(urlx):
    abuseipdburl = ("https://www.abuseipdb.com/check/" + urlx)
    print("ABUSEIPDB.COM: " + abuseipdburl)
    # webbrowser.open(abuseipdburl)


def transparencyreportgooglecom(urlx):
    transparencyreportgooglecomurl = ("https://transparencyreport.google.com/safe-browsing/search?url=" + urlx)
    print("TRANSPARENCYREPORT.GOOGLE.COM: " + transparencyreportgooglecomurl)


def hashddcom(urlx):
    hashddcomurl = ("https://hashdd.com/i/" + urlx)
    print("HASHDD.COM: " + hashddcomurl)



def malwaredomainlistcom(urlx):
    malwaredomainlistcomurl = ("http://www.malwaredomainlist.com/mdl.php?search=" + urlx + "&colsearch=All&quantity=50")
    print("MALWAREDOMAINLIST.COM: " + malwaredomainlistcomurl)



def reputationauthorityorg(urlx):
    reputationauthorityorgurl = ("http://www.reputationauthority.org/domain_lookup.php?ip=" + urlx + "&ipvalid=&Submit.x=0&Submit.y=0")
    print("REPUTATIONAUTHORIY.ORG: " + reputationauthorityorgurl)



def scamadvisorcom(urlx):
    scamadvisorcomurl = ("https://www.scamadviser.com/check-website/" + urlx)
    print("HASHDD.COM: " + scamadvisorcomurl)



def securitytrailscom(urlx):
    securitytrailscomurl = ("https://securitytrails.com/domain/" + urlx + "/dns")
    print("SECURITYTRAILS.COM : " + securitytrailscomurl)




introscreen()
urlx = input("  Enter a domain address to get the analysis results: ")
print("  You entered: ", urlx + "\n")

urlvoid(urlx)
safewebnorton(urlx)
sucurinet(urlx)
talosintelligence(urlx)
threatminerorg(urlx)
abuseipdb(urlx)
transparencyreportgooglecom(urlx)
hashddcom(urlx)
malwaredomainlistcom(urlx)
reputationauthorityorg(urlx)
scamadvisorcom(urlx)
securitytrailscom(urlx)
