
from legged_gym import LEGGED_GYM_ROOT_DIR, LEGGED_GYM_ENVS_DIR
from legged_gym.envs.a1.a1_config import A1RoughCfg, A1RoughCfgPPO
from .base.legged_robot import LeggedRobot
import os

from legged_gym.utils.task_registry import task_registry

from .a1.a1_config import A1RoughCfg, A1RoughCfgPPO

task_registry.register( "a1", LeggedRobot, A1RoughCfg(), A1RoughCfgPPO() )


from .g1.g1_12dof_walk.g1_env import G1_12dof_walk
from .g1.g1_12dof_walk.g1_config import G1_12dof_Cfg, G1_12dof_CfgPPO  
task_registry.register( "g1_12dof_walk", G1_12dof_walk, G1_12dof_Cfg(), G1_12dof_CfgPPO() )

from .g1.g1_29dof_walk.g1_env import G1_29dof_walk
from .g1.g1_29dof_walk.g1_config import G1Cfg, G1CfgPPO  
task_registry.register( "g1_29dof_walk", G1_29dof_walk, G1Cfg(), G1CfgPPO() )


