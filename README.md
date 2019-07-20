# tensorboard2seaborn 🌈
Plot Tensorflow's Summary event in a beautiful way (using seaborn actually) instead of using Tensorboard.

## Installation
```bash
cd tensorboard2seaborn
python setup.py install
```

## Usage:
#### Terminal:
```bash
usage: tensorboard2seaborn [-h] [--logdir LOGDIR] [--smooth SMOOTH]
optional arguments:
  -h, --help       show this help message and exit
  --logdir LOGDIR  Path to event files
  --smooth SMOOTH  window size for average smoothing
```

Example: ```tensorboard2seaborn --logdir=/experiments/logs --smooth=0.95```

#### Console: 
```python
import tensorboard2seaborn

tensorboard2seaborn.plot(logdir='/experiments/logs')
```
