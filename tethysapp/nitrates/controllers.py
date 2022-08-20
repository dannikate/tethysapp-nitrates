from django.shortcuts import render
from django.http import JsonResponse
from tethys_sdk.workspaces import app_workspace

import pandas as pd
import numpy as np
import os


def home(request):
    """
    Controller for the app home page.
    """
    context = {}
    return render(request, 'nitrates/home.html', context)


# def solve_linreg(x, m, b):
    # return x * m + b


@app_workspace
def get_nitrate_time_series(request, workspace):
    # determine which well id the user wants a time series for
    well_id = request.GET.get("well_id")
    # read the csv with the same name as the id
    df = pd.read_csv(os.path.join(workspace.path, f'{well_id}.csv')).dropna()
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    df_stats = pd.read_csv(os.path.join(workspace.path, 'NO3Data-All.csv'))
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
