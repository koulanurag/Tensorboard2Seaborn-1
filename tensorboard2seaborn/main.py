import argparse
from .beautify import plot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logdir', type=str, help='Path to event files', required=True)
    parser.add_argument('--smoothing', default=0.6, type=float,
                        help='smoothing scale .It should be in [0,1] (default: %(default)s)')
    parser.add_argument('--no_title', action='store_true', default=False,
                        help='Doesn\'t show title in any of the graphs')
    parser.add_argument('--no_legend', action='store_true', default=False,
                        help='Doesn\'t show legend in any of the graphs')
    parser.add_argument('--no_axis_labels', action='store_true', default=False,
                        help='Doesn\'t show axis labels in any of the graphs')

    args = parser.parse_args()

    plot(logdir=args.logdir, savedir=args.logdir, smoothing=args.smoothing,
         no_title=args.no_title, no_legend=args.no_legend, no_axis_labels=args.no_axis_labels)


if __name__ == '__main__':
    main()
