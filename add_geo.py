from osgeo import osr, gdal
# 给图片添加地理信息，针对单个文件


def assign_spatial_reference_byfile(src_path, dst_path):
    src_ds = gdal.Open(src_path, gdal.GA_ReadOnly)
    sr = osr.SpatialReference()
    sr.ImportFromWkt(src_ds.GetProjectionRef())
    geoTransform = src_ds.GetGeoTransform()
    dst_ds = gdal.Open(dst_path, gdal.GA_Update)
    dst_ds.SetProjection(sr.ExportToWkt())
    dst_ds.SetGeoTransform(geoTransform)
    dst_ds = None
    src_ds = None


if __name__ == '__main__':

    src_path = r'D:\样本\temp\源文件\瓜沥镇_clip26.tif'
    dst_path = r'D:\code\Road_segmentation\image\clip1.tif'
    assign_spatial_reference_byfile(src_path, dst_path)