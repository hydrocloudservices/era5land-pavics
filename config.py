from datetime import datetime, timedelta


class Config(object):

    # Bucket configuration
    BUCKET = 's3://era5/north-america/reanalysis/land/netcdf4'
    
    CLIENT_KWARGS = {'endpoint_url': 'https://s3.wasabisys.com',
                     'region_name': 'us-east-1'}
    CONFIG_KWARGS = {'max_pool_connections': 30}
    PROFILE = 'default'

    STORAGE_OPTIONS = {'profile': PROFILE,
                       'client_kwargs': CLIENT_KWARGS,
                       'config_kwargs': CONFIG_KWARGS
                       }

    # Dataset
    # START_DATE = "2023-01-01"
    # END_DATE = (datetime.utcnow() - timedelta(days=6)).strftime('%Y-%m-%d')

    # VARIABLES = {
    #     'total_precipitation': 'tp',
    #     '2m_temperature': 't2m',
    #     'snow_depth_water_equivalent': 'sd',
    # }

    START_DATE = "1951-01-01"
    END_DATE = (datetime.utcnow() - timedelta(days=6)).strftime('%Y-%m-%d')

    VARIABLES = {
        'snowfall': 'sf',
        '10m_u_component_of_wind': 'u10',
        '10m_v_component_of_wind': 'v10',
        '2m_dewpoint_temperature': 'd2m',
        'potential_evaporation': 'pev',
        'surface_pressure': 'sp',
        'surface_solar_radiation_downwards': 'ssrd',
        'surface_thermal_radiation_downwards': 'strd'
            }

    TIMES = ['00:00', '01:00', '02:00',
             '03:00', '04:00', '05:00',
             '06:00', '07:00', '08:00',
             '09:00', '10:00', '11:00',
             '12:00', '13:00', '14:00',
             '15:00', '16:00', '17:00',
             '18:00', '19:00', '20:00',
             '21:00', '22:00', '23:00'
             ]
