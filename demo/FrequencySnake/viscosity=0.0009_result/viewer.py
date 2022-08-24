from mujoco_py import load_model_from_path

from demo.FrequencySnake.OneTest import oneTest

model = load_model_from_path("FreqSwimmer6.xml")
#              view  plot
# amplitude, omega, lamda, y = 80.0, 0.2, 20.0, 0.2   # s=0 v=0.12
# amplitude, omega, lamda, y = 150.0, 0.5, 30.0, 1.0    # s=2 v=0.2
amplitude, omega, lamda, y = 50.0, 0.5, 40.0, 0.8    # s=2 v=0.12
average_velocity, fp, v = oneTest(model, True, True, 0, 0, 0, amplitude, omega, lamda, y)
file = open("GE_s=2_v=0.12.txt", 'w')
file.writelines(str(v))
