from googlesearch import search
from bs4 import BeautifulSoup
import re
import requests
import pymysql.cursors

database = pymysql.connect (
    host="localhost",
    user = "ivanubi",
    passwd = "ubinas",
    db = "indotel", # Database with all the NXX phone codes from INDOTEL.
    )

#NXX: NXX stands for Network Numbering Exchange (in North American Numbering Plan)

def local_numbers():
    cursor = database.cursor()
    sql = "SELECT `nxx` FROM `indotel` WHERE (`tipo`= 'LINEA FIJA'); "
    query = cursor.execute(sql)
    results = cursor.fetchall()
    return results

def fullfil_locations():
    try:
        cursor = database.cursor()
        sql = "SELECT `nxx` FROM `indotel` WHERE (`tipo`= 'LINEA FIJA'); "
        query = cursor.execute(sql)
        results = cursor.fetchall()
        for nxx in results:
            localidad = location(nxx[0])
            if isinstance(localidad, str):
                query = "UPDATE indotel SET localidad = '" + localidad +"' WHERE (nxx = " + str(nxx[0]) + " AND `tipo`= 'LINEA FIJA');"
                cursor.execute(query)
                print("NXX: " + str(nxx[0]) + " / Localidad: " + localidad)
        cursor.close() # Close the cursor
        database.commit() # Commit the transaction
        database.close() # Close the database connection
    except TypeError as error:
        print("Error")
        pass


def top_url(nxx):
    if isinstance(nxx, int):
        nxx = str(nxx)

    for url in search('809 ' + nxx, stop=5):
        top_url = url
        break

    if '1411.com.do' not in top_url:
        for url in search('809 '+ nxx + ' 1411.com.do', stop=5):
            top_url = url
            break
    return top_url


def location(nxx):
    url = top_url(nxx)
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, features="html.parser")
    print(url)

    # HTML Example:
    #   <div class="title floatleft fix">
    #	  <h1>Premium 98</h1>
    #	  <p><strong>Dirección: </strong>R Marte 50, Nagua</p>
    #	  <br>
    #	  <h2>809-584-1212</h2>
    #   </div>

    try:
        # First we want the 'div' element with the class 'Title floatleft fix':
        text = soup.find("div", {"class": "title floatleft fix"})
        # Then we get the only 'p' element inside that div:
        result = text.find('p').get_text()
        # Finally we get the word between the strings ', ' and ''.
        # In the example case that would be 'Nagua'.
        if "Santo Domingo" in result:
            return "Santo Domingo"
        elif "Santiago" in result:
            return "Santiago"
        elif "Distrito Nacional" in result:
            return "Distrito Nacional"
        else:
            result = re.search(', (.*)', result)
            return result.group(1)

    except AttributeError as error:
        pass

fullfil_locations()
