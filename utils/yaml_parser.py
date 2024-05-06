import argparse
import yaml


def yaml_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-config', help="configuration file *.yaml", type=str, required=False, default='config.yaml')
    args = parser.parse_args()
    
    config = yaml.load(open(args.config), Loader=yaml.FullLoader)
    for key, value in config.items():
        parser.add_argument(f"--{key}", type=type(key), default=value)
        
    args = parser.parse_args()
    
    return args