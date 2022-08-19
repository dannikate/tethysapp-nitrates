from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
from django.shortcuts import render
from django.http import JsonResponse
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import Button

import json

import pandas as pd
import numpy as np
import os


@controller
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='save',
        style='success',
        attributes={
            'data-bs-toggle':'tooltip',
            'data-bs-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='pen',
        style='warning',
        attributes={
            'data-bs-toggle':'tooltip',
            'data-bs-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='trash',
        style='danger',
        attributes={
            'data-bs-toggle':'tooltip',
            'data-bs-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-bs-toggle':'tooltip',
            'data-bs-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-bs-toggle':'tooltip',
            'data-bs-placement':'top',
            'title':'Next'
        }
    )

    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button
    }

    return render(request, 'nitrates/home.html', context)


# def solve_linreg(x, m, b):
    # return x * m + b


@controller(name='get-nitrate-time-series', url='get-nitrate-time-series', app_workspace=True)
def get_nitrate_time_series(request, app_workspace):
    # determine which well id the user wants a time series for
    well_id = request.GET.get("well_id")
    # read the csv with the same name as the id
    df = pd.read_csv(os.path.join(app_workspace.path, f'{well_id}.csv')).dropna()
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    df_stats = pd.read_csv(os.path.join(app_workspace.path, 'NO3Data-All.csv'))
    df_stats = df_stats.loc[df_stats['Well'] == well_id]
    df_stats = df_stats.replace(np.nan, '')
    df_stats = df_stats.to_dict(orient='records')[0]
    
    # format the csv as a json which we can send back to the user
    return JsonResponse({
        'datetime': list(df['datetime']),
        'values': list(df['values']),
        'stats': df_stats,
        'datetime_linreg': [list(df['datetime'])[0], list(df['datetime'])[-1]],
        # 'values_linreg': [
            # solve_linreg(df['datetime'][0], df_stats['Slope'], df_stats['Intercept']),
            # solve_linreg(df['datetime'][-1], df_stats['Slope'], df_stats['Intercept']),
        # ]
    })

# @controller(name='get-well-stats', url='get-well-stats', app_workspace=True)
# def get_well_stats(request, app_workspace):
#     # determine which well id the user wants a time series for
#     well_id = request.GET.get("well_id")
#      # read the csv with the same name as the id
#     df_stats = pd.read_csv(os.path.join(app_workspace.path, 'NO3Data-All.csv'))
#     df_stats = df_stats.loc[df_stats['Well'] == well_id].to_dict(orient='records')
    
#     return JsonResponse({
#         'avg': df_stats['Average'],
#         'basin': df_stats['Basin']
#     })
