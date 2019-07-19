import argparse
from .beautify import plot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logdir', type=str, help='Path to event files')
    parser.add_argument('--smooth', default=100, type=float, help='window size for average smoothing')
    args = parser.parse_args()

    plot(args.logdir, args.smooth)


if __name__ == '__main__':
    main()
