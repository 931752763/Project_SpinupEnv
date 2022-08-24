from mujoco_py import load_model_from_path

from demo.FrequencySnake.OneTest import oneTest

model = load_model_from_path("FreqSwimmer6.xml")
#              view  plot
oneTest(model, True, True, 20, 0, 0, 60, 0.2, 20, 0.4)
