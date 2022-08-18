from tethys_sdk.base import TethysAppBase


class Nitrates(TethysAppBase):
    """
    Tethys app class for Test.
    """

    name = 'Guam Nitrates'
    description = 'Well nitrate measurments'
    package = 'nitrates'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'nitrates'
    color = '#2d3436'
    tags = ''
    enable_feedback = False
    feedback_emails = []