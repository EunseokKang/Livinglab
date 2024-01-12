from arcgis.gis import GIS
from arcgis.geometry import Polyline
from arcgis.features import Feature, FeatureSet, FeatureLayer
import geopandas as gpd
import os

# ArcGIS Online에 로그인
gis = GIS("https://www.arcgis.com", "Eunseok", "90979231qC@")

# CSV 파일이 있는 디렉토리 경로
csv_directory = 'D:/CodingBackup/Coding/School/Bus/csvFiles/Buses'

# CSV 파일을 처리하는 함수
def process_csv_file(csv_file_path, color):
    # CSV 파일을 GeoDataFrame으로 변환
    gdf = gpd.read_file(csv_file_path)

    # GeoDataFrame을 FeatureSet으로 변환
    features = [Feature(geometry=f['geometry'].__geo_interface__, attributes=f['properties']) for f in gdf.__geo_interface__['features']]
    feature_set = FeatureSet(features=features)

    # 마커 생성
    marker_layer = gis.content.import_data(feature_set, title='Markers')

    # 마커들을 연결하는 선 생성
    line_geometry = Polyline(features=feature_set.features)
    line_feature = [{"geometry": line_geometry, "attributes": {}}]
    line_layer = FeatureLayer.from_dict({"geometryType": "esriGeometryPolyline", "features": line_feature})

    # 선의 색상 설정
    line_layer.renderer = {
        "type": "simple",
        "symbol": {
            "type": "simple-line",
            "color": color,  # 여기서 색상을 설정합니다.
            "width": 2
        }
    }

    # ArcGIS Earth에 레이어 추가
    map_widget.add_layer(marker_layer)
    map_widget.add_layer(line_layer)

# ArcGIS Earth에 맵 생성
map_widget = gis.map("Your_Location")

# CSV 디렉토리 안의 모든 파일에 대해 처리
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        csv_file_path = os.path.join(csv_directory, filename)

        # 색상을 다르게 할당
        color = "#{:06x}".format(hash(filename) & 0xFFFFFF)

        # 각 CSV 파일을 처리
        process_csv_file(csv_file_path, color)

# 지도 표시
map_widget
