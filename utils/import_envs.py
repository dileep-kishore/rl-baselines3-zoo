try:
    import pybullet_envs  # pytype: disable=import-error
except ImportError:
    pybullet_envs = None

try:
    import highway_env  # pytype: disable=import-error
except ImportError:
    highway_env = None

try:
    import neck_rl  # pytype: disable=import-error
except ImportError:
    neck_rl = None

try:
    import mocca_envs  # pytype: disable=import-error
except ImportError:
    mocca_envs = None

try:
    import custom_envs  # pytype: disable=import-error
except ImportError:
    custom_envs = None

try:
    import gym_donkeycar  # pytype: disable=import-error
except ImportError:
    gym_donkeycar = None

try:
    import panda_gym  # pytype: disable=import-error
except ImportError:
    panda_gym = None

try:
    from relearn.environments import dFBAEnv
    from gym.envs.registration import register

    param_dict = {
        "C0,in": 20,
        "q": 0.5,
        "vmax": [10.0, 5.0],
        "vmax0": [5.0, 5.0],
        "Km0": [1e-4, 1e-4],
        "Km": [2e-3, 1e-3],
        "models": [
            "../../ReLearn/data/covert/mutant1.json",
            "../../ReLearn/data/covert/mutant2.json",
        ]
    }
    env_dict = {
      "initial_N": [
        [2, 3],
        [3, 3],
        [2, 2],
        [3, 2]
      ],
      "target_N": [
        [2, 3],
        [3, 3],
        [2, 2],
        [3, 2]
      ],
      "initial_C": [0.0, 0.0],
      "initial_C0": 10.0,
      "Cin_bounds": [0.0, 20],
      "sampling_rate": 0.0833
    }
    register(
        id="dFBA-v1",
        entry_point=dFBAEnv,
        max_episode_steps=200,
        kwargs={"param_dict": param_dict, "env_dict": env_dict, "dt": 1/720, "ep_length": 200}
    )
except ImportError:
    dFBAEnv = None
