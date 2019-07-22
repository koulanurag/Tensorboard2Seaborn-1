import argparse
from .beautify import plot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logdir', type=str, help='Path to event files', required=True)
    parser.add_argument('--smoothing', default=0.6, type=float,
                        help='smoothing scale .It should be in [0,1] (default: %(default)s)')
    args = parser.parse_args()

    plot(logdir=args.logdir, savedir=args.logdir, smoothing=args.smoothing)


if __name__ == '__main__':
    main()
