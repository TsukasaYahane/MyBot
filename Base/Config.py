import yaml

def get_config(yaml_file_path) :
    with open(yaml_file_path,"r",encoding = "utf-8") as yaml_flie :
        data = yaml.safe_load(yaml_flie)
    return data