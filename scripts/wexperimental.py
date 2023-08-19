import modules.scripts as scripts
from modules import images
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state

import gradio as gr
import numpy as np

class Script(scripts.Script):

    def title(self):
        print('**************title')
        return "WExperimental"
        
    def show(self):
        print('**************show')
        return True

    def ui(self):
        print('**************ui')
        return None

    def run(self, p, only_save_background_free_pictures, do_not_auto_save):
        print('**************run')
        return None
