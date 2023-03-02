import xarray as xr


class XarrayZarrStore():
    def __init__(self,
                 path,
                 time_dim_name: str = "time"):
        self.path = path
        self.time_dim_name = time_dim_name

    @property
    def datastore(self):
        return xr.open_zarr(self.path)

    def _get_last_timestep(self):
        return self.datastore[self.time_dim_name]

    def _clip_dataset(self):
        return self.datastore[self.time_dim_name]