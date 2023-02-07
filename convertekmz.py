import streamlit as st
import fiona
import geopandas as gpd

def convert_kmz_to_shp(kmz_file):
    # Carregar o arquivo .kml como um GeoDataFrame
    gdf = gpd.read_file(kmz_file)

    # Escrever o GeoDataFrame como um shapefile
    gdf.to_file("arquivo.shp", driver="ESRI Shapefile")
    
    return "Arquivo convertido com sucesso!"

st.title("Conversor de KMZ para Shapefile")

file = st.file_uploader("Escolha o arquivo KMZ", type=["kmz"])

if file:
    result = convert_kmz_to_shp(file)
    st.success(result)
