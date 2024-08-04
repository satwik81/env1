import os
import pandas as pd
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import formforcsv
from .models import filecsv

def uploadfilecsv(request):
    if request.method == 'POST':
        form = formforcsv(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.save()
            file_path = csv_file.file.path
            file_name=csv_file.file.name     
            try:
                dataset_html, debug_info, plot_paths = process_csv_file(file_path)
            except Exception as e:
                debug_info = {"error": str(e)}
                dataset_html = ""
                plot_paths = []
            
            return render(request, 'success.html', {
                'dataset_html': dataset_html,
                'debug_info': debug_info,
                'plot_paths': plot_paths,
                'file_name':file_name
            })
    else:
        form = formforcsv()
    
    return render(request,'uploadcsvfile.html',{'form': form})

def process_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        #First few rows
        first_rows_html = df.head().to_html(classes='table table-striped')
        #Summary statistics
        summary_stats = df.describe().T[['mean', '50%', 'std']].rename(columns={'50%': 'Median'})
        summary_stats_html = summary_stats.to_html(classes='table table-striped')
        #Handling missing values
        missing_values = df.isnull().sum()
        missing_values_html = missing_values[missing_values > 0].to_frame().rename(columns={0: 'Missing Values'}).to_html(classes='table table-striped')
        #Generate plots
        plot_paths = generate_plots(df)
        debug_info = {
            "first_rows": first_rows_html,
            "summary_stats": summary_stats_html,
            "missing_values": missing_values_html
        }
        return df.to_html(classes='table table-striped'),debug_info,plot_paths
    except Exception as e:
        return "",{"error": str(e)}, []

def generate_plots(df):
    plot_paths = []
    numerical_columns = df.select_dtypes(include=['float64','int64']).columns
    for column in numerical_columns:
        plt.figure()
        sns.histplot(df[column].dropna(),kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plot_path = os.path.join(settings.MEDIA_ROOT,f'{column}_histogram.png')
        plt.savefig(plot_path)
        plt.close()
        plot_paths.append(os.path.join(settings.MEDIA_URL,f'{column}_histogram.png'))

    return plot_paths

    

def uploadsuccess(request):
    return render(request,'success.html',{'data_html':''})
            

# Create your views here.
