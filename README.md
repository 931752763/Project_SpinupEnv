# Project_SpinupEnv
```bash
.
├── demo
│   ├── ant.xml
│   ├── arm26.xml
=========================================================================
│   ├── FrequencySnake                          # main code is here
│   │   ├── FreqSwimmer6.py                     # simulation for GE controller, model using FreqSwimmer6.xml in the same folder
│   │   ├── FreqSwimmer6Test.py
│   │   ├── FreqSwimmer6_torque.py              # simulation for GE controller, model using FreqSwimmer6_torque.xml in the same folder
│   │   ├── FreqSwimmer6_torque.xml             # XML for GE controller, using torque controller
│   │   ├── FreqSwimmer6.xml                    # XML for GE controller, using position controller
│   │   ├── MUJOCO_LOG.TXT
│   │   ├── OneTest.py                          # simulation one time
│   │   ├── pic                                 # result pictures
│   │   │   ├── 0.0001compare.jpg
│   │   │   ├── .......
│   │   │   └── v.pdf
│   │   ├── PID.py                              
│   │   ├── plot.py                             # method for plot result
│   │   ├── pltR.py                             # some test for reward function
│   │   ├── __pycache__
│   │   │   ├── OneTest.cpython-36.pyc
│   │   │   ├── PID.cpython-36.pyc
│   │   │   └── plot.cpython-36.pyc
│   │   ├── RLsnake                             # for DRL simulation
│   │   │   ├── main2.py
│   │   │   ├── main3.py
│   │   │   ├── main.py                         # main method for DRL simulation
│   │   │   ├── MUJOCO_LOG.TXT
│   │   │   ├── plotReward.py                   # plot DRL reward result
│   │   │   ├── runRLresult.py                  # view DRL training result
│   │   │   ├── swimmer6.py                     # this py is not used
│   │   │   └── swimmer6.xml                    # this xml is not used
│   │   ├── test
│   │   │   ├── test_kp.py
│   │   │   └── test.xml
│   │   ├── testMaxP.py
│   │   ├── testPID.py
│   │   ├── test.xml
│   │   ├── viewer.py                           # view GE result
│   │   ├── viewer_torque.py
│   │   ├── viscosity=0.0001_result
│   │   │   ├── FreqSwimmer6.py
│   │   │   ├── FreqSwimmer6.xml
│   │   │   ├── plot_result.py
│   │   │   └── viewer.py
│   │   ├── viscosity=0.0009_result                 # three "viscosity=xxxxxx_result" folder is similar
│   │   │   ├── 150.0_0.5_30.0_1.0_s=2_v=0.201.txt
│   │   │   ├── 80.0_0.2_20.0_0.2_s=0_v=0.117.txt
│   │   │   ├── DRL_s=0_v=0.124.txt
│   │   │   ├── DRL_s=2_v=0.12.txt
│   │   │   ├── DRL_s=2_v=0.199.txt                 # speed data for plot is recoreded in these .txt file
│   │   │   ├── FreqSwimmer6.py                     # simulation for GE controller, model using FreqSwimmer6.xml in the same folder
│   │   │   ├── FreqSwimmer6.xml                    # XML for GE controller, using position controller
│   │   │   ├── GE_s=2_v=0.12.txt
│   │   │   ├── plot_P.py                           # plot the bar picture (energy cosumption for different joint)
│   │   │   ├── plot_result.py                      # the main results are plotted here
│   │   │   ├── plot_vel.py                         # plot velocity, using those .txt files in this folder
│   │   │   ├── plot_v_P.py                         # combine plot_vel and plot_P
│   │   │   ├── viewer.py                           # view the results of DRL controller
│   │   │   └── vp2_spring.pdf                      
│   │   └── viscosity=0.01_result
│   │       ├── compare.eps
│   │       ├── equation.png
│   │       ├── FreqSwimmer6.py
│   │       ├── FreqSwimmer6.xml
│   │       ├── plot_result.py
│   │       └── viewer.py
==================================================================
│   ├── main.py
│   ├── myManta
│   │   ├── main.py
│   │   ├── manta.py
│   │   ├── manta-v1.xml
│   │   ├── manta-v2.xml
│   │   └── manta-v3-2connector.xml
│   ├── slider.xml
│   ├── swimmer.xml
│   └── udrf.xml
├── MUJOCO_LOG.TXT
└── myswimmer
    ├── __init__.py
    ├── myenv
    │   ├── __init__.py
    │   ├── models
    │   │   ├── common
    │   │   │   ├── __init__.py
    │   │   │   ├── materials.xml
    │   │   │   ├── skybox.xml
    │   │   │   └── visual.xml
    │   │   ├── __init__.py
    │   │   └── swimmer5.xml
    │   ├── __pycache__
    │   │   └── swimmer5.cpython-36.pyc
    │   └── swimmer5.py
    └── runswimmer
        ├── runswimmer5.py
        └── spinup_record
            └── swimmer5
                ├── config.json
                └── progress.txt
                
/home/zheng/spinningup/spinup/algos/tf1/ppo/ppo.py          # PPO algo for DRL controller, I edited this file
/home/zheng/anaconda3/envs/spinningupEnv/lib/python3.6/site-packages/gym/envs/mujoco/RLsnake/swimmer6.py    # this also used for DRL controller
/home/zheng/anaconda3/envs/spinningupEnv/lib/python3.6/site-packages/gym/envs/mujoco/RLsnake/swimmer6.xml   # the xml model for DRL controller
```
So the whole process is like this:
Run GE controller: 

