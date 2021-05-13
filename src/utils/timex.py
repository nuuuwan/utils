"""Time utils."""
import time


class StopWatch:
    """Implements StopWatch.

    .. code-block:: python

        >>> import time
        >>> from utils import timex
        >>> sw = timex.StopWatch()
        >>> time.sleep(3)
        >>> print(sw.stop('Test'))
        3930.06706237793

    """

    def __init__(self):
        """__init__."""
        self.reset()

    def reset(self):
        """Reset StopWatch."""
        self.t_start = time.time()

    def stop(self, label=""):
        """Stop StopWatch, print and return elapsed time.

        Args:
            label(str, optional): Optional label to prefix the output

        Return:
            Elapsed time in miliseconds (float)

        """
        delta_t = (time.time() - self.t_start) * 1000
        print('{label} {delta_t}ms'.format(label=label, delta_t=delta_t))
        return delta_t