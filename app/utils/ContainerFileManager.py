import shutil

advanced_config_dir = '/home/israel/Documents/project/opensource/spectre/InstanceControllerService/OdooConfigurationFiles'
def create_new_config_dir(instance_dir):
    new_path = shutil.copytree(advanced_config_dir, instance_dir)
    return new_path