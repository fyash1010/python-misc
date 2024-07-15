import webbrowser
import time

placeList = ["california", "alabama", "mumbai", "jaipur", "alaska", "arizona", "arkansa", "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "ohio", "oregon", "done"]

edgePath = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"

for x in placeList:
    webbrowser.get(edgePath).open("https://www.bing.com/search?q=" + x)
    time.sleep(3)