import os
import json

class Settings:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = {
            'default_paths': {
                'memory_analysis': '',
                'disk_analysis': '',
                'email_analysis': '',
                'network_analysis': '',
                'registry_analysis': '',
                'browser_forensics': '',
                'log_analysis': '',
                'mobile_forensics': '',
                'cloud_forensics': '',
                'timeline_analysis': '',
                'usb_forensics': '',
                'malware_analysis': '',
                'metadata_analysis': '',
                'social_media_forensics': '',
                'steganography_detection': ''
            },
            'logging': {
                'log_level': 'INFO',
                'log_file': 'forensics_tool.log'
            },
            'ui_preferences': {
                'theme': 'light',  # Options: 'light', 'dark'
                'font_size': 12
            }
        }
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                self.config.update(json.load(file))

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

    def get_default_path(self, analysis_type):
        return self.config['default_paths'].get(analysis_type, '')

    def set_default_path(self, analysis_type, path):
        self.config['default_paths'][analysis_type] = path
        self.save_config()

    def get_log_level(self):
        return self.config['logging']['log_level']

    def set_log_level(self, log_level):
        self.config['logging']['log_level'] = log_level
        self.save_config()

    def get_log_file(self):
        return self.config['logging']['log_file']

    def set_log_file(self, log_file):
        self.config['logging']['log_file'] = log_file
        self.save_config()

    def get_ui_preference(self, preference):
        return self.config['ui_preferences'].get(preference, '')

    def set_ui_preference(self, preference, value):
        self.config['ui_preferences'][preference] = value
        self.save_config()