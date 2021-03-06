from ast import arg
import pandas as pd
import argparse
from src.utils.common_utils import read_params, clean_prev_dirs_if_exists, create_dir, save_local_df
import logging
import requests
from loguru import logger

logger.add("artifacts/logs/out.log", format="{time} {level} {message}")

def get_data(config_path):
    config = read_params(config_path)
    
    data_path = config["data_source"]["drive_source"]
    artifacts_dir = config["artifacts"]["artifacts_dir"] 
    
    raw_local_data_dir = config["artifacts"]["raw_local_data_dir"] 
    raw_local_data = config["artifacts"]["raw_local_data"]
    
    clean_prev_dirs_if_exists(artifacts_dir)
    
    create_dir(dirs=[artifacts_dir, raw_local_data_dir])
    
    df = pd.read_csv(data_path, sep=",")
    
    save_local_df(df, raw_local_data)
    logger.info("Successfully saved dataframe in the give path")


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parse_args = args.parse_args()
    
    try:
        data = get_data(config_path=parse_args.config)
    except Exception as e:
        raise e 