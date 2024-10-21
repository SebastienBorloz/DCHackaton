# my_app.py
import folium
from streamlit_folium import st_folium
import streamlit as st

def get_pos(lat,lng):
    return lat,lng

m = folium.Map(location=[40.7128, -74.0060], zoom_start=14).add_child(folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}"))
#m.save("FoliumMap.html")


map = st_folium(m, height=900, width=1500)


data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])

if data is not None:
    st.write(data) # Writes to the app
    print(data) # Writes to terminal
