import os
import subprocess
import sys
from time import sleep

try:
    from queue import Empty
except ImportError:
    from Queue import Empty


is_windows = sys.platform == 'win32'


def beep():
    """
    Emits a beep sound.
    """
    sys.stdout.write('\a')
    sys.stdout.flush()


def clear():
    """
    Clears the terminal.
    """
    subprocess.call('cls' if is_windows else 'clear', shell=True)


def dequeue_all(queue, spool=False):
    """
    Empties the specified queue into a list, optionally with spool time.
    """
    items = []
    while True:
        try:
            while True:
                items.append(queue.get_nowait())
        except Empty:
            # If spooling, wait a moment and check for new items
            if spool:
                sleep(0.2)
                if not queue.empty():
                    continue
            break
    return items


def samepath(left, right):
    """
    Determines whether two paths are the same.
    """
    return (os.path.abspath(os.path.normcase(left)) ==
            os.path.abspath(os.path.normcase(right)))
