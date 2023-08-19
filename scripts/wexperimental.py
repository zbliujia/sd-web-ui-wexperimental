import modules.scripts as scripts
from modules import images
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state

import gradio as gr
import numpy as np

class Script(scripts.Script):

    def title(self):
        print('----------------custom extension titile')
        return "Extension Template"

    # Decide to show menu in txt2img or img2img
    # - in "txt2img" -> is_img2img is `False`
    # - in "img2img" -> is_img2img is `True`
    #
    # below code always show extension menu
    def show(self, is_img2img):
        print('----------------custom extension show')
        return scripts.AlwaysVisible

    # Setup menu ui detail
    def ui(self, is_img2img):
        print('----------------custom extension ui')
        return None

    # Extension main process
    # Type: (StableDiffusionProcessing, List<UI>) -> (Processed)
    # args is [StableDiffusionProcessing, UI1, UI2, ...]
    def run(self, p, angle='', checkbox=''):
        print('----------------custom extension run')
        # TODO: get UI info through UI object angle, checkbox
        proc = process_images(p)
        # TODO: add image edit process via Processed object proc
        return proc
