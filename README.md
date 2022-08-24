# Project_SpinupEnv

.
├── demo
│   ├── ant.xml
│   ├── arm26.xml
│   ├── FrequencySnake
│   │   ├── FreqSwimmer6.py
│   │   ├── FreqSwimmer6Test.py
│   │   ├── FreqSwimmer6_torque.py
│   │   ├── FreqSwimmer6_torque.xml
│   │   ├── FreqSwimmer6.xml
│   │   ├── MUJOCO_LOG.TXT
│   │   ├── OneTest.py
│   │   ├── pic
│   │   │   ├── 0.0001compare.jpg
│   │   │   ├── 0.0001compare.pdf
│   │   │   ├── 0.01compare.jpg
│   │   │   ├── 0.01compare.pdf
│   │   │   ├── compare.jpg
│   │   │   ├── compare.pdf
│   │   │   ├── DRL_max_v.pdf
│   │   │   ├── DRL.pdf
│   │   │   ├── DRL_p_of_target_v.jpg
│   │   │   ├── DRL_p_of_target_v.pdf
│   │   │   ├── DRL_p_of_target_v.png
│   │   │   ├── DRL_v=0.12_p.pdf
│   │   │   ├── DRL_v=0.12_v.pdf
│   │   │   ├── equation.pdf
│   │   │   ├── GE_max_v.pdf
│   │   │   ├── GE.pdf
│   │   │   ├── GE_p_of_target_v.jpg
│   │   │   ├── GE_p_of_target_v.pdf
│   │   │   ├── GE_p_of_target_v.png
│   │   │   ├── GE_v=0.12_p.pdf
│   │   │   ├── GE_v=0.12_v.pdf
│   │   │   ├── max_v.jpg
│   │   │   ├── max_v.pdf
│   │   │   ├── p.pdf
│   │   │   ├── reward.jpg
│   │   │   ├── reward.pdf
│   │   │   ├── reward.png
│   │   │   ├── s=0_compare.png
│   │   │   ├── s=0_contour.pdf
│   │   │   ├── s=0_DRL.jpg
│   │   │   ├── s=0_DRL.png
│   │   │   ├── s=0_GE.pdf
│   │   │   ├── s=0_GE.png
│   │   │   ├── s=0_p.pdf
│   │   │   ├── s=0_sin.jpg
│   │   │   ├── s=0_v.pdf
│   │   │   ├── s=2_DRL.jpg
│   │   │   ├── s=2_p.pdf
│   │   │   ├── s=2_s=4.jpg
│   │   │   ├── s=2_s=4.pdf
│   │   │   ├── s=2_s=4.png
│   │   │   ├── s=2_sin.jpg
│   │   │   ├── s=2_v.pdf
│   │   │   └── v.pdf
│   │   ├── PID.py
│   │   ├── plot.py
│   │   ├── pltR.py
│   │   ├── __pycache__
│   │   │   ├── OneTest.cpython-36.pyc
│   │   │   ├── PID.cpython-36.pyc
│   │   │   └── plot.cpython-36.pyc
│   │   ├── RLsnake
│   │   │   ├── main2.py
│   │   │   ├── main3.py
│   │   │   ├── main.py
│   │   │   ├── MUJOCO_LOG.TXT
│   │   │   ├── plotReward.py
│   │   │   ├── runRLresult.py
│   │   │   ├── swimmer6.py
│   │   │   └── swimmer6.xml
│   │   ├── test
│   │   │   ├── test_kp.py
│   │   │   └── test.xml
│   │   ├── testMaxP.py
│   │   ├── testPID.py
│   │   ├── test.xml
│   │   ├── viewer.py
│   │   ├── viewer_torque.py
│   │   ├── viscosity=0.0001_result
│   │   │   ├── FreqSwimmer6.py
│   │   │   ├── FreqSwimmer6.xml
│   │   │   ├── plot_result.py
│   │   │   └── viewer.py
│   │   ├── viscosity=0.0009_result
│   │   │   ├── 150.0_0.5_30.0_1.0_s=2_v=0.201.txt
│   │   │   ├── 80.0_0.2_20.0_0.2_s=0_v=0.117.txt
│   │   │   ├── DRL_s=0_v=0.124.txt
│   │   │   ├── DRL_s=2_v=0.12.txt
│   │   │   ├── DRL_s=2_v=0.199.txt
│   │   │   ├── FreqSwimmer6.py
│   │   │   ├── FreqSwimmer6.xml
│   │   │   ├── GE_s=2_v=0.12.txt
│   │   │   ├── plot_P.py
│   │   │   ├── plot_result.py
│   │   │   ├── plot_vel.py
│   │   │   ├── plot_v_P.py
│   │   │   ├── viewer.py
│   │   │   └── vp2_spring.pdf
│   │   └── viscosity=0.01_result
│   │       ├── compare.eps
│   │       ├── equation.png
│   │       ├── FreqSwimmer6.py
│   │       ├── FreqSwimmer6.xml
│   │       ├── plot_result.py
│   │       └── viewer.py
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
