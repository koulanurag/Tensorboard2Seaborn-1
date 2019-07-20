import os
import seaborn as sns
import matplotlib.pyplot as plt
from tensorboard.backend.event_processing import event_accumulator as ea


def plot(logdir: str, savedir: str, smooth: int = 100, ):
    """ re-draw the tf summary events plots  using seaborn
    :param logdir: Path to the directory having event logs
    :param savedir: Path to save the seaborn graphs
    :param smooth: smoothing value for the plots
    """

    scalars_info = {}
    for root, dirs, files in os.walk(logdir):
        for event_file in [x for x in files if 'tfevents' in x]:  # we recognize all files which have tfevents
            event_path = os.path.join(root, event_file)

            acc = ea.EventAccumulator(event_path)
            acc.Reload()

            # only support scalar now
            scalar_list = acc.Tags()['scalars']
            for tag in scalar_list:
                x = [s.step for s in acc.Scalars(tag)]
                y = [s.value for s in acc.Scalars(tag)]
                data = {'x': x, 'y': y, 'legend': ''}
                if tag not in scalars_info:
                    scalars_info[tag] = [data]
                else:
                    scalars_info[tag].append(data)

    for tag, tag_data in scalars_info.items():
        _split = tag.split('/')
        if len(_split) < 1:
            _path = os.path.join(logdir, 'seaborn')
            _name = _split[0]
        else:
            _path = os.path.join(logdir, 'seaborn', _split[0])
            _name = ''.join(_split[1:])

        os.makedirs(_path, exist_ok=True)

        for data in tag_data:
            _plt = sns.lineplot(data['x'], data['y'], label='label')
        _plt.set(xlabel='x', ylabel='y')
        _plt.set_title('title')

        plt.savefig(os.path.join(_path, _name + '.png'))
        plt.clf()
