from ._pattern import Pattern

class SSDP:
  def __init__(self, target):
    self.target = target

  def run(self, k, eval_metric) -> "list[Pattern]":
    p = Pattern(k, eval_metric)
    return [p for n in range(k)]
