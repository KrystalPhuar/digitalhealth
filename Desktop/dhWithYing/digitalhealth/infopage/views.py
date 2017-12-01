# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bs4 import BeautifulSoup
from django.shortcuts import render
import re
from xml.dom.minidom import parse, parseString
from .models import Bsi, Bsm, Bsds, Bshf, Cci, Ccm, Ccds, Cchf, Chi, Chm, Chds, Chhf, Mi, Mm, Mds, Mhf
#remember to import models


def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    htmlDoc = open("infopage/templates/index.html")
    soup = BeautifulSoup(htmlDoc, 'lxml')
    findBsi = soup.find(id='bsi')
    findBsm = soup.find(id='bsm')
    findBsds = soup.find(id='bsds')
    findBshf = soup.find(id='bshf')
    findCci = soup.find(id='cci')
    findCcm = soup.find(id='ccm')
    findCcds = soup.find(id='ccds')
    findCchf = soup.find(id='cchf')
    findChi = soup.find(id='chi')
    findChm = soup.find(id='chm')
    findChds = soup.find(id='chds')
    numBsi = Bsi.objects.count()
    numBsm = Bsm.objects.count()
    numBsds = Bsds.objects.count()
    numBshf = Bshf.objects.count()
    numCci = Cci.objects.count()
    numCcm = Ccm.objects.count()
    numCcds = Ccds.objects.count()
    numCchf = Cchf.objects.count()
    numChi = Chi.objects.count()
    numChm = Chm.objects.count()
    numChds = Chds.objects.count()
    print(numCci)


    if numBsi > 0 and numBsi <= 1:
        addAttBsi = findBsi['style'] = "top: 4px; left: 50px; width: 15px; height: 15px;"
    elif numBsi >= 2 and numBsi <=3:
        addAttBsi = findBsi['style'] = "top: 1px; left: 46px; width: 25px; height: 25px;"
    elif numBsi > 3:
        addAttBsi = findBsi['style'] = "top: -3px; left: 40px; width: 35px; height: 35px;"
    else:
        addAttBsi = findBsi['style'] = "width: 0px; height: 0px;"

    if numBsm > 0 and numBsm <= 1:
        addAttBsm = findBsm['style'] = "top: 4px; left: 95px; width: 15px; height: 15px;"
    elif numBsm >= 2 and numBsm <= 3:
        addAttBsm = findBsm['style'] = "top: 1px; left: 90px; width: 25px; height: 25px;"
    elif numBsm > 3:
        addAttBsm = findBsm['style'] = "top: -3px; left: 85px; width: 35px; height: 35px;"
    else:
        addAttBsm = findBsm['style'] = "width: 0px; height: 0px;"

    if numBsds > 0 and numBsds <= 1:
        addAttBsds = findBsds['style'] = "top: 4px; left: 140px; width: 15px; height: 15px;"
    elif numBsds >= 2 and numBsds <= 3:
        addAttBsds = findBsds['style'] = "top: 1px; left: 135px; width: 25px; height: 25px;"
    elif numBsds > 3:
        addAttBsds = findBsds['style'] = "top: -3px; left: 130px; width: 35px; height: 35px;"
    else:
        addAttBsds = findBsds['style'] = "width: 0px; height: 0px;"

    if numBshf > 0 and numBshf <= 1:
        addAttBshf = findBshf['style'] = "top: 4px; left: 185px; width: 15px; height: 15px;"
    elif numBshf >= 2 and numBshf <= 3:
        addAttBshf = findBshf['style'] = "top: 1px; left: 180px; width: 25px; height: 25px;"
    elif numBshf > 3:
        addAttBshf = findBshf['style'] = "top: -3px; left: 175px; width: 35px; height: 35px;"
    else:
        addAttBshf = findBshf['style'] = "width: 0px; height: 0px;"


    if numCci > 0 and numCci <= 1:
        addAttCci = findCci['style'] = "top: 49px; left: 50px; width: 15px; height: 15px;"
    elif numCci >= 2 and numCci <= 3:
        addAttCci = findCci['style'] = "top: 44px; left: 46px; width: 25px; height: 25px;"
    elif numCci > 3:
        addAttCci = findCci['style'] = "top: 39px; left: 40px; width: 35px; height: 35px;"
    else:
        addAttCci = findCci['style'] = "width: 0px; height: 0px;"

    if numCcm > 0 and numCcm <= 1:
        addAttCcm = findCcm['style'] = "top: 49px; left: 95px; width: 15px; height: 15px;"
    elif numCci >= 2 and numCci <= 3:
        addAttCcm = findCcm['style'] = "top: 44px; left: 140px; width: 25px; height: 25px;"
    elif numCcm > 3:
        addAttCcm = findCcm['style'] = "top: 39px; left: 185px; width: 35px; height: 35px;"
    else:
        addAttCcm = findCcm['style'] = "width: 0px; height: 0px;"

    if numCcds > 0 and numCcds <= 1:
        addAttCcds = findCcds['style'] = "top: 49px; left: 140px; width: 15px; height: 15px;"
    elif numCcds >= 2 and numCcds <= 3:
        addAttCcds = findCcds['style'] = "top: 44px; left: 135px; width: 25px; height: 25px;"
    elif numCcds > 3:
        addAttCcds = findCcds['style'] = "top: 39px; left: 130px; width: 35px; height: 35px;"
    else:
        addAttCcds = findCcds['style'] = "width: 0px; height: 0px;"

    if numCchf > 0 and numCchf <= 1:
        addAttCchf = findCchf['style'] = "top: 49px; left: 185px; width: 15px; height: 15px;"
    elif numCchf >= 2 and numCchf <= 3:
        addAttCchf = findCchf['style'] = "top: 44px; left: 180px; width: 25px; height: 25px;"
    elif numCchf > 3:
        addAttCchf = findCchf['style'] = "top: 39px; left: 175px; width: 35px; height: 35px;"
    else:
        addAttCchf = findCchf['style'] = "width: 0px; height: 0px;"

    if numChi > 0 and numChi <= 1:
        addAttChi = findChi['style'] = "top: 94px; left: 50px; width: 15px; height: 15px;"
    elif numChi >= 2 and numChi <= 3:
        addAttChi = findChi['style'] = "top: 139px; left: 46px; width: 25px; height: 25px;"
    elif numChi > 3:
        addAttChi = findChi['style'] = "top: 184px; left: 40px; width: 35px; height: 35px;"
    else:
        addAttChi = findChi['style'] = "width: 0px; height: 0px;"

    if numChm > 0 and numChm <= 1:
        addAttChm = findChm['style'] = "top: 94px; left: 95px; width: 15px; height: 15px;"
    elif numChm >= 2 and numChm <= 3:
        addAttChm = findChm['style'] = "top: 139px; left: 135px; width: 25px; height: 25px;"
    elif numChm > 3:
        addAttChm = findChm['style'] = "top: 184px; left: 180px; width: 35px; height: 35px;"
    else:
        addAttChm = findChm['style'] = "width: 0px; height: 0px;"

    if numChds > 0 and numChds <= 1:
        addAttChds = findChds['style'] = "top: 94px; left: 95px; width: 15px; height: 15px;"
    elif numChds >= 2 and numChds <= 3:
        addAttChds = findChds['style'] = "top: 139px; left: 135px; width: 25px; height: 25px;"
    elif numChds > 3:
        addAttChds = findChds['style'] = "top: 184px; left: 180px; width: 35px; height: 35px;"
    else:
        addAttChds = findChds['style'] = "width: 0px; height: 0px;"



    htmlDoc.close()
    html = soup.prettify("utf-8")

    with open("infopage/templates/index.html", "wb") as output:
        output.write(html)


    return render(
        request,
        'index.html',
        context={},
    )
