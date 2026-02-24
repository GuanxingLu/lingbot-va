# Copyright 2024-2025 The Robbyant Team Authors. All rights reserved.
from easydict import EasyDict
from .va_franka_cfg import va_franka_cfg

va_franka_i2va_cfg = EasyDict(__name__='Config: VA franka i2va')
va_franka_i2va_cfg.update(va_franka_cfg)

va_franka_i2va_cfg.input_img_path = 'example/franka'
va_franka_i2va_cfg.num_chunks_to_infer = 1  # Reduce chunks (was 10), generates x4 frames
va_franka_i2va_cfg.prompt = 'pick bunk'
va_franka_i2va_cfg.infer_mode = 'i2va'
va_franka_i2va_cfg.num_layers = 1
va_franka_i2va_cfg.ignore_mismatched_sizes = True

va_franka_i2va_cfg.guidance_scale = 1.0  # Disable CFG to reduce memory (was 5)
va_franka_i2va_cfg.num_inference_steps = 1
va_franka_i2va_cfg.action_num_inference_steps = 1
