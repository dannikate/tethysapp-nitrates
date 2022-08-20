from tethys_sdk.base import TethysAppBase, url_map_maker


class Nitrates(TethysAppBase):
    """
    Tethys app class for Test.
    """
    name = 'Guam Nitrates'
    description = 'Well nitrate measurements'
    package = 'nitrates'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'nitrates'
    color = '#2d3436'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)
        return (
            UrlMap(
                name='home',
                url=f'{self.root_url}',
                controller=f'nitrates.controllers.home'
            ),
            UrlMap(
                name='get-nitrate-time-series',
                url=f'{self.root_url}/get-nitrate-time-series',
                controller=f'nitrates.controllers.get_nitrate_time_series'
            )
        )
