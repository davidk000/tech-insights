# CANN GitCode 仓库列表

> 数据来源：https://gitcode.com/org/cann/repos
> 抓取时间：2026-04-03
> 共 48 个代码仓

---

## Git 克隆地址格式

```
https://gitcode.com/cann/{repo-name}.git
```

---

## 完整仓库列表

### Page 1（10个）

| 序号 | 仓库名 | Git 地址 |
|:---:|:---|:---|
| 1 | ops-math | https://gitcode.com/cann/ops-math.git |
| 2 | runtime | https://gitcode.com/cann/runtime.git |
| 3 | pypto | https://gitcode.com/cann/pypto.git |
| 4 | hcomm | https://gitcode.com/cann/hcomm.git |
| 5 | ge | https://gitcode.com/cann/ge.git |
| 6 | pto-isa | https://gitcode.com/cann/pto-isa.git |
| 7 | ops-nn | https://gitcode.com/cann/ops-nn.git |
| 8 | ascend-transformer-boost | https://gitcode.com/cann/ascend-transformer-boost.git |
| 9 | metadef | https://gitcode.com/cann/metadef.git |
| 10 | ops-transformer | https://gitcode.com/cann/ops-transformer.git |

### Page 2（10个）

| 序号 | 仓库名 | Git 地址 |
|:---:|:---|:---|
| 11 | asc-devkit | https://gitcode.com/cann/asc-devkit.git |
| 12 | cann-recipes-infer | https://gitcode.com/cann/cann-recipes-infer.git |
| 13 | cann-samples | https://gitcode.com/cann/cann-samples.git |
| 14 | community | https://gitcode.com/cann/community.git |
| 15 | hccl | https://gitcode.com/cann/hccl.git |
| 16 | hixl | https://gitcode.com/cann/hixl.git |
| 17 | ops-cv | https://gitcode.com/cann/ops-cv.git |
| 18 | pyasc | https://gitcode.com/cann/pyasc.git |
| 19 | shmem | https://gitcode.com/cann/shmem.git |
| 20 | skills | https://gitcode.com/cann/skills.git |

### Page 3（10个）

| 序号 | 仓库名 | Git 地址 |
|:---:|:---|:---|
| 21 | amct | https://gitcode.com/cann/amct.git |
| 22 | asc-tools | https://gitcode.com/cann/asc-tools.git |
| 23 | cann-learning-hub | https://gitcode.com/cann/cann-learning-hub.git |
| 24 | cann-recipes-embodied-intelligence | https://gitcode.com/cann/cann-recipes-embodied-intelligence.git |
| 25 | cann-recipes-train | https://gitcode.com/cann/cann-recipes-train.git |
| 26 | catlass | https://gitcode.com/cann/catlass.git |
| 27 | driver | https://gitcode.com/cann/driver.git |
| 28 | graph-autofusion | https://gitcode.com/cann/graph-autofusion.git |
| 29 | mat-chem-sim-pred | https://gitcode.com/cann/mat-chem-sim-pred.git |
| 30 | oam-tools | https://gitcode.com/cann/oam-tools.git |

### Page 4（10个）

| 序号 | 仓库名 | Git 地址 |
|:---:|:---|:---|
| 31 | ascend-boost-comm | https://gitcode.com/cann/ascend-boost-comm.git |
| 32 | asnumpy | https://gitcode.com/cann/asnumpy.git |
| 33 | atvc | https://gitcode.com/cann/atvc.git |
| 34 | atvoss | https://gitcode.com/cann/atvoss.git |
| 35 | cann-spack-package | https://gitcode.com/cann/cann-spack-package.git |
| 36 | infrastructure | https://gitcode.com/cann/infrastructure.git |
| 37 | opbase | https://gitcode.com/cann/opbase.git |
| 38 | ops-blas | https://gitcode.com/cann/ops-blas.git |
| 39 | sip | https://gitcode.com/cann/sip.git |
| 40 | triton-inference-server-ge-backend | https://gitcode.com/cann/triton-inference-server-ge-backend.git |

### Page 5（8个）

| 序号 | 仓库名 | Git 地址 |
|:---:|:---|:---|
| 41 | cann-agreements | https://gitcode.com/cann/cann-agreements.git |
| 42 | cann-recipes-harmony-infer | https://gitcode.com/cann/cann-recipes-harmony-infer.git |
| 43 | cann-recipes-spatial-intelligence | https://gitcode.com/cann/cann-recipes-spatial-intelligence.git |
| 44 | elec-ops-inspection | https://gitcode.com/cann/elec-ops-inspection.git |
| 45 | elec-ops-prediction | https://gitcode.com/cann/elec-ops-prediction.git |
| 46 | elec-ops-simulation | https://gitcode.com/cann/elec-ops-simulation.git |
| 47 | manifest | https://gitcode.com/cann/manifest.git |
| 48 | release-management | https://gitcode.com/cann/release-management.git |

---

## 批量克隆脚本

```bash
# 克隆所有仓库
for repo in ops-math runtime pypto hcomm ge pto-isa ops-nn ascend-transformer-boost metadef ops-transformer \
  asc-devkit cann-recipes-infer cann-samples community hccl hixl ops-cv pyasc shmem skills \
  amct asc-tools cann-learning-hub cann-recipes-embodied-intelligence cann-recipes-train catlass driver graph-autofusion mat-chem-sim-pred oam-tools \
  ascend-boost-comm asnumpy atvc atvoss cann-spack-package infrastructure opbase ops-blas sip triton-inference-server-ge-backend \
  cann-agreements cann-recipes-harmony-infer cann-recipes-spatial-intelligence elec-ops-inspection elec-ops-prediction elec-ops-simulation manifest release-management; do
  git clone https://gitcode.com/cann/${repo}.git
done
```
