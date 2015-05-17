from rest_framework import generics
from rest_framework.filters import DjangoFilterBackend

from .models import *
from .serializers import *
from rest_framework_gis.filters import *


class LocationList(generics.ListCreateAPIView):
    model = Location
    serializer_class = LocationGeoSerializer
    queryset = Location.objects.all()
    pagination_class = PaginatedLocationGeoSerializer

location_list = LocationList.as_view()


class LocationDetails(generics.RetrieveUpdateDestroyAPIView):
    model = Location
    serializer_class = LocationGeoSerializer
    queryset = Location.objects.all()

location_details = LocationDetails.as_view()


class GeojsonLocationList(generics.ListCreateAPIView):
    model = Location
    serializer_class = LocationGeoFeatureSerializer
    queryset = Location.objects.all()
    pagination_class = PaginatedLocationGeoFeatureSerializer

geojson_location_list = GeojsonLocationList.as_view()


class GeojsonLocationContainedInBBoxList(generics.ListAPIView):
    model = Location
    serializer_class = LocationGeoFeatureSerializer
    queryset = Location.objects.all()
    bbox_filter_field = 'geometry'
    filter_backends = (InBBoxFilter,)

geojson_location_contained_in_bbox_list = GeojsonLocationContainedInBBoxList.as_view()


class GeojsonLocationOverlapsBBoxList(GeojsonLocationContainedInBBoxList):
    bbox_filter_include_overlapping = True

geojson_location_overlaps_bbox_list = GeojsonLocationOverlapsBBoxList.as_view()


class GeojsonLocationContainedInTileList(generics.ListAPIView):
    model = Location
    serializer_class = LocationGeoFeatureSerializer
    queryset = Location.objects.all()
    bbox_filter_field = 'geometry'
    filter_backends = (TMSTileFilter,)

geojson_location_contained_in_tile_list = GeojsonLocationContainedInTileList.as_view()


class GeojsonLocationOverlapsTileList(GeojsonLocationContainedInTileList):
    bbox_filter_include_overlapping = True

geojson_location_overlaps_tile_list = GeojsonLocationOverlapsTileList.as_view()


class GeojsonLocationWithinDistanceOfPointList(generics.ListAPIView):
    model = Location
    serializer_class = LocationGeoFeatureSerializer
    distance_filter_convert_meters = True
    queryset = Location.objects.all()
    distance_filter_field = 'geometry'
    filter_backends = (DistanceToPointFilter,)

geojson_location_within_distance_of_point_list = GeojsonLocationWithinDistanceOfPointList.as_view()


class GeojsonLocationWithinDegreesOfPointList(GeojsonLocationWithinDistanceOfPointList):
    distance_filter_convert_meters = False #Default setting

geojson_location_within_degrees_of_point_list = GeojsonLocationWithinDegreesOfPointList.as_view()


class GeojsonLocationDetails(generics.RetrieveUpdateDestroyAPIView):
    model = Location
    serializer_class = LocationGeoFeatureSerializer
    queryset = Location.objects.all()

geojson_location_details = GeojsonLocationDetails.as_view()


class GeojsonLocationSlugDetails(generics.RetrieveUpdateDestroyAPIView):
    model = Location
    lookup_field = 'slug'
    serializer_class = LocationGeoFeatureSlugSerializer
    queryset = Location.objects.all()

geojson_location_slug_details = GeojsonLocationSlugDetails.as_view()


class GeojsonLocationFalseIDDetails(generics.RetrieveUpdateDestroyAPIView):
    model = Location
    serializer_class = LocationGeoFeatureFalseIDSerializer
    queryset = Location.objects.all()

geojson_location_falseid_details = GeojsonLocationFalseIDDetails.as_view()


class LocationFilter(GeoFilterSet):
    contains_properly = GeometryFilter(name='geometry', lookup_type='contains_properly')

    class Meta:
        model = Location


class GeojsonLocationContainedInGeometry(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationGeoSerializer
    filter_class = LocationFilter

    filter_backends = (DjangoFilterBackend,)

geojson_contained_in_geometry = GeojsonLocationContainedInGeometry.as_view()


class GeojsonLocatedFileDetails(generics.RetrieveUpdateDestroyAPIView):
    model = LocatedFile
    serializer_class = LocatedFileGeoFeatureSerializer
    queryset = LocatedFile.objects.all()

geojson_located_file_details = GeojsonLocatedFileDetails.as_view()


class GeojsonLocatedImageDetails(generics.RetrieveUpdateDestroyAPIView):
    model = LocatedImage
    serializer_class = LocatedImageGeoFeatureSerializer
    queryset = LocatedImage.objects.all()

geojson_located_image_details = GeojsonLocatedImageDetails.as_view()

