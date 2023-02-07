import streamlit as st
import geopandas as gpd

def convert_to_shp(file):
    # Carregar o arquivo como um GeoDataFrame
    gdf = gpd.read_file(file)

    # Escrever o GeoDataFrame como um shapefile
    filename = file.split(".")[0] + ".shp"
    gdf.to_file(filename, driver="ESRI Shapefile")
    
    return f"Arquivo convertido com sucesso para {filename}!"

st.title("Conversor de KML/KMZ para Shapefile")

file = st.file_uploader("Escolha o arquivo KML/KMZ", type=["kml", "kmz"])

if file:
    result = convert_to_shp(file)
    st.success(result)
