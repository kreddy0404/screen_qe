import sys

import tasks


def main(task, path='/usr/src/data'):
    getattr(tasks, task)(path)


if __name__ == "__main__":
    main(sys.argv[1].split('--')[-1])
